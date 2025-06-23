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

#### Production Deployment

```bash
# Deploy to Google Cloud
adk deploy mataconnect_data_agent --project your-gcp-project

# Deploy with custom configuration
adk deploy mataconnect_data_agent --config production.yaml
```

### ADK Best Practices

1. **Agent Design**: Keep agents focused on specific tasks
2. **Tool Integration**: Use tools for external operations (database, APIs)
3. **Error Handling**: Implement robust error handling in tools
4. **State Management**: Use ADK state for complex workflows
5. **Testing**: Test agents with various inputs and edge cases

### Troubleshooting ADK

#### Common Issues

1. **API Key Issues**:

   ```bash
   # Verify API key is set
   echo $GOOGLE_API_KEY

   # Test API key
   adk test-api-key
   ```

2. **Agent Not Starting**:

   ```bash
   # Check agent configuration
   adk validate mataconnect_data_agent

   # Run with verbose output
   adk run mataconnect_data_agent --verbose
   ```

3. **Tool Errors**:

   ```bash
   # Test individual tools
   adk test-tool save_enriched_community_to_db

   # Check tool configuration
   adk inspect-tools mataconnect_data_agent
   ```

#### Getting Help

- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK GitHub Repository](https://github.com/google/adk)
- [ADK Samples](https://github.com/google/adk-samples)

# MATA Connect Data Agent

A powerful data agent for enriching community information for the MATA Connect platform - the world's largest archive of women's communities.

## Features

- **Community Enrichment**: Automatically enriches basic community data with detailed information
- **Smart Web Scraping**: Extracts comprehensive information from community websites
- **LLM-Powered Analysis**: Uses advanced AI to analyze and categorize communities
- **Robust Database Integration**: Seamlessly integrates with SQLAlchemy database
- **Focus Area Intelligence**: Creates detailed focus areas for superior search matching

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## Quick Start

### Basic Usage

```bash
# Enrich all communities with URLs
python main.py --action enrich

# Enrich only first 5 communities (for testing)
python main.py --action enrich --limit 5

# Use specific OpenAI API key
python main.py --action enrich --openai-key your_key_here
```

### Python API Usage

```python
from mataconnect_data_agent.sub_agents.community_enricher.agent import enrich_communities

# Run enrichment
results = enrich_communities(
    openai_api_key="your_key",
    limit=10  # Optional: limit for testing
)

print(f"Processed: {results['total_processed']}")
print(f"Successful: {results['successful']}")
```

## How It Works

### 1. Data Loading

The agent loads communities from the `basic_communities` table that have URLs.

### 2. Web Scraping

For each community, the agent:

- Scrapes the main website
- Follows "About" links for detailed information
- Extracts contact information and social links
- Analyzes footer content for additional links

### 3. LLM Analysis

The scraped content is analyzed by GPT-4 to extract:

- **Description**: Clear, informative community description
- **Tags**: Generic, searchable tags (e.g., tech, finance, networking)
- **Focus Areas**: Detailed descriptions for search matching
- **Location**: Country and city information
- **Contact Info**: Email addresses and social links
- **Community Details**: Pricing, audience type, event types
- **Metrics**: Member counts, years active, etc.

### 4. Data Storage

Enriched data is saved to the `communities` table with comprehensive fields.

## Database Schema

### Enhanced CommunityDB Fields

| Field              | Type    | Description                       |
| ------------------ | ------- | --------------------------------- |
| `name`             | String  | Community name                    |
| `website`          | String  | Community website URL             |
| `description`      | Text    | AI-generated description          |
| `tags`             | JSON    | List of searchable tags           |
| `focus_areas`      | Text    | Detailed focus areas for matching |
| `country`          | String  | Primary country                   |
| `city`             | String  | Primary city                      |
| `language`         | String  | Primary language                  |
| `contact_email`    | String  | Contact email                     |
| `is_virtual`       | Boolean | Supports virtual events           |
| `social_links`     | JSON    | Social media links                |
| `community_info`   | JSON    | Community metrics                 |
| `pricing_model`    | String  | free/paid/freemium                |
| `topics_supported` | JSON    | List of topics                    |
| `audience_type`    | String  | Target audience                   |
| `event_types`      | JSON    | Types of events offered           |
| `year_founded`     | Integer | Year established                  |
| `verified`         | Boolean | Verification status               |
| `embedding`        | JSON    | Vector embedding for search       |

## Focus Areas - The Secret Sauce

Focus areas are critical for MATA Connect's success. They enable matching complex user queries like:

- "I just graduated and need job search support in the UK"
- "I'm going through a life crisis and need support"
- "I have 6 years experience in tech and feel stuck in my career"

### Example Focus Areas

**Good Focus Area:**

> "Supports women transitioning into tech careers, offering coding bootcamp guidance, interview preparation, and networking with established tech professionals. Particularly helpful for career changers and new graduates seeking entry-level positions in software engineering, data science, and product management."

**Why It Works:**

- Specific situations (transitioning, career change)
- Concrete support offered (guidance, preparation, networking)
- Target audience (career changers, new graduates)
- Specific domains (software engineering, data science)

## Configuration

### Environment Variables

| Variable         | Description                     | Required                |
| ---------------- | ------------------------------- | ----------------------- |
| `OPENAI_API_KEY` | OpenAI API key for LLM analysis | Yes                     |
| `DATABASE_URL`   | Database connection string      | No (defaults to SQLite) |

### Command Line Options

```bash
python main.py --help
```

Options:

- `--action`: Action to perform (default: enrich)
- `--limit`: Limit number of communities to process
- `--openai-key`: OpenAI API key (overrides env var)

## Error Handling

The agent includes robust error handling:

- **Network Errors**: Graceful handling of website timeouts
- **Parsing Errors**: Fallback when LLM responses can't be parsed
- **Database Errors**: Transaction rollback on save failures
- **Rate Limiting**: Built-in delays between requests

## Performance

- **Respectful Scraping**: 2-second delays between requests
- **Async Processing**: Efficient handling of multiple communities
- **Fallback Mode**: Works without OpenAI API (limited functionality)
- **Progress Tracking**: Real-time progress updates

## Architecture

```
mataconnect_data_agent/
├── shared_libraries/
│   ├── database.py          # Database models and utilities
│   └── types.py            # Shared type definitions
├── sub_agents/
│   └── community_enricher/
│       ├── agent.py        # Main enrichment agent
│       └── prompt.py       # LLM prompts and instructions
└── main.py                 # Entry point and CLI
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## License

This project is part of the MATA Connect ecosystem.
