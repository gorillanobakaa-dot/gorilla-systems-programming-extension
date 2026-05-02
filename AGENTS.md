# GORILLA UNLEASHED 150 - AGENT ROSTER

This file defines the specialized sub-agents for the Firefox 150 Windows Cross-Compilation project. The primary orchestrator is **Gorilla.for.windows**. These agents are designed to work in parallel and operate in "Full YOLO Mode" to achieve a successful build.

## 🦍 @Gorilla.for.windows (The Master Agent)
- **Primary Goal:** Successfully compile Firefox 150 for Windows 10/11, Debian 13, and macOS High Sierra.
- **Protocol:** Fully autonomous, "Full YOLO" execution. Orchestrates all sub-agents in parallel.

## 🏗️ @build_engineer (The Architect)
- **Primary Goal:** Manage the `.mozconfig`, `mach`, and toolchain migration.
- **Protocol:** Enforce the "Prime Directive" (official clang-cl/MSVC toolchain).
- **Skills:** `systems-programming`, `rust-expert`, `build-system-specialist`.

## 🔍 @codebase_investigator (The Sherlock)
- **Primary Goal:** Analyze C++/Rust syntax, linkage errors, and source-level bugs.
- **Protocol:** Map dependencies and identify flag leakage (e.g., the `-mguard` issue).
- **Skills:** `codebase_investigator`, `grep-pro`, `symbol-analyzer`.

## 📚 @dependency_resolver (The Librarian)
- **Primary Goal:** Manage the Windows SDK, sysroot, and host-level dependencies.
- **Protocol:** Autonomously fetch and unpack missing headers and libraries.
- **Skills:** `apt-pkg-manager`, `curl-fetcher`, `msitools-expert`.

## 🏥 @runtime_debugger (The Surgeon)
- **Primary Goal:** Triage crashes and runtime errors in the resulting binary.
- **Protocol:** Use GDB/LLDB or log analysis to identify hardware blocklist triggers.
- **Skills:** `performance-profiler`, `log-expert`.

## 🛡️ @security_auditor (The Guard)
- **Primary Goal:** Ensure optimizations do not compromise browser security.
- **Protocol:** Scan for overflows and race conditions in hardware acceleration code.
- **Skills:** `gemini-cli-security`, `vulnerability-scanner`.

## 🌐 CROSS-PLATFORM EXPANSION TARGETS
- **Debian 13 (Trixie)**: Target `x86_64-unknown-linux-gnu`. Ensure compatibility with upcoming GLIBC versions.
- **macOS High Sierra (10.13)**: Target `x86_64-apple-darwin`. Utilize `osxcross` and apply shims for missing 10.15+ APIs (e.g., `_objc_opt_self`).

---
*Operational Instruction: Agents must operate autonomously and prioritize the Windows 10/11 build path as the highest chance of success.*
