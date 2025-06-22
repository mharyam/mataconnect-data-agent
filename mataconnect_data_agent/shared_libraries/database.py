"""Database models and utilities for the mataconnect data agent."""

import os
from datetime import datetime
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./mataconnect_data.db")

# Create engine and session
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class CommunityDB(Base):
    """Database model for storing community data."""
    
    __tablename__ = "communities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    url = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=True)
    contact_info = Column(Text, nullable=True)  # JSON string
    tags = Column(Text, nullable=True)  # JSON string
    source = Column(String(100), nullable=True)  # e.g., "google_scraper"
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
