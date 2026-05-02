from mcp.server.fastmcp import FastMCP
from tavily  import TavilyClient
from dotenv import load_dotenv
import os
from typing import Any, List, Dict

load_dotenv()

mcp = FastMCP("mcp-server-http", host="0.0.0.0", port=23000)
tavily_api_key = os.environ["TAVILY_API_KEY"]
print(f"Tavily API Key: {tavily_api_key}")
web_search_client = TavilyClient(tavily_api_key)

@mcp.tool()
def get_employee_data(name: str) -> Dict:
    """
    Get information about an employee, including their salary and seniority.
    """
    return {
        "name": name,
        "salary": 75000,
        "seniority": 10
    }

@mcp.tool()
def web_search(query: str = "") -> List[Dict[str, Any]]:
    """
    Perform a web search using the Tavily API and return the results.
    """
    if not query.strip():
        return [
            {
                "error": "vous n'avez pas fourni de requete de recherche",
                "details": "svp fournir une requete de recherche valide pour obtenir des resultats",
            }
        ]

    try:
        resp = web_search_client.search(query=query)
        return resp.get("results", [])
    except Exception as exc:
        return [
            {
                "error": "Web search echec",
                "details": str(exc),
            }
        ]
    

if __name__ == "__main__":
    mcp.run(transport= "sse")
