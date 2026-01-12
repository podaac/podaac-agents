"""StackTraceAnalysisAgent for analyzing and summarizing stack traces."""
import os
from pydantic import BaseModel
from strands.models import BedrockModel
from strands.models.ollama import OllamaModel
from strands.models.openai import OpenAIModel
from strands import Agent
from strands_tools import current_time


SYSTEM_PROMPT = """You are a StackTrace Analysis Agent, an expert at analyzing stack traces and providing clear, actionable error summary and possible solutions to fix the error.

Your role as a software engineer is to:
1. Receive a full stack trace as input
2. Provide a clear summary of what went wrong.  Label this as "Detailed Summary" so it can be identified in the output.
3. Also provide a short summary of the error in 10 words or less.  Label this as "Short Summary" so it can be identified in the output.
4. Suggest specific, actionable fixes/solutions.  If you are showing a list, be sure to put each row on a new line.  Label this as "Suggested Solution" so it can be identified in the output.
5. Use the current_time tool to add when the analysis was run.  Put in local Pacific time with timezone, and 12 hour format.  Be sure to include the date and time.

When analyzing stack traces:
- Focus on the most relevant error information
- Identify the specific line and function where the error occurred
- Look for common patterns (import errors, type errors, attribute errors, etc.)
- Provide concrete steps to fix the issue
- Suggest preventive measures if applicable

Always be concise but thorough in your analysis and recommendations.
And do not use a lot of words.  Keep it short and to the point.
"""


# Create a Bedrock model
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    #model_id="openai.gpt-oss-120b-1:0",
    #max_tokens=3000,
    temperature=0.0
)

# Create an Ollama model (local)
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="gpt-oss:20b",
    temperature=0.0
)

# Create an OpenAI-compatible model with OpenRouter
openrouter_model = OpenAIModel(
    client_args={
        "base_url": "https://openrouter.ai/api/v1",
        "api_key": os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY"),
    },
    model_id="nvidia/nemotron-3-nano-30b-a3b:free",
    params={
        "temperature": 0.0,
    }
)

class StackTraceInfo(BaseModel):
    detailed_summary: str
    short_summary: str
    suggested_solution: str
    analysis_run_time: str


# Create agent with the selected model and tools
# Choose which model to use by uncommenting the desired one:
stack_trace_agent = Agent(
    #model=ollama_model,
    #model=bedrock_model,
    model=openrouter_model,
    tools=[current_time],
    system_prompt=SYSTEM_PROMPT,
    #callback_handler=None,
    structured_output_model=StackTraceInfo
)
