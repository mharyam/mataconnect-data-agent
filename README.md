# Mataconnect Data Agent

A Google ADK-based agent system for collecting and processing community data from various sources. This project demonstrates how to build a multi-agent system using Google's Agent Development Kit (ADK) for community data collection, field sourcing, and data cleaning.

## 🎯 Overview

The Mataconnect Data Agent is designed to:

- **Collect community data** from multiple sources
- **Source and validate fields** for data consistency
- **Clean and standardize** community information
- **Provide structured outputs** for further processing

## 🏗️ Architecture

This project follows the Google ADK architecture pattern with:

- **Root Agent**: `communities_data_agent` - Orchestrates the overall workflow
- **Sub-Agents**: Specialized agents for specific data collection tasks
- **Tools**: Custom functions for data processing and validation
- **Shared Libraries**: Common types and utilities
- **Prompts**: Centralized prompt management

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google ADK access
- Google GenAI API key

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

### 3. Run the Agent

```bash
python main.py
```

## 🔧 Running with Google ADK

### ADK Setup

This project is built using Google's Agent Development Kit (ADK). Here's how to set it up and run it:

#### 1. Install Google ADK

```bash
# Install the Google ADK CLI
pip install google-adk

# Verify installation
adk --version
```

#### 2. Configure ADK

```bash
# Set up your Google API key
export GOOGLE_API_KEY="your-google-genai-api-key"

# Or create a .env file
echo "GOOGLE_API_KEY=your-google-genai-api-key" > .env
```

#### 3. Run with ADK CLI

```bash
# Start the ADK server
adk run mataconnect_data_agent

# This will start a local server (usually at http://localhost:8000)
# You can then interact with your agent through the ADK interface
```

#### 4. Using ADK with Python

```python
from google.adk.runners import InMemoryRunner
from mataconnect_data_agent.agent import root_agent

# Initialize the runner
runner = InMemoryRunner(agent=root_agent)

# Run the agent
result = runner.run("enrich communities")

# Access the results
print(result)
```

#### 5. ADK Development Mode

For development and debugging:

```bash
# Run in development mode with hot reload
adk run mataconnect_data_agent --dev

# Run with verbose logging
adk run mataconnect_data_agent --verbose

# Run on a specific port
adk run mataconnect_data_agent --port 8080
```

#### 6. ADK Agent Testing

```bash
# Test your agent with a specific prompt
adk test mataconnect_data_agent "Find women's communities in London"

# Run tests with specific parameters
adk test mataconnect_data_agent --params '{"limit": 5}'
```

### ADK Project Structure

The project follows ADK conventions:

```
mataconnect_data_agent/
├── agent.py                    # Main agent definition
├── prompt.py                   # Agent prompts
├── sub_agents/                 # Sub-agent modules
│   ├── google_scraper/         # Google scraping agent
│   └── community_enricher/     # Community enrichment agent
├── shared_libraries/           # Shared utilities
│   ├── database.py            # Database models
│   ├── database_tool.py       # Database tools
│   └── types.py               # Type definitions
└── main.py                    # Entry point
```

### ADK Configuration

#### Agent Configuration

The main agent is configured in `agent.py`:

```python
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
```

#### Tool Configuration

Tools are defined in `shared_libraries/database_tool.py`:

```python
def save_enriched_community_to_db(enriched_data: dict) -> Dict[str, Any]:
    """Save enriched community data to the database."""
    # Implementation here
```

### ADK Workflows

#### 1. Community Data Collection

```bash
# Collect community data from Google
adk run mataconnect_data_agent "Search for women's tech communities in San Francisco"
```

#### 2. Community Enrichment

```bash
# Enrich existing communities
adk run mataconnect_data_agent "enrich communities"
```

#### 3. Database Operations

```bash
# Get communities to enrich
adk run mataconnect_data_agent "get communities to enrich"

# Save community data
adk run mataconnect_data_agent "save community data"
```

### ADK Debugging

#### Enable Debug Logging

```bash
# Set debug environment variable
export ADK_DEBUG=1

# Run with debug output
adk run mataconnect_data_agent --debug
```

#### View Agent Logs

```bash
# View agent execution logs
adk logs mataconnect_data_agent

# Follow logs in real-time
adk logs mataconnect_data_agent --follow
```

#### Agent State Inspection

```python
from google.adk.runners import InMemoryRunner
from mataconnect_data_agent.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

# Run with state inspection
with runner.run_with_state("enrich communities") as context:
    print(f"Agent state: {context.state}")
    print(f"Tool calls: {context.tool_calls}")
```

### ADK Deployment

#### Local Development

```bash
# Run locally for development
adk run mataconnect_data_agent --local
```

#### Getting Help

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [ADK Samples](https://github.com/google/adk-samples)

# MATA Connect Data Agent

A powerful data agent for enriching community information for the MATA Connect platform - the world's largest archive of women's communities.

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```
