---
name: systems-programming
description: Use for low-level systems tasks, cross-compilation, and OS-level debugging.
---

# Systems Programming Skill

## Core Mandates
- **Memory Safety:** Always prioritize memory safety in C++/Rust. Use RAII, smart pointers, and borrow checker rules strictly.
- **Efficiency:** Minimize allocations and context switches. Use SIMD and zero-copy abstractions where applicable.
- **Portability:** Handle platform-specific shims (e.g., `_objc_opt_self` for macOS 10.13) via robust header inclusion or weak linkage.

## Procedures
- **Cross-Compilation:** Use `rustup target add` for Rust and `clang-cl` with `--sysroot` for C++.
- **Linkage:** Use `dump_syms` or `objdump` to verify symbol availability in the target SDK.
- **Build Orchestration:** Prefer `mach` for Firefox and `cargo` for Rust components. Handle `build.rs` failures by inspecting environment leakage.
