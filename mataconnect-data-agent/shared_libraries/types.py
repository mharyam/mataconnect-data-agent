"""Shared types and data models for the mataconnect data agent."""

from typing import List
from pydantic import BaseModel, Field


class Community(BaseModel):
    """Represents a community or organization."""
    
    name: str = Field(..., description="Name of the community or organization")
    url: str = Field(..., description="URL of the community or organization")


class CommunityList(BaseModel):
    """List of communities returned by the agent."""
    
    communities: List[Community] = Field(..., description="List of communities found")


# JSON response configuration for Google ADK
json_response_config = {
    "response_mime_type": "application/json",
    "response_schema": CommunityList.model_json_schema()
} 