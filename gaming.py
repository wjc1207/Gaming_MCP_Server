from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
import os
import sys
import json

mcp = FastMCP("gaminglog")
GAMING_JSON_PATH = os.path.abspath("gaming.json")

def load_gaming_data() -> List[Dict[str, Any]]:
    """Load the gaming data from JSON file."""
    if not os.path.exists(GAMING_JSON_PATH):
        return []
    try:
        with open(GAMING_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        return [{"id": -1, "context": f"[ERROR] Failed to parse JSON: {e}"}]

@mcp.tool()
async def get_all_gaming_contexts() -> str:
    """
    Return all 嘉明 contexts from the JSON file.
    """
    entries = load_gaming_data()
    if not entries:
        return "No gaming entries found."

    summary = ""
    for entry in entries:
        summary += f"ID {entry.get('id')}: {entry.get('context')}\n"
    return summary.strip()

if __name__ == "__main__":
    print(f"[INFO] MCP Server starting in: {os.getcwd()}", file=sys.stderr)
    print(f"[INFO] Gaming log path: {GAMING_JSON_PATH}", file=sys.stderr)
    print(f"[INFO] File exists? {os.path.exists(GAMING_JSON_PATH)}", file=sys.stderr)
    mcp.run(transport="stdio")

