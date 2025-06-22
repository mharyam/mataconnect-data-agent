"""Google scraper sub-agent using Google ADK."""

from google.adk.agents import Agent
from google.adk.tools import google_search

from .prompts import get_google_scraper_instruction


google_scraper_agent = Agent(
    model="gemini-2.0-flash",
    name="google_scraper_agent",
    description="Searches for women communities and organizations using Google Search and returns structured data with names and URLs",
    instruction=get_google_scraper_instruction(),
    tools=[
        google_search,
    ],
    disallow_transfer_to_parent=False,
    disallow_transfer_to_peers=False,
)
