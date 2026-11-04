# Synapse Layer — Python Basic Example

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Store and recall AI agent memories through the canonical MCP endpoint in under 30 seconds.

## What this does

This example connects to `https://forge.synapselayer.org/api/mcp` over JSON-RPC,
stores a memory with the `save_to_synapse` tool, and recalls it with the `recall`
tool. It demonstrates the core store/recall loop that gives AI agents persistent
memory across sessions and tools.

## Prerequisites

- Python 3.9+
- A Synapse Layer account and `sk_connect_` token ([get yours here](https://forge.synapselayer.org/dashboard/connect))

## Install

```bash
git clone https://github.com/SynapseLayer/synapse-layer-python-basic
cd synapse-layer-python-basic && pip install -r requirements.txt
cp .env.example .env  # edit with your token
```

## Run

```bash
python3 main.py
```

## Expected output

```
[store] Saving memory via MCP...
[store] Done. memory_id=6f1c...
[store] trust_quotient=0.716

[recall] Searching for user preferences via MCP...
  [0] content: The user prefers dark mode and communicates in Portuguese.
      trust_quotient: 0.716

[recall] 1 memories found.
```

`recall` requires a `reason` (10–200 chars) under the
`MEMORY_EXPORT_GOVERNANCE_V1` audit policy; the example includes one.

## Get your token

1. Go to [forge.synapselayer.org](https://forge.synapselayer.org)
2. Sign up or log in
3. Navigate to **Dashboard → Connect**
4. Generate a new `sk_connect_` token
5. Paste it in your `.env` file
