# PR Helper MCP Server

FastMCP server that inspects local Git changes and suggests pull-request templates so an assistant (or you) can bootstrap PR descriptions quickly.

## Tools Exposed

- `analyze_file_changes`: wraps `git diff`/`git log` and returns JSON with stats + optional truncated diff.
- `get_pr_templates`: reads Markdown templates from `../templates/`.
- `suggest_template`: maps your change type (bug, feature, docs…) to a template and explains the pick.

## Setup

```bash
python server.py
```


## Typical Flow
1. Run python server.py.
2. Connect with an MCP-aware agent (e.g., Claude Desktop, smolagents).
3. Ask agent to recommend a PR description and let the magic happen.


## Notes
If you add new templates, update DEFAULT_TEMPLATES / TYPE_MAPPING in server.py.