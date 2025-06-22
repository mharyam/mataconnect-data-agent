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
