"""Synapse Layer — Python Basic Example
Store a memory and recall it with semantic search.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SYNAPSE_TOKEN", "")
BASE_URL = os.getenv("SYNAPSE_BASE_URL", "https://forge.synapselayer.org")

if not TOKEN or TOKEN == "sk_connect_xxx":
    print("ERROR: Set SYNAPSE_TOKEN in .env")
    print("Get yours at: https://forge.synapselayer.org/dashboard/connect")
    exit(1)

HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}
AGENT = "python-example"


def store_memory():
    """Store a memory via the Forge API."""
    print("[store] Saving memory...")
    resp = requests.post(f"{BASE_URL}/api/forge", headers=HEADERS, json={
        "action": "store",
        "agent": AGENT,
        "content": "The user prefers dark mode and communicates in Portuguese.",
        "intent": "user_preference",
    })
    resp.raise_for_status()
    print("[store] Done.\n")


def recall_memory():
    """Recall memories with a semantic query (cross-agent)."""
    print("[recall] Searching for user preferences...")
    resp = requests.post(f"{BASE_URL}/api/forge", headers=HEADERS, json={
        "action": "recall",
        "query": "What are the user preferences?",
        "topK": 5,
    })
    resp.raise_for_status()
    data = resp.json()
    memories = data.get("memories", [])
    if memories:
        for i, mem in enumerate(memories):
            print(f"  [{i}] content: {mem.get('content', 'N/A')}")
            print(f"      tq_score: {mem.get('trustQuotient', 'N/A')}")
        print(f"\n[recall] {len(memories)} memories found.")
    else:
        print("[recall] No memories found yet.")


if __name__ == "__main__":
    try:
        store_memory()
        recall_memory()
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code} — {e.response.text[:200]}")
    except Exception as e:
        print(f"Error: {e}")
