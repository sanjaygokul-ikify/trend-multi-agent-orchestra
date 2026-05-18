# Contributing to Multi-Agent Orchestra

## Code of Conduct
We are committed to providing a welcoming environment. Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Getting Started
1. Fork the repository
2. Create a feature branch for your work
3. Run `make validate` to check code quality

## Development Workflow
We recommend installing the latest stable Rust toolchain with `rustup`. The project requires:
- WebAssembly target (`wasm32-unknown-unknown`)
- `protoc` compiler (v3.21+)
- `cargo-contract` (Substrate integration)

## Security
All contributions must pass
1. Rust clippy
2. MIRAI static analysis
3. WebAssembly safety checks
4. Provenance audit trail validation

## Reporting Issues
To report security vulnerabilities, please email security@multiagentorchestra.com