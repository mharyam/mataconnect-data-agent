import sys
import os
from pathlib import Path
from absl import app
from dotenv import load_dotenv
import vertexai
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from mataconnect_data_agent.agent import root_agent  # noqa: E402


def main(argv: list[str]) -> None:
    load_dotenv()

    PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
    print(PROJECT, "PROJECTPROJECTPROJECTPROJECT")
    LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]
    STAGING_BUCKET = os.environ["GOOGLE_CLOUD_STORAGE_BUCKET"]

    if not PROJECT:
        print("Missing required environment variable: GOOGLE_CLOUD_PROJECT")
        return
    elif not LOCATION:
        print("Missing required environment variable: GOOGLE_CLOUD_LOCATION")
        return
    elif not STAGING_BUCKET:
        print("Missing required environment variable: GOOGLE_CLOUD_STORAGE_BUCKET")
        return

    print(f"PROJECT: {PROJECT}")
    print(f"LOCATION: {LOCATION}")
    print(f"STAGING_BUCKET: {STAGING_BUCKET}")

    vertexai.init(
        project=PROJECT,
        location=LOCATION,
        staging_bucket=f"gs://{STAGING_BUCKET}",
    )

    app = AdkApp(agent=root_agent, enable_tracing=False)

    remote_agent = agent_engines.create(
        app,
        requirements=[
            "google-adk (==0.5.0)",
            "google-cloud-aiplatform[adk,agent_engines] (==1.94.0)",
            "google-cloud-secret-manager",
            "deprecated",
            "pydantic>=2.5.0",
            "sqlalchemy>=2.0.0",
            "requests>=2.31.0",
            "beautifulsoup4>=4.12.0",
            "aiohttp>=3.9.0",
            "lxml>=4.9.0",
            "html5lib>=1.1",
            "soupsieve>=2.5.0",
        ],
    )

    print(f"Created remote agent: {remote_agent.resource_name}")
    print(
        f"Before testing, run the following: export AGENT_ENGINE_ID={remote_agent.resource_name}"
    )


if __name__ == "__main__":
    app.run(main)
