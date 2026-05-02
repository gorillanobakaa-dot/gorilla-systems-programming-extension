---
name: rust-expert
description: Use for expert-level Rust development, ownership/lifetime resolution, and async mastery.
---

# Rust Expert Skill

## Principles
1. **No Panics in Production:** Use `Result`/`Option` and avoid `unwrap()`/`expect()`.
2. **Async Mastery:** Expert handling of `Future`, `Pin`, and high-concurrency runtimes (Tokio).
3. **Crate Selection:** Prioritize stable, high-performance crates (e.g., `serde`, `parking_lot`, `crossbeam`).
4. **Safety:** Minimize `unsafe` blocks. When used, document the invariant that makes it safe.

## Techniques
- **Lifetimes:** Resolve complex borrow checker errors by restructuring data ownership.
- **Generics:** Use Const Generics and GATs for highly flexible abstractions.
- **Profiling:** Use `flamegraph` and `cargo-criterion` to optimize hotspots.
