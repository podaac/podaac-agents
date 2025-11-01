# AGENTS.md

This file provides guidance to AI when working with the code in this repository.


## Project Overview

**podaac-agents** is a collection of AI-powered agents for the PODAAC project.

## Technology Stack

- **Language**: Python 3.12+
- **Package Manager**: uv (fast Python package installer and resolver)
- **CLI Framework**: Click with Rich for enhanced output
- **AI Integration**: Bedrock APIs and Strands Agents SDK.  Always look up documentation on how to use these properly.
- **Testing**: pytest with asyncio support

## Development Setup

### Prerequisites
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Initial Setup
```bash
# Install dependencies and create virtual environment
uv sync

# Install development dependencies
uv sync --extra dev

# Install the package in development mode
uv pip install -e .
```

### Common Commands

**Development:**
```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Format code
uv run black .

# Lint code
uv run ruff check .

# Type checking
uv run mypy src/

# Install pre-commit hooks
uv run pre-commit install
```

**Building:**
```bash
# Build package
uv build
```

**Running CLIs:**
```bash
# Run Bedrock-based CLI (requires AWS credentials)
uv run python src/stack_trace_cli.py
```

## TODO List

[] Add tools

## License

Apache License 2.0

## Update Docs

Always update the docs after doing edits to reflect changes that should be included in this document
