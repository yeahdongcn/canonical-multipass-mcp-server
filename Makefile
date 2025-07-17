.PHONY: help env dev clean run debug test lint fmt publish

# Default target
help:
	@echo "Available targets:"
	@echo "  env      - Create/activate virtual environment and install main dependencies"
	@echo "  dev      - Install main and development dependencies"
	@echo "  clean    - Clean up temporary files and caches"
	@echo "  run      - Start the MCP server"
	@echo "  debug    - Start the MCP server in debug mode"
	@echo "  test     - Run unit tests (dev env)"
	@echo "  lint     - Run flake8 and mypy (dev env)"
	@echo "  fmt      - Format code with black (dev env)"
	@echo "  publish  - Build and publish wheel to PyPI using uv build && uv publish"
	@echo "  help     - Show this help message"

# Create virtual environment and install main dependencies
env:
	@echo "Setting up environment with uv..."
	uv sync
	@echo "Environment ready! Activate with: source .venv/bin/activate"

# Install for development (main + dev dependencies)
dev: env
	@echo "Installing main and development dependencies..."
	uv sync --extra dev

# Clean up
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleanup complete!"

# Start the MCP server
run: env
	@echo "Starting Canonical Multipass MCP Server..."
	uv run python -m canonical_multipass_mcp.server

# Run the server with debug output
debug: env
	@echo "Starting Canonical Multipass MCP Server in debug mode..."
	uv run python -m canonical_multipass_mcp.server --debug

# Run tests
test: dev
	@echo "Running tests..."
	uv run pytest tests/ -v

# Run linting
lint: dev
	@echo "Running flake8..."
	uv run flake8 canonical_multipass_mcp/ tests/
	@echo "Running mypy..."
	uv run mypy canonical_multipass_mcp/

# Format code
fmt: dev
	@echo "Formatting code with black..."
	uv run black canonical_multipass_mcp/ tests/

# Publish to PyPI
publish: env
	rm -rf dist
	uv build
	uv publish