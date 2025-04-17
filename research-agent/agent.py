import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

import arxiv

def search_arxiv(query: str):
    '''Search for scientific publications on arXiv'''

    arxiv_client = arxiv.Client()

    search = arxiv.Search(
        query=query, max_results=10, sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = arxiv_client.results(search)
    results = str([r for r in results])

root_agent = Agent(
    name="research_agent",
    model="gemini-2.5-pro-preview-03-25",
    description=(
        "Agent to answer questions about research from BioArXiV."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about scientific research on BioArXiV."
    ),
    tools=[search_arxiv],
)
