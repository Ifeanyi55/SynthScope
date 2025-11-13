import gradio as gr
from synthscope import GoogleSearchImageGen

with gr.Blocks(
    theme=gr.themes.Base(primary_hue="teal", secondary_hue="amber").set(
        body_background_fill="*neutral_950",
        body_text_color="*neutral_200",
        background_fill_primary="*neutral_900",
        background_fill_secondary="*neutral_800",
        border_color_primary="*neutral_700",
        block_background_fill="*neutral_900",
        input_background_fill="*neutral_800",
        button_primary_background_fill="*primary_600",
        button_primary_background_fill_hover="*primary_700",
        button_secondary_background_fill="*neutral_700",
        button_secondary_background_fill_hover="*neutral_600"
    ),
    css="""
    footer {display: none !important;}
    body {
        background: linear-gradient(135deg, #0f172a 0%,
         #1e293b 50%, #334155 100%);
        color: #e2e8f0;
    }
               .audio-container {
                 padding: 10px;
                 border-radius: 8px;
                 background: rgba(30, 41, 59, 0.8);
                 border: 1px solid rgba(100, 116, 139, 0.3);
               }
               .audio-container audio {
                 width: 100%;
                 height: 60px;
                 border-radius: 6px;
                 background: #1e293b;
               }
               .output-section {
                 margin-bottom: 20px;
                 padding: 15px;
                 border-radius: 10px;
                 background: rgba(30, 41, 59, 0.6);
                 border: 1px solid rgba(100, 116, 139, 0.3);
                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
                 backdrop-filter: blur(10px);
               }
               .input-section {
                 padding: 20px;
                 background: rgba(15, 23, 42, 0.8);
                 border: 1px solid rgba(20, 184, 166, 0.3);
                 border-radius: 10px;
                 margin-top: 20px;
                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
               }
               .section-title {
                 color: #14b8a6;
                 font-weight: bold;
                 margin-bottom: 10px;
                 font-size: 1.1em;
                 text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);
               }
               h1 {
                 color: #14b8a6 !important;
                 text-shadow: 0 0 20px rgba(20, 184, 166, 0.4);
               }
               h4 {
                 color: #14b8a6 !important;
                 text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);
               }
               .gradio-container {
                 background: linear-gradient(135deg, #0f172a 0%,
                  #1e293b 50%, #334155 100%) !important;
               }
               """) as app:

    gr.HTML("""
    <div style='text-align:center;overflow:hidden;padding:20px;'>
    <h1 style='color:#14b8a6;text-shadow: 0 0 20px
     rgba(20, 184, 166, 0.4);'>SynthScope</h1><h1><p>🌐   🎨   🔊</p></h1>
     <p style='color:#94a3b8;'>Search, Visualize, Listen to Information</p>
     </div>
     """)
    gr.HTML("""
    <h4><p style='color:#14b8a6;text-shadow: 0 0 20px
     rgba(20, 184, 166, 0.4);text-align:center;'>
     SynthScope is an intelligent Web Search Agent that delivers results in text, image, and translated audio simultaneously.</p></h4>
      """)

    # Collapsible Sidebar for Controls
    with gr.Sidebar(elem_classes="input-section"):
        gr.HTML("<div class='section-title'>🔧 Search Configuration</div>")

        # Primary search input
        text_input = gr.Textbox(
            label="🔍 Search Query",
            placeholder="Enter your search topic...",
            lines=4,
            max_lines=6
        )

        # Configuration options
        language_input = gr.Dropdown(
            label="🌍 Output Language",
            choices=["English", "Spanish", "French", "German",
                     "Italian", "Japanese", "Tamil", "Arabic",
                     "Russian", "Portuguese", "Dutch", "Thai",
                     "Turkish", "Romanian", "Polish"],
            value="English",
            info="Language for text and audio"
        )

        voice_input = gr.Dropdown(
            label="🎙️ Voice Selection",
            choices=["Kore", "Zephyr", "Orus", "Fenrir",
                     "Charon", "Umbriel", "Schedar",
                     "Iapetus", "Puck", "Gacrux"],
            value="Kore",
            info="Voice for audio narration"
        )

        radio_input = gr.Radio(
            label="🎨 Visual Style",
            choices=["Comic", "Cartoon", "Disney",
                     "Anime", "Ghibli", "Victorian",
                     "Movie", "Star Wars", "Marvel",
                     "Van Gogh", "Picasso"],
            value="Comic",
            info="Artistic style for images"
        )

    # Main Body for Results and Actions
    # Action buttons at the top of main body
    with gr.Row():
        btn = gr.Button(
            "🚀 Run SynthScope",
            variant="primary",
            size="lg",
            scale=1
        )
        clear_btn = gr.ClearButton(
            [text_input, radio_input, language_input, voice_input],
            value="🗑️ Clear Inputs",
            variant="secondary",
            size="lg",
            scale=1
        )

    # Results Section
    with gr.Column(elem_classes="output-section"):
        gr.HTML("<div class='section-title'>📊 Generated Results</div>")
        gr.HTML("""
        <p style='color:#94a3b8; margin-bottom:15px; text-align:center;'>
        Your search results will appear below once processing is complete</p>
        """)

        # Text and Image side by side
        with gr.Row():
            with gr.Column(scale=1):
                gr.HTML("""
                <h4 style='color:#14b8a6; margin-bottom:10px;
                 text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>
                 📝 Text Summary</h4>
                 """)
                text_output = gr.Markdown(
                    value="*Search results will appear here...*",
                    height=350,
                    container=True
                )
            with gr.Column(scale=1):
                gr.HTML("""
                <h4 style='color:#14b8a6; margin-bottom:10px;
                 text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>
                 🎨 Generated Image</h4>
                 """)
                image_output = gr.Image(
                    label="",
                    show_label=False,
                    height=350,
                    container=True,
                    placeholder="Generated image will appear here..."
                )

        # Audio spanning full width below text and image
        gr.HTML("""
        <h4 style='color:#14b8a6; margin-bottom:10px;
         text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>
         🔊 Audio Narration</h4>
         """)
        audio_output = gr.Audio(
            label="",
            type="filepath",
            show_label=False,
            elem_classes="audio-container",
            interactive=False
        )
        gr.HTML("""
        <p style='color:#94a3b8; font-size:0.9em;
         text-align:center; margin-top:10px;'>
         Audio will be generated in your selected language and voice</p>
         """)

    # Footer with usage tips
    gr.HTML("""
    <div style='text-align:center; margin-top:30px; padding:20px;
     background:rgba(15, 23, 42, 0.5); border-radius:10px;
     border:1px solid rgba(20, 184, 166, 0.2);'>
        <h4 style='color:#14b8a6; margin-bottom:10px;'>
        💡 Tips for Best Results</h4>
        <p style='color:#94a3b8; font-size:0.9em; line-height:1.5;'>
            • Be specific in your search queries for more accurate results<br>
            • Try different visual styles to match your content theme<br>
            • Audio generation works best with shorter text summaries<br>
            • Processing may take 30-60 seconds depending on complexity
        </p>
    </div>
    """)

    # Event handlers
    btn.click(
        fn=GoogleSearchImageGen,
        inputs=[text_input, radio_input, voice_input, language_input],
        outputs=[text_output, image_output, audio_output],
        show_progress=True
    )

if __name__ == "__main__":
    app.launch(mcp_server=True)
