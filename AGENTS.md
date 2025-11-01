# AGENTS.md

This file provides guidance to AI when working with the code in this repository.


## Project Overview

**podaac-agents** is a collection of AI-powered agents for the PODAAC project.

## Technology Stack

- **Language**: Python 3.10+
- **Package Manager**: poetry
- **CLI Framework**: Click with Rich for enhanced output
- **AI Integration**: Bedrock APIs and Strands Agents SDK.  Always look up documentation on how to use these properly.
- **Testing**: pytest with asyncio support

## Development Setup

### Initial Setup
```bash
# Install dependencies and create virtual environment
poetry install
```

### Common Commands

**Development:**
```bash
# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov

# Format code
poetry run black .

# Lint code
poetry run ruff check .

# Type checking
poetry run mypy src/

# Install pre-commit hooks
poetry run pre-commit install
```

**Building:**
```bash
# Build package
poetry build
```

**Running CLIs:**
```bash
# Run Bedrock-based CLI (requires AWS credentials)
poetry run python src/stack_trace_cli.py example_stacktrace_error.txt
```

## TODO List

[] Add tools

## License

Apache License 2.0

## Update Docs

Always update the docs after doing edits to reflect changes that should be included in this document
