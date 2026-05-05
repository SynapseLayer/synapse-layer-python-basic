# Synapse Layer — Python Basic Example

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Store and recall AI agent memories with semantic search in under 30 seconds.

## What this does

This example connects to the Synapse Layer API, stores a memory with semantic
content, and recalls it using a natural language query. It demonstrates the
core store/recall loop that gives your AI agents persistent memory across
sessions and tools.

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
[store] Saving memory...
[store] Done.

[recall] Searching for user preferences...
  [0] content: The user prefers dark mode and communicates in Portuguese.
      tq_score: 0.716

[recall] 1 memories found.
```

## Get your token

1. Go to [forge.synapselayer.org](https://forge.synapselayer.org)
2. Sign up or log in
3. Navigate to **Dashboard → Connect**
4. Generate a new `sk_connect_` token
5. Paste it in your `.env` file
