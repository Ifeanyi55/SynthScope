# SynthScope

[![License](https://img.shields.io/github/license/Ifeanyi55/SynthScope)](./LICENSE)
![Build Status](https://github.com/Ifeanyi55/SynthScope/actions/workflows/ci.yml/badge.svg)
[![Stars](https://img.shields.io/github/stars/Ifeanyi55/SynthScope?style=social)](https://github.com/Ifeanyi55/SynthScope/stargazers)
[![Forks](https://img.shields.io/github/forks/Ifeanyi55/SynthScope?style=social)](https://github.com/Ifeanyi55/SynthScope/network/members)
[![Issues](https://img.shields.io/github/issues/Ifeanyi55/SynthScope)](https://github.com/Ifeanyi55/SynthScope/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Ifeanyi55/SynthScope)](https://github.com/Ifeanyi55/SynthScope/commits/main)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Ifeanyi55/SynthScope)

A web search agent that enables you to search, visualize, and listen to information. Powered by the Gemini family of models.

![SynthScope](SynthScope.gif)

## Table of Contents

- [Features](#features)
- [How it Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Local Deployment with Docker](#local-deployment-with-docker)
- [Usage](#usage)
- [MCP](#mcp)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Web Search:** Get concise, text-based answers to your questions.
- **Image Generation:** Visualize the search results with AI-generated images in various artistic styles.
- **Text-to-Speech:** Listen to the search results in multiple languages and voices.
- **Multi-language Support:** Get search results and audio in several languages.

## How it Works

SynthScope uses the Google Gemini API to perform the following steps:

1.  **Google Search:** It takes your query and uses Google Search to find the most relevant information.
2.  **Text Summarization:** The search results are summarized into a concise text.
3.  **Image Prompt Generation:** The summary is used to generate a prompt for the image generation model.
4.  **Image Generation:** An image is created based on the generated prompt and your chosen style.
5.  **Translation and TTS:** The text is translated into your chosen language and converted to speech using a text-to-speech model.

## Getting Started

### Prerequisites

- Python 3.9 or later
- A `GEMINI_API_KEY` environment variable. You can get your API key from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Ifeanyi55/SynthScope.git
    cd SynthScope
    ```
2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set your `GEMINI_API_KEY` environment variable:
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```
4.  Run the application:
    ```bash
    gradio app.py
    ```

## Local Deployment with Docker

You can also run SynthScope using Docker.

1.  Build the Docker image:
    ```bash
    docker build -t synthscope .
    ```
2.  Run the Docker container:
    ```bash
    docker run -p 7860:7860 -e GEMINI_API_KEY="YOUR_API_KEY" synthscope
    ```
    The application will be available at `http://localhost:7860`.

## Usage

1.  Enter your search query in the "Search Query" text box.
2.  Select the output language, voice, and visual style.
3.  Click the "Run SynthScope" button.
4.  The search results will be displayed as text, an image, and an audio file.

## MCP Integration

SynthScope supports the **Meta-Agent Communication Protocol (MCP)**, allowing it to be used as a tool by other agents and applications. This enables developers to programmatically interact with SynthScope's functionalities.

### Connecting to the MCP Server

The MCP server is exposed at the `/gradio_api/mcp/sse` endpoint of the application. You can connect to it using any MCP-compliant client.

There are two primary ways to configure your MCP client:

**1. Direct URL Configuration:**

If your client supports direct SSE URL connections, you can configure it with the following JSON object:

```json
{
  "mcpServers": {
    "SynthScope": {
      "url": "https://ifeanyi-synthscope.hf.space/gradio_api/mcp/sse"
    }
  }
}
```

**2. Command-Line Configuration:**

For clients that use a command-line interface, you can use the `mcp-remote` tool to establish a connection. This is particularly useful for local development or when you need more control over the connection parameters.

```json
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

### Example Usage

Once connected, you can send requests to SynthScope with a specific prompt. For optimal results, your prompt should be as descriptive as possible.

**Example Prompt:**

```
"Help me search for the current price of gold, and return the search result as a French audio narration."
```

## Contributing

Please read the [contributing guide](CONTRIBUTING.md) in order to see how you can contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.