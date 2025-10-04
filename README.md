# MCPs: Sentiment Analysis & Pull Requests Agent

This repo tracks my first experiments with the Model Context Protocol (MCP) by building two small hands-on projects.

## Projects

- **MCP Sentiment Server/Client** (`sentiment_analysis_mcp/`): Gradio app that uses TextBlob for quick polarity/subjectivity checks and exposes itself as an MCP server and a Gradio MCP client that connects to said server.
- **PR Helper MCP Server** (`PRmcp/`): FastMCP server that inspects your repository changes and recommends pull-request templates so you can draft PR descriptions faster.

## Stack

Python · Gradio · TextBlob · smolagents · FastMCP

## Getting Started

1. `pip install -r requirements.txt`
2. Jump into a project directory and follow its README for launch details.

Both demos were built to understand how MCP servers expose tools, how a client negotiates available capabilities, and how agents can compose those tools into workflows.
