# Gorilla Systems Programming Extension: Official Manual

## 🦍 Overview
The **Systems Programming Extension (Gorilla Edition)** is a high-performance architectural framework designed for the Gemini CLI. It transforms the AI agent into the **MASTER ORCHESTRATION AGENT (Gorilla Systems)**, a senior collective capable of managing large-scale, multi-platform codebases with a focus on systems engineering, cross-compilation, and low-level optimization.

This extension was created in May 2026 to facilitate complex build processes, specifically for projects like **Firefox 150+** and modern **GNOME** desktop environments.

---

## 🛠️ Architecture: The Orchestration Model
Unlike standard extensions that perform tasks linearly, Gorilla Systems operates as a **Root Controller**. It designs, spawns, and coordinates specialized sub-agents that run in parallel.

### The Agent Roster
| Agent | Title | Primary Responsibility |
| :--- | :--- | :--- |
| **@build_engineer** | The Architect | Manages `.mozconfig`, `mach`, toolchains, and environment variables. |
| **@codebase_investigator** | The Sherlock | Analyzes C++ and Rust syntax, dependencies, and linkage graphs. |
| **@dependency_resolver** | The Librarian | Manages sysroots, Windows SDKs, and unpacking protocols. |
| **@runtime_debugger** | The Surgeon | Triages crashes, analyzes logs, and uses GDB/LLDB for deep inspection. |
| **@security_auditor** | The Guard | Scans for overflows, race conditions, and compromised optimizations. |
| **@quality_supervisor** | The Gatekeeper | Validates code sanity and prevents hallucinations or flag leakage. |
| **@custodian_archivist** | The Backer | Documents every step and roadblock in persistent markdown state. |

---

## 🎯 Primary Capabilities
- **Firefox 150+ Ecosystem**: Deep knowledge of Gecko, SpiderMonkey, and the `mozbuild` system.
- **Cross-Compilation Mastery**: Expert handling of Debian hosts targeting Windows 10/11 (MSVC) and legacy macOS (High Sierra/osxcross).
- **Desktop Engineering**: Integration and debugging for GNOME 48-51, Mutter, Wayland, and X11.
- **Systematic Debugging**: A strict protocol of: *Clarify constraints -> Isolate failure -> Analyze root cause -> Deploy surgical fix -> Validate.*

---

## 📜 Operating Principles
1. **The Prime Directive**: Always prioritize official toolchains (`clang-cl` + VS sysroot) for Windows over secondary alternatives like MinGW.
2. **Environment Isolation**: Maintain strictly separate and clean build environments for each target platform to prevent header leakage.
3. **Validation-First**: No change is considered successful until it has been empirically verified through the build system and tests.
4. **Persistent Memory**: Every significant action and failure is logged by the `@custodian_archivist` into `GEMINI.md` or `MEMORY.md` to ensure continuity across sessions.

---

## 🚀 Commands & Usage

### Starting the Agent
The extension is automatically loaded if installed. You can trigger its specialized logic by asking about system tasks:
> "Analyze the current Firefox build failure."
> "Configure a cross-compilation environment for Windows."

### Activating Specific Skills
You can manually activate the specialized skills contained within the extension:
- `activate_skill(name="build-system-specialist")`
- `activate_skill(name="rust-expert")`
- `activate_skill(name="custodian-archivist")`

### Example Workflow
1. **Research**: The `@codebase_investigator` identifies a missing C++17 trait in an old SDK.
2. **Strategy**: The `@build_engineer` proposes a shim header.
3. **Execution**: The `@quality_supervisor` verifies the shim doesn't break other targets.
4. **Archival**: The `@custodian_archivist` saves the result to the workspace memory.

---

## 📥 Installation & Deployment
To deploy this extension on a fresh Debian installation:

1. **Prerequisites**: Ensure `gemini-cli` is installed and authenticated.
2. **Manual Installation**:
   - Copy the `systems-programming` folder to `~/.gemini/extensions/`.
3. **CLI Installation (via Source)**:
   ```bash
   gemini extensions install /path/to/backup/Gorilla\ Systems\ Programming\ Extension
   ```
4. **Verification**:
   ```bash
   /extensions list
   ```

---

## 🗑️ Uninstallation
To remove the extension:
```bash
gemini extensions uninstall systems-programming
```
Or manually delete the directory:
```bash
rm -rf ~/.gemini/extensions/systems-programming
```

---

## ⚖️ Open Source Spirit
- **Created By**: Gemini CLI User "Gorilla" & Gemini AI.
- **License**: MIT / Open Source.
- **Philosophy**: Transparency, surgical precision, and architectural integrity.
