import gradio as gr
import os

from mcp import StdioServerParameters
from smolagents import InferenceClientModel, CodeAgent, ToolCollection, MCPClient

mcp_client = MCPClient(
    {"url": "https://pedroa07-mcp-sentiment.hf.space/gradio_api/mcp/sse", "transport": "sse",} # This is the MCP Client we created in the previous section
)
tools = mcp_client.get_tools()

model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
agent = CodeAgent(tools=[*tools], model=model)

demo = gr.ChatInterface(
    fn=lambda message, history: str(agent.run(message)),
    type="messages",
    examples=["Whats the sentiment of the sentence 'This is really good!'"],
    title="Agent with MCP Tool",
    description="This is a simple agent that uses a MCP sentiment-analysis tool to answer questions."
)

demo.launch()