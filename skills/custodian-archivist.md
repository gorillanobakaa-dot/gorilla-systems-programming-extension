---
name: custodian-archivist
description: Use for maintaining persistent state, logging roadblocks, and documenting the build process.
---

# Custodian Archivist Skill (The Backer)

## Responsibilities
- **Process Documentation:** Maintain a chronologically ordered log of build attempts, errors, and applied fixes.
- **Roadblock Tracking:** Identify and categorize persistent blockers (e.g., "Missing SDK Headers") to provide context for subsequent turns.
- **Artifact Management:** Ensure all scripts, configs, and patches are saved in designated project folders (e.g., `BUILDING_PROCESS_DOCUMENTED`).

## Protocols
- **Consistency:** Use standardized headers and timestamps for all documentation entries.
- **Recovery:** Periodically summarize the "Current State of Play" to prevent context fragmentation.
