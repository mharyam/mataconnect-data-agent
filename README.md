# Event Data Agent with Google ADK

A comprehensive event data collection and processing system built using Google's Agent Development Kit (ADK). This project follows the official Google ADK structure and patterns for building multi-agent systems.

## 🏗️ Architecture

The project follows the Google ADK structure with:

- **Root Agent**: Orchestrates the overall workflow
- **Sub-Agents**: Specialized agents for specific tasks
- **Tools**: Custom functions for data processing
- **Shared Libraries**: Common types and utilities
- **Prompts**: Centralized prompt management

## 📁 Project Structure

```
mataconnect-data-agent/
├── agents/
│   ├── __init__.py
│   ├── event_data_agent.py          # Main root agent
│   ├── prompts.py                   # Centralized prompts
│   ├── shared_libraries/
│   │   ├── __init__.py
│   │   └── types.py                 # Pydantic data models
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── scraper/
│   │   │   ├── __init__.py
│   │   │   └── agent.py             # Eventbrite scraper agent
│   │   └── cleaner/
│   │       ├── __init__.py
│   │       └── agent.py             # Data cleaning agent
│   └── tools/
│       ├── __init__.py
│       └── event_tools.py           # Custom tools
├── main.py                          # Main entry point
├── example_usage.py                 # Usage examples
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Main Agent

```bash
python main.py
```

### 3. Try Examples

```bash
python example_usage.py
```

## 🤖 Agents Overview

### Root Agent (`event_data_agent`)
- **Purpose**: Orchestrates the overall event data workflow
- **Capabilities**: Coordinates sub-agents for scraping and cleaning
- **Model**: Gemini 2.0 Flash

### Eventbrite Scraper Agent (`eventbrite_scraper_agent`)
- **Purpose**: Scrapes events from Eventbrite platform
- **Tools**: Google Search, custom Eventbrite search tool
- **Output**: Structured event data with location, organizer, tags, etc.

### Data Cleaner Agent (`data_cleaner_agent`)
- **Purpose**: Cleans and enriches event data
- **Tools**: Custom data cleaning tool
- **Output**: Standardized, enriched event data

## 📊 Data Models

The system uses Pydantic models for type safety:

- `Event`: Individual event with all details
- `EventLocation`: Location information
- `EventOrganizer`: Organizer information
- `EventList`: Collection of events
- `ScrapingResult`: Result of scraping operations

## 🛠️ Custom Tools

### Eventbrite Search Tool
- Searches for events on Eventbrite
- Parameters: query, country
- Returns structured event data

### Data Cleaning Tool
- Cleans and enriches event data
- Parameters: events list
- Returns cleaned events

### File Save Tool
- Saves events to JSON files
- Parameters: events, filename
- Returns save status

## 📝 Usage Examples

### Basic Usage

```python
from google.adk.runners import InMemoryRunner
from agents.event_data_agent import root_agent

# Initialize runner
runner = InMemoryRunner(agent=root_agent)

# Run agent
result = runner.run("Find technology events in London")

# Access results
if hasattr(result, 'events'):
    print(f"Found {len(result.events)} events")
```

### Using Individual Sub-Agents

```python
from agents.sub_agents.scraper import eventbrite_scraper_agent

# Use just the scraper
runner = InMemoryRunner(agent=eventbrite_scraper_agent)
result = runner.run("Find coding workshops in Birmingham")
```

## 🔧 Configuration

The agents use the following configuration:

- **Model**: Gemini 2.0 Flash
- **Temperature**: 0.1 (for consistent results)
- **Output Format**: JSON with structured schemas
- **Tools**: Google Search + custom tools

## 📋 Requirements

- Python 3.8+
- google-adk
- pydantic
- google-genai
- requests
- beautifulsoup4

## 🎯 Key Features

- ✅ **Google ADK Compliant**: Follows official ADK patterns
- ✅ **Multi-Agent Architecture**: Modular, scalable design
- ✅ **Type Safety**: Pydantic models for data validation
- ✅ **Structured Output**: Consistent JSON responses
- ✅ **Extensible**: Easy to add new agents and tools
- ✅ **Well Documented**: Clear structure and examples

## 🔄 Migration from Old Structure

The project has been restructured from the old custom agent classes to follow Google ADK patterns:

- **Before**: Custom `EventbriteScraper` and `CleanerAgent` classes
- **After**: Proper ADK `Agent` instances with tools and schemas

## 📚 Additional Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Samples](https://github.com/google/adk-samples)
- [Google GenAI Python SDK](https://github.com/google/generative-ai-python)
