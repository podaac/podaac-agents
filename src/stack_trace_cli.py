"""Simple Strands agent for testing using Bedrock."""

import asyncio
import argparse
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from podaac_agents.agents.stack_trace_agent import stack_trace_agent

console = Console()

async def main():
    """Run a simple Strands agent with Bedrock."""
    parser = argparse.ArgumentParser(
        description="AI-powered testing agent for analyzing stack traces"
    )
    parser.add_argument(
        "error_file",
        type=str,
        help="Path to the error file to analyze"
    )
    args = parser.parse_args()
    
    console.print("[bold blue]podaac-agents —– stack trace CLI[/bold blue]\n")
    
    error_file = Path(args.error_file)
    if not error_file.exists():
        console.print(f"[bold red]Error:[/bold red] File not found: {error_file}")
        return 1
    
    with open(error_file, "r") as f:
        error_content = f.read()
    
    with console.status("[green]Analyzing stack trace..."):
        response = stack_trace_agent(error_content)
    
    console.print(Panel(response.structured_output.detailed_summary, title="[green]Detailed Summary[/green]", border_style="green"))
    console.print(Panel(response.structured_output.short_summary, title="[yellow]Short Summary[/yellow]", border_style="yellow"))
    console.print(Panel(response.structured_output.suggested_solution, title="[cyan]Suggested Solution[/cyan]", border_style="cyan"))
    console.print(Panel(response.structured_output.analysis_run_time, title="[orange1]Analysis Run Time[/orange1]", border_style="orange1"))
    
    console.print(f"\n[dim]Tokens:[/dim] {response.metrics.accumulated_usage['totalTokens']:,} | "
                  f"[dim]Execution Time:[/dim] {sum(response.metrics.cycle_durations):.2f}s | "
                  f"[dim]Tools:[/dim] {', '.join(response.metrics.tool_metrics.keys()) or 'None'}")

if __name__ == "__main__":
    asyncio.run(main())
