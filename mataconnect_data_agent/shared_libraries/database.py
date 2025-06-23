"""Database models and utilities for the mataconnect data agent."""

import os
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    Boolean,
    JSON,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mataconnect_data.db")

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class CommunityDB(Base):
    """Database model for storing enriched community data."""

    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    website = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(JSON, nullable=True)  # List of generic tags
    focus_areas = Column(Text, nullable=True)  # Rich description for LLM matching
    country = Column(String(100), nullable=True)
    city = Column(String(100), nullable=True)
    language = Column(String(50), nullable=True)
    contact_email = Column(String(255), nullable=True)
    is_virtual = Column(Boolean, default=False)
    social_links = Column(JSON, nullable=True)  # Dict of social media links
    community_info = Column(JSON, nullable=True)  # Dict of community metrics
    pricing_model = Column(String(20), nullable=True)  # free, paid, freemium
    topics_supported = Column(JSON, nullable=True)  # List of topics
    audience_type = Column(String(100), nullable=True)  # students, professionals, etc.
    event_types = Column(JSON, nullable=True)  # List of event types
    year_founded = Column(Integer, nullable=True)
    verified = Column(Boolean, default=False)
    embedding = Column(JSON, nullable=True)  # Vector embedding for search
    data_source = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)


class BasicCommunityDB(Base):
    """Simple database model for storing basic community data."""

    __tablename__ = "basic_communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    url = Column(String(500), nullable=True)
    source = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class CommunityInfo(BaseModel):
    """Pydantic model for community information and URL."""

    name: str
    url: Optional[str] = None
    source: str


class EnrichedCommunity(BaseModel):
    """Pydantic model for enriched community data."""

    name: str
    website: str
    description: Optional[str] = None
    tags: Optional[list] = None
    focus_areas: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    language: Optional[str] = None
    contact_email: Optional[str] = None
    is_virtual: bool = False
    social_links: Optional[dict] = None
    community_info: Optional[dict] = None
    pricing_model: Optional[str] = None
    topics_supported: Optional[list] = None
    audience_type: Optional[str] = None
    event_types: Optional[list] = None
    year_founded: Optional[int] = None
    verified: bool = False
    embedding: Optional[list] = None
    data_source: Optional[str] = None


def get_db() -> Session:
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database tables."""
    Base.metadata.create_all(bind=engine)
