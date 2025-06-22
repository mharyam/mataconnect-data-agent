"""Database tool for Google ADK agents to save community data."""

from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Dict, Any
from .database import BasicCommunityDB, get_db


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
