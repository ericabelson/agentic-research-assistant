# Building an Scientific Research Team with Google's Agent Development Kit

This repository contains an example multi-agent system built using Google's [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) and powered by Google's Gemini models.

## Scope

The goal of this project is to demonstrate how a team of AI agents can automate parts of the scientific literature review process. Specifically, this system aims to:

1.  **Search** for relevant papers on bioRxiv based on a user's research topic.
2.  **Download** selected papers.
3.  **Read** the PDF content.
4.  **Extract** specific information, such as research methodologies.
5.  **Summarize** the findings for the user.

## Architecture

This system employs a multi-agent architecture orchestrated by ADK:

*   **Root Agent (`research_agent`):** Acts as the supervisor, coordinating the overall workflow.
*   **Search Agent (`search_agent`):** Specializes in searching articles in bioRxiv.
*   **Methodologies Agent (`methodologies_agent`):** Downloads papers, reads PDFs, and uses its LLM reasoning to extract methodologies from the text.

## Running the Agent

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ericabelson/agentic-research-assistant.git
    cd agentic-research-assistant
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set API Key:**
    *   Add your [Google AI Studio API key](https://aistudio.google.com/app/apikey) to the `.env` file:
        ```text title=".env"
        GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
        ```

4.  **Run with ADK:**
    *   **Web UI:**
        ```bash
        adk web
        ```
        Navigate to `http://localhost:8000` in your browser and select `research-agent`.
    *   **Command Line:**
        ```bash
        adk run research-agent
        ```
        This starts an interactive chat session in your terminal.

## Blog Post

Learn more about the design and implementation in our blog post: [[Link to Blog Post](https://medium.com/@esabelson/building-an-agentic-scientific-research-team-with-googles-agent-development-kit-4c4b024e29de)]

## Contributing

This is a sample project built with Agent Development Kit. To join the ADK open source movement, visit the [Google ADK Python repository](https://github.com/google/adk-python) to get started, talk with other agent builders, or make your contribution!
