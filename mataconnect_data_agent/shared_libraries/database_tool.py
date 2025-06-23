"""Database tool for Google ADK agents to save community data."""

import json
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Dict, Any, Optional
from .database import CommunityDB, BasicCommunityDB, get_db


def save_community_info_to_db(
    community_data: dict, source: str = "google_scraper"
) -> List[Dict[str, Any]]:
    """
    Save a list of community information and URLs to the basic database.
    """

    db = next(get_db())
    db_communities = []
    communities = community_data.get("communities", [])

    try:
        for i, community_info in enumerate(communities):
            name = community_info.get("name", "").strip()
            url = community_info.get("url", "")

            db_community = BasicCommunityDB(
                name=name,
                url=url if url else None,
                source=source,
                created_at=datetime.now(),
            )

            db.add(db_community)
            db_communities.append(db_community)
            print(f"Added community: {name}")

        # Commit all changes
        db.commit()
        print(f"Successfully saved {len(db_communities)} communities to database")

        # Refresh all communities to get their IDs
        for db_community in db_communities:
            db.refresh(db_community)

        # Convert to serializable format
        result = []
        for db_community in db_communities:
            result.append(
                {
                    "id": db_community.id,
                    "name": db_community.name,
                    "url": db_community.url,
                    "source": db_community.source,
                    "created_at": db_community.created_at.isoformat()
                    if db_community.created_at
                    else None,
                }
            )

        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Database error: {str(e)}")
        raise Exception(f"Failed to save communities: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"Unexpected error: {str(e)}")
        raise Exception(
            f"Failed to save communities: {str(e)}, community_data: {communities}, type: {type(communities)}"
        )


def get_communities_to_enrich(limit: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Fetch communities from the database that have URLs and need enrichment.
    """
    db = next(get_db())

    try:
        # Query communities that have URLs
        query = db.query(BasicCommunityDB).filter(
            BasicCommunityDB.url.isnot(None), BasicCommunityDB.url != ""
        )

        if limit:
            query = query.limit(limit)

        communities = query.all()

        # Convert to serializable format
        result = []
        for community in communities:
            result.append(
                {
                    "id": community.id,
                    "name": community.name,
                    "url": community.url,
                    "source": community.source,
                    "created_at": community.created_at.isoformat()
                    if community.created_at
                    else None,
                }
            )

        print(f"Found {len(result)} communities to enrich")
        return result

    except SQLAlchemyError as e:
        print(f"Database error: {str(e)}")
        raise Exception(f"Failed to fetch communities: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise Exception(f"Failed to fetch communities: {str(e)}")


def save_enriched_community_to_db(enriched_data: dict) -> Dict[str, Any]:
    """
    Save enriched community data to the database.
    """

    db = next(get_db())

    try:
        # Map 'url' to 'website' if present, since CommunityDB expects 'website'
        if "url" in enriched_data and "website" not in enriched_data:
            enriched_data["website"] = enriched_data.pop("url")

        # Map 'source' to 'data_source' if present, since CommunityDB expects 'data_source'
        if "source" in enriched_data and "data_source" not in enriched_data:
            enriched_data["data_source"] = enriched_data.pop("source")

        # Prepare data for database insertion with proper JSON serialization
        db_data = {}
        for key, value in enriched_data.items():
            if key in [
                "tags",
                "social_links",
                "community_info",
                "topics_supported",
                "event_types",
                "embedding",
            ]:
                # Serialize JSON fields properly
                if value is not None:
                    if isinstance(value, (list, dict)):
                        db_data[key] = json.dumps(value)
                    else:
                        db_data[key] = value
                else:
                    db_data[key] = None
            elif key == "focus_areas":
                # Handle focus_areas specially - it's a Text column but receives list data
                if value is not None:
                    if isinstance(value, list):
                        db_data[key] = ", ".join(value)
                    else:
                        db_data[key] = str(value)
                else:
                    db_data[key] = None
            else:
                db_data[key] = value

        # Check if community already exists
        existing = (
            db.query(CommunityDB)
            .filter(
                CommunityDB.name == db_data.get("name"),
                CommunityDB.website == db_data.get("website"),
            )
            .first()
        )

        if existing:
            print(f"Community {db_data.get('name')} already exists, updating...")
            # Update existing record
            for key, value in db_data.items():
                if key not in ["name", "website"]:  # Don't update primary identifiers
                    setattr(existing, key, value)
            existing.updated_at = datetime.utcnow()
            community_db = existing
        else:
            # Create new record
            community_db = CommunityDB(**db_data)
            community_db.created_at = datetime.utcnow()
            db.add(community_db)

        db.commit()
        print(f"Successfully saved enriched community: {db_data.get('name')}")

        # Return the saved data
        return {
            "id": community_db.id,
            "name": community_db.name,
            "website": community_db.website,
            "description": community_db.description,
            "tags": community_db.tags,
            "focus_areas": community_db.focus_areas,
            "country": community_db.country,
            "city": community_db.city,
            "language": community_db.language,
            "contact_email": community_db.contact_email,
            "is_virtual": community_db.is_virtual,
            "social_links": community_db.social_links,
            "community_info": community_db.community_info,
            "pricing_model": community_db.pricing_model,
            "topics_supported": community_db.topics_supported,
            "audience_type": community_db.audience_type,
            "event_types": community_db.event_types,
            "year_founded": community_db.year_founded,
            "verified": community_db.verified,
            "data_source": community_db.data_source,
            "created_at": community_db.created_at.isoformat()
            if community_db.created_at
            else None,
            "updated_at": community_db.updated_at.isoformat()
            if community_db.updated_at
            else None,
        }

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Database error: {str(e)}")
        raise Exception(f"Failed to save enriched community: {str(e)} {enriched_data}")
    except Exception as e:
        db.rollback()
        print(f"Unexpected error: {str(e)}")
        raise Exception(f"Failed to save enriched community: {str(e)} {enriched_data}")
