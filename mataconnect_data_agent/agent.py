from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.google_scraper import google_scraper_agent
from .sub_agents.community_enricher import community_enricher_agent
from .shared_libraries.database_tool import (
    save_community_info_to_db,
    get_communities_to_enrich,
    save_enriched_community_to_db,
)
from . import prompt


communities_data_agent = LlmAgent(
    name="communities_data_agent",
    model="gemini-2.0-flash",
    description="Get communities data from different sources, source for fields, and clean them",
    tools=[
        AgentTool(agent=google_scraper_agent),
        AgentTool(agent=community_enricher_agent),
        save_community_info_to_db,
        get_communities_to_enrich,
        save_enriched_community_to_db,
    ],
    instruction=prompt.COMMUNITIES_DATA_AGENT_INSTRUCTION,
)

root_agent = communities_data_agent
