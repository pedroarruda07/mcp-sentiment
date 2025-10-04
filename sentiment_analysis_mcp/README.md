# MCP Sentiment Analysis

Simple sentiment-analysis tool that doubles as my “hello world” for Model Context Protocol.

## What It Does

- wraps TextBlob sentiment scoring in a Gradio UI
- exposes the same function as an MCP tool/server (see `app.py`)
- includes a smolagents-powered client that talks to the running MCP server

## Run the Tool Server

```bash
pip install -r ../requirements.txt
python app.py
``` 

Gradio launches at http://127.0.0.1:7860 and registers an MCP server automatically.


## Talk to the Tool with an Agent
Set your Hugging Face token so the agent can call the hosted inference model:
```bash
export HF_TOKEN=hf_your_token
python client.py
``` 

The Gradio chat window proxies your questions through the smolagents CodeAgent, which discovers the MCP tool, invokes it, and streams back the JSON result.