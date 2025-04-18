import arxiv
import pymupdf
from google.adk.agents import Agent

# ==============================================================================
# Tools
# ==============================================================================

def search_arxiv(query: str):
    """Search for scientific publications on arXiv"""
    arxiv_client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=10,
    )
    results = arxiv_client.results(search)
    results = str([r for r in results])
    return results


def download_arxiv_paper(id: str):
    """Download a paper from arXiv"""
    paper = next(arxiv.Client().results(arxiv.Search(id_list=[id])))
    paper.download_pdf(dirpath="downloads/", filename="paper.pdf")
    return("Downloads complete!")


def load_pdf():
    """Load downloaded PDF file as text"""
    doc = pymupdf.open("downloads/paper.pdf")
    out = []
    for page in doc:
        text = page.get_text()
        out.append(text)
    print(out)
    return(" ".join(out))

# ==============================================================================
# Sub-agents
# ==============================================================================

search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-pro-preview-03-25",
    description=("Look up and answer questions about research on arXiv."),
    instruction=(
        """
        You are a helpful agent who can search papers on arXiv. Given input from
        the user, rewrite their query to search for papers on arXiv.
        """
    ),
    tools=[search_arxiv],
)

methodologies_agent = Agent(
    name="methodologies_agent",
    model="gemini-2.5-pro-preview-03-25",
    description=("""
                 You are a helpful agent who extracts research methodologies
                 used in scientific papers.
                 """),
    instruction=(
        """
        1. You'll receive a list of papers
        2. Download a random paper from the list
        3. Load a PDF of the paper and extract all methodologies used
        4. Repeat this process until you've downloaded and extracted 3 papers
        """
    ),
    tools=[download_arxiv_paper, load_pdf]
)

# ==============================================================================
# Root Agent
# ==============================================================================

root_agent = Agent(
    name="research_agent",
    model="gemini-2.5-pro-preview-03-25",
    description=(
        """
        Agent that coordinates literature searches, extracts research
        methodologies, and summarizes them.
        """
    ),
    instruction=(
        """
        1. Receive user input
        2. Coordinate a literature searches
        3. Coordinate research methodology extraction
        4. Summarize your findings and include a table of the methodologies used
        """
    ),
    sub_agents=[search_agent, methodologies_agent],
)
