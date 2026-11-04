"""Synapse Layer — Python Basic Example

Store a memory and recall it through the canonical MCP endpoint.
"""
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SYNAPSE_TOKEN", "")
BASE_URL = os.getenv("SYNAPSE_BASE_URL", "https://forge.synapselayer.org").rstrip("/")
MCP_URL = f"{BASE_URL}/api/mcp"
AGENT = "python-example"

HEADERS = {
    "Content-Type": "application/json",
    "x-connect-token": TOKEN,
}

if not TOKEN or TOKEN == "sk_connect_xxx":
    print("ERROR: Set SYNAPSE_TOKEN in .env")
    print("Get yours at: https://forge.synapselayer.org/dashboard/connect")
    sys.exit(1)


def call_tool(name, arguments, request_id=1):
    """Call a Synapse Layer MCP tool over JSON-RPC and return its payload."""
    payload = {
        "jsonrpc": "2.0",
        "id": request_id,
        "method": "tools/call",
        "params": {"name": name, "arguments": arguments},
    }
    response = requests.post(MCP_URL, headers=HEADERS, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    if "error" in data:
        raise RuntimeError(data["error"].get("message", "MCP error"))

    result = data.get("result", {})
    content = result.get("content", [])
    text = content[0].get("text", "{}") if content else "{}"

    if result.get("isError"):
        raise RuntimeError(f"MCP tool '{name}' failed: {text[:200]}")

    structured = result.get("structuredContent")
    if isinstance(structured, dict):
        return structured

    # Fallback for servers that only return the text payload.
    payload, _ = json.JSONDecoder().raw_decode(text.lstrip())
    return payload


def store_memory():
    """Store a memory via the save_to_synapse MCP tool."""
    print("[store] Saving memory via MCP...")
    data = call_tool(
        "save_to_synapse",
        {
            "content": "The user prefers dark mode and communicates in Portuguese.",
            "agent_id": AGENT,
        },
        request_id=1,
    )
    print(f"[store] Done. memory_id={data.get('memory_id', 'n/a')}")
    print(f"[store] trust_quotient={data.get('trust_quotient', 'n/a')}\n")


def recall_memory():
    """Recall memories via the recall MCP tool."""
    print("[recall] Searching for user preferences via MCP...")
    data = call_tool(
        "recall",
        {
            "query": "What are the user preferences?",
            "limit": 5,
            "reason": "python-basic example: recall the stored preference",
        },
        request_id=2,
    )

    memories = data.get("memories", [])
    if memories:
        for index, memory in enumerate(memories):
            print(f"  [{index}] content: {memory.get('content', 'N/A')}")
            print(f"      trust_quotient: {memory.get('trust_quotient', 'N/A')}")
        print(f"\n[recall] {len(memories)} memories found.")
    else:
        print("[recall] No memories found yet.")


if __name__ == "__main__":
    try:
        store_memory()
        recall_memory()
    except requests.exceptions.HTTPError as exc:
        print(f"HTTP error: {exc.response.status_code} - {exc.response.text[:200]}")
        sys.exit(1)
    except (RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)
