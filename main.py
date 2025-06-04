# pip install openai-agents
# pip install python-dotenv

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Create the model using Gemini via OpenAI-compatible wrapper (⚠️ may not fully work)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

writer = Agent(
    name='Writer Agent',
    instructions="""You are a writer agent. Generate poems, stories, essays, emails, etc."""
)

response = Runner.run_sync(
    writer,
    input=' write a short poem , stories, essays and a email on Generative AI',
    run_config=config
)

print(response.final_output)