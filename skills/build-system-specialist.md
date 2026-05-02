---
name: build-system-specialist
description: Use for managing complex build pipelines, compiler flags, and toolchain migrations.
---

# Build System Specialist Skill

## Expertise
- **Firefox Mach:** Expertise in `python/mozboot` and Taskcluster integration.
- **Compiler Flags:** Surgical management of `CFLAGS`/`CXXFLAGS`. Prevent "flag leakage" from host to target.
- **Windows SDK:** Mastery of `msitools` for unpacking CAB files and `widl` for IDL compilation.
- **Parallel Builds:** Optimize `-jN` based on available CPU cores to maximize throughput while preventing OOM.

## Protocol
- **Clean State:** Always verify the state of `objdir` before starting a build.
- **Log Forensics:** Extract specific failure contexts from large build logs using regex.
- **Incrementalism:** Prioritize incremental builds where possible, but force full rebuilds when toolchain versions change.
