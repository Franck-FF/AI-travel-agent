# AI Travel Planning Agent

An autonomous AI-powered travel planning application built with Python, Streamlit, LangGraph, Pydantic, and OpenAI.

This project takes a natural language travel request, extracts structured trip details, creates a day-by-day travel plan, researches activities, and generates a clean itinerary for the user.

---

## Project Overview

The AI Travel Planning Agent is designed to simulate a multi-agent travel assistant.

Instead of using one large prompt to generate an entire trip, the system separates the workflow into specialized agents:

1. **Intake Agent** — understands the user request and extracts structured travel information.
2. **Planning Agent** — creates a high-level day-by-day trip plan.
3. **Research Agent** — gathers place/activity information for each day.
4. **Writing Agent** — produces a polished travel itinerary using only the available research results.

The goal is to make the travel planning process more reliable, structured, and easier to improve over time.

---

## Features

* Natural language trip request input
* Structured trip extraction using Pydantic
* Multi-agent workflow using LangGraph
* Streamlit web interface
* Session state support so generated itineraries stay visible after reruns
* Markdown itinerary generation
* Modular architecture with separate agents, services, schemas, and graph logic
* Designed with hallucination prevention in mind by separating planning, research, and writing steps

---

## Tech Stack

* Python
* Streamlit
* LangGraph
* OpenAI API
* Pydantic
* python-dotenv
* Markdown

---

## Project Structure

```text
travel_ai_agent/
│
├── agents/
│   ├── intake_agent.py
│   ├── planning_agent.py
│   ├── research_agent.py
│   └── writing_agent.py
│
├── graph/
│   ├── state.py
│   └── travel_graph.py
│
├── schemas/
│   └── trip_schema.py
│
├── services/
│   ├── llm_service.py
│   ├── search_service.py
│   └── output_service.py
│
├── outputs/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## How It Works

The user enters a request such as:

```text
Plan a 5 day budget trip to Tokyo focused on anime and food.
```

The system then runs the request through the following workflow:

```text
User Request
   ↓
Intake Agent
   ↓
Planning Agent
   ↓
Research Agent
   ↓
Writing Agent
   ↓
Final Itinerary
```

Each step has a specific responsibility, making the system easier to debug, test, and expand.

---

## Example Output

```markdown
# Tokyo Travel Itinerary

## Day 1: Anime and Pop Culture in Akihabara
Explore Tokyo’s anime and gaming district with themed stores, arcades, and collectible shops.

## Day 2: Food Tour in Shibuya
Discover casual restaurants, street food, and popular local dining areas.

## Day 3: Traditional Tokyo in Asakusa
Visit cultural landmarks, local markets, and historic neighborhoods.
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/travel-ai-agent.git
cd travel-ai-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create your environment file

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

### 6. Run the Streamlit app

```bash
streamlit run app.py
```

---

## Environment Variables

This project uses a `.env` file for sensitive credentials.

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not commit your `.env` file to GitHub.

---

## Current Status

This is Version 1 of the project.

The current version includes:

* Working multi-agent architecture
* Streamlit user interface
* LangGraph workflow
* Structured data extraction
* Markdown itinerary generation

Future improvements may include:

* Real-time web search integration
* Verified opening hours and prices
* Map integration
* Hotel and restaurant recommendations
* PDF itinerary export
* User authentication
* Saved trip history

---

## Why This Project Matters

This project demonstrates practical AI engineering concepts, including:

* Multi-agent architecture
* Prompt engineering
* Structured outputs
* State-based workflows
* Modular Python design
* Streamlit app development
* LLM-powered automation

It is designed as a portfolio project to show how AI can be used to solve real-world planning problems with a clean and scalable architecture

Built by Franck Fossi 
