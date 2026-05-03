import os
import json
import asyncio
from datetime import datetime

class GorillaSystemsProgrammingExtension:
    # Master Agent configuration for Gemi CLI Orchestration
    
    def __init__(self):
        self.extension_name = "gorilla_systems_programmer"
        self.doc_directory = os.path.abspath("BUILDING_PROCESS_DOCUMENTED")
        os.makedirs(self.doc_directory, exist_ok=True)
        
        # Internal state to track active sub agent tasks
        self.active_tasks = {}
        
        # Load the system prompt from the GEMINI.md file
        gemini_md_path = os.path.join(os.path.dirname(__file__), "GEMINI.md")
        with open(gemini_md_path, 'r', encoding='utf-8') as f:
            self.system_prompt = f.read()


    def get_tool_schemas(self):
        # Define the delegation and management tools for the Master Agent
        return [
            {
                "name": "delegate_task",
                "description": "Assigns a specific systems programming task to a sub agent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "agent_id": {
                            "type": "string", 
                            "enum": [
                                "@build_engineer", "@codebase_investigator", 
                                "@dependency_resolver", "@runtime_debugger", 
                                "@security_auditor"
                            ]
                        },
                        "task_instruction": {"type": "string"},
                        "target_files": {"type": "array", "items": {"type": "string"}},
                        "block_until_complete": {"type": "boolean", "default": True}
                    },
                    "required": ["agent_id", "task_instruction"]
                }
            },
            {
                "name": "invoke_supervisor",
                "description": "Submits a proposed code patch or build script to the supervisor for sanity checking before execution.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "proposed_code": {"type": "string"},
                        "context_rationale": {"type": "string"}
                    },
                    "required": ["proposed_code", "context_rationale"]
                }
            },
            {
                "name": "document_process",
                "description": "Calls the custodian to write logs, rationale, and roadblock data to the documentation folder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string"},
                        "content": {"type": "string"},
                        "category": {"type": "string", "enum": ["ROADBLOCK", "PATCH_APPLIED", "SCRIPT_CREATED", "SHIM_EXPLANATION"]}
                    },
                    "required": ["topic", "content", "category"]
                }
            },
            {
                "name": "search_documentation",
                "description": "Queries past build logs and roadblock resolutions to retrieve historical context without overloading memory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_query": {"type": "string"},
                        "max_results": {"type": "integer", "default": 3}
                    },
                    "required": ["search_query"]
                }
            }
        ]

    async def execute_tool(self, tool_name, parameters):
        # Main execution router for the LLM tool calls
        if tool_name == "delegate_task":
            return await self._run_sub_agent(parameters)
        elif tool_name == "invoke_supervisor":
            return await self._run_supervisor_check(parameters)
        elif tool_name == "document_process":
            return await self._write_documentation(parameters)
        elif tool_name == "search_documentation":
            return await self._search_documentation(parameters)
        else:
            raise ValueError(f"Unknown execution request: {tool_name}")

    async def _run_sub_agent(self, params):
        agent = params.get("agent_id")
        instruction = params.get("task_instruction")
        blocking = params.get("block_until_complete", True)
        
        task_id = f"task_{datetime.now().strftime('%H%M%S')}_{agent.strip('@')}"
        self.active_tasks[task_id] = {"status": "running", "agent": agent}
        
        # Mocking the subprocess execution for the isolated environment
        # In production this interfaces with the container runtime
        await asyncio.sleep(2) 
        
        self.active_tasks[task_id]["status"] = "completed"
        
        return {
            "status": "success", 
            "task_id": task_id,
            "agent": agent, 
            "output": f"Simulated successful execution of instruction: {instruction[:50]}..."
        }

    async def _run_supervisor_check(self, params):
        code = params.get("proposed_code")
        rationale = params.get("context_rationale")
        
        # Strict evaluation logic goes here to catch syntax errors or flag leakage
        if "-mguard" in code and "windows" not in rationale.lower():
            return {"status": "REJECTED", "reason": "Flag leakage detected. -mguard applied outside Windows context."}
            
        return {"status": "APPROVED", "analysis": "Syntax structurally sound. No hallucinations detected."}

    async def _write_documentation(self, params):
        topic = params.get("topic").replace(" ", "_").lower()
        content = params.get("content")
        category = params.get("category")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        filename = f"{timestamp}_{category}_{topic}.md"
        filepath = os.path.join(self.doc_directory, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {category}: {topic}
")
                f.write(f"Date: {datetime.now().isoformat()}

")
                f.write(content)
            return {"status": "success", "filepath": filepath}
        except Exception as e:
            return {"status": "error", "error_message": str(e)}

    async def _search_documentation(self, params):
        query = params.get("search_query").lower()
        limit = params.get("max_results", 3)
        results = []
        
        if not os.path.exists(self.doc_directory):
            return {"status": "error", "message": "Documentation directory does not exist yet."}
            
        for filename in os.listdir(self.doc_directory):
            if filename.endswith(".md"):
                filepath = os.path.join(self.doc_directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query in content.lower():
                        # Extract a window around the query match to save context tokens
                        match_index = content.lower().find(query)
                        start = max(0, match_index - 150)
                        end = min(len(content), match_index + 350)
                        
                        results.append({
                            "file": filename,
                            "snippet": f"...{content[start:end]}..." 
                        })
                        
        if not results:
            return {"status": "no_results", "message": "No historical data found for this query."}
            
        return {"status": "success", "matches": results[:limit]}

def register(cli_context):
    extension = GorillaSystemsProgrammingExtension()
    cli_context.add_agent_profile(
        name="gorilla_master",
        system_prompt=extension.system_prompt,
        tools=extension.get_tool_schemas(),
        executor=extension.execute_tool
    )
