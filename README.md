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

## MCP

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

## Contributing

Please read the [contributing guide](CONTRIBUTING.md) in order to see how you can contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.