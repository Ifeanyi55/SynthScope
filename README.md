# **SynthScope**

Search, visualize, listen to information. Powered by the Gemini family of models.

![SynthScope](SynthScope.gif)

## **MCP**

SynthScope's MCP enables you to interact with the application through your favorite MCP clients, such as [Windsurf](https://windsurf.com/), [Claude desktop](https://claude.ai/download), [Warp](https://www.warp.dev/?utm_source=google&utm_medium=search&utm_campaign=segment_ai_dev_tools_other&utm_term=best%20ai%20for%20code&gad_source=1&gad_campaignid=22880547260&gclid=CjwKCAjwk7DFBhBAEiwAeYbJscPzuFVXx0mHUo9m0yeC7Os2cLJTq7hztbLrOxE89MuBcCi2kh9bDhoC25sQAvD_BwE), and [Cursor](https://cursor.com/). You can ask your client to search for a current piece of information on Google and return a translated audio of the search result. For the best result, be specific with the kind of response you want in your prompt. 

Here is an example prompt that is specific:

*"Help me search for the current price of gold, and return the search result as a French audio narration."*

```
{
  "mcpServers": {
    "SynthScope": {
      "url": "https://ifeanyi-synthscope.hf.space/gradio_api/mcp/sse"
    }
  }
}
```
Or
```
{
  "mcpServers": {
    "SynthScope": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://ifeanyi-synthscope.hf.space/gradio_api/mcp/sse",
        "--transport",
        "sse-only"
      ]
    }
  }
}
```
