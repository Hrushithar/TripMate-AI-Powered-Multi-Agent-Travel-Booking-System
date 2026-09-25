# TripMate AI: Multi-Agent Travel Booking System

TripMate AI is an advanced, AI-powered multi-agent travel booking and planning system built using **LangGraph** and **FastAPI**. It leverages a coordinated team of specialized AI agents to generate comprehensive, budget-aware, and personalized travel itineraries, complete with human-in-the-loop approval.

## End-to-End Workflow & Functionality

1. **User Input & Guardrail Verification**:
   The user submits a travel request through the web frontend. The **Input Guardrail** intercepts the request to ensure it is a valid travel-related query. Irrelevant or harmful requests are blocked immediately with an explanation.
    
2. **Supervisor Routing**:
   Once validated, the **Supervisor Agent** analyzes the request to determine which specialist agents are needed. It extracts trip constraints (destination, origin, budget, duration) and dynamically routes the request to the required agents.
    
3. **Specialist Agents Execution**:
   Selected specialist agents run to gather specific data:
   * **Flight Agent**: Queries aviation APIs via the Model Context Protocol (MCP) to provide airport details, airlines, typical durations, and estimated airfares.
   * **Hotel Agent**: Uses Tavily web search (via MCP) to find the best hotels and accommodation advice.
   * **Weather Agent**: Uses weather MCP tools to fetch current conditions and forecasts for the destination, providing packing and seasonal guidance.
   * **Budget Agent**: Analyzes the collected flight, hotel, and weather data against the user's constraints to assess feasibility, highlight risks, and suggest money-saving tips.

4. **Draft Itinerary Generation**:
   The **Itinerary Agent** synthesizes all the specialist data into a practical, day-by-day draft travel plan. 

5. **Human-in-the-Loop (HITL) Review**:
   The workflow pauses and presents the draft itinerary to the user. The user can either:
   * **Approve** the draft as is.
   * **Reject** the draft and provide specific feedback for revision.

6. **Final Response Agent**:
   The **Final Agent** takes the draft and the user's feedback (if any) and generates a beautifully formatted, comprehensive final response containing the trip summary, flight and hotel suggestions, weather info, budget analysis, and the finalized day-by-day itinerary.

7. **State Management**:
   All conversational state and agent steps are persisted securely in a PostgreSQL database using LangGraph's `PostgresSaver` checkpointer, ensuring reliable multi-turn conversations and seamless pauses for human approval.

## Technology Stack

* **Backend Framework**: FastAPI
* **Agent Orchestration**: LangGraph, LangChain
* **LLM Provider**: Groq (e.g., `openai/gpt-oss-120b`)
* **State Persistence**: PostgreSQL
* **External Integrations (MCP)**: Aviationstack, Weather APIs, Tavily Search
* **Frontend**: HTML, CSS, JavaScript (via Jinja2 Templates)

## Getting Started

1. Clone the repository.
2. Set up your `.env` file with `DATABASE_URL`, `GROQ_API_KEY`, and other necessary API keys.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application: `python app.py`.
5. Access the web interface at `http://127.0.0.1:8000`.