validate: fmt clippy

build: cargo build --release

clean: cargo clean

docker: docker compose build

doc: cargo doc --no-deps

test: cargo test --all-features

fmt: cargo fmt

clippy: cargo clippy --all-targets

release: cargo build --release

ci: validate test
