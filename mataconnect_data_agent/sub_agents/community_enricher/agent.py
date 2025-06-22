"""Community enricher sub-agent using Google ADK."""

from google.adk.agents import Agent
from google.adk.tools import google_search

from .prompts import get_community_enricher_instruction


community_enricher_agent = Agent(
    model="gemini-2.0-flash",
    name="community_enricher_agent",
    description="Enriches basic community data with detailed information by scraping websites and using LLM analysis",
    instruction=get_community_enricher_instruction(),
    tools=[
        google_search,
    ],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
)
