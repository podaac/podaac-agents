"""Tests for the stack_trace_agent."""

import pytest
from pathlib import Path

from podaac_agents.agents.stack_trace_agent import stack_trace_agent
from strands.agent.agent_result import AgentResult


def test_stack_trace_agent_with_example_error():
    """Test stack_trace_agent with example_stacktrace_error.txt, similar to CLI usage."""
    # Read the example error file (same approach as cli.py)
    error_file = Path(__file__).parent.parent / "example_stacktrace_error.txt"
    
    if not error_file.exists():
        pytest.skip(f"Example error file not found: {error_file}")
    
    with open(error_file, "r") as f:
        error_content = f.read()
    
    # Pass the error content to the stack trace agent
    response = stack_trace_agent(error_content)
    
    print(f"Response: {response}")
    print(f"Response type: {type(response)}")

    # Verify we got a response and it's an AgentResult
    assert response is not None
    assert isinstance(response, AgentResult)
    assert response.structured_output is not None
    assert response.structured_output.detailed_summary is not None
    assert response.structured_output.short_summary is not None
    assert response.structured_output.suggested_solution is not None
    assert response.structured_output.analysis_run_time is not None