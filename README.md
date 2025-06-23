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

## 🤖 Agents Overview

### Root Agent: `communities_data_agent`

- **Purpose**: Orchestrates community data collection workflow
- **Model**: Gemini 2.0 Flash
- **Capabilities**:
  - Coordinates sub-agents for data collection
  - Manages data validation and cleaning
  - Provides structured community data output

### Sub-Agent: `google_scraper_agent`

- **Purpose**: Scrapes community data from Google search results
- **Tools**: Google Search integration
- **Output**: Structured community information with metadata

## 📝 Usage Examples

### Basic Usage

```python
from google.adk.runners import InMemoryRunner
from mataconnect_data_agent.agent import root_agent

# Initialize runner
runner = InMemoryRunner(agent=root_agent)

# Run agent to collect community data
result = runner.run("Find technology communities in San Francisco")

# Access results
print(f"Found {len(result.communities)} communities")
```

### Using Individual Sub-Agents

```python
from mataconnect_data_agent.sub_agents.google_scraper import google_scraper_agent

# Use just the scraper agent
runner = InMemoryRunner(agent=google_scraper_agent)
result = runner.run("Search for developer communities in London")
```

## 🔧 Configuration

### Agent Configuration

- **Model**: Gemini 2.0 Flash
- **Temperature**: Optimized for consistent data collection
- **Output Format**: Structured JSON with community data schemas
- **Tools**: Google Search + custom validation tools

### Environment Variables

```bash
GOOGLE_API_KEY=your-google-genai-api-key
```

## 🎯 Key Features

- ✅ **Google ADK Compliant**: Follows official ADK patterns and best practices
- ✅ **Multi-Agent Architecture**: Modular, scalable design for different data sources
- ✅ **Type Safety**: Pydantic models for data validation and consistency
- ✅ **Structured Output**: Consistent JSON responses with defined schemas
- ✅ **Extensible**: Easy to add new data sources and processing agents
- ✅ **Well Documented**: Clear structure and comprehensive examples

## 📚 Additional Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Samples Repository](https://github.com/google/adk-samples)
- [Google GenAI Python SDK](https://github.com/google/generative-ai-python)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

**Note**: This project is built using Google's Agent Development Kit (ADK) and follows the patterns established in the [ADK samples repository](https://github.com/google/adk-samples/tree/main/python/agents/brand-search-optimization).

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
