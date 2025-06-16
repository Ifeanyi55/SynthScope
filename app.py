import gradio as gr
from synthscope import GoogleSearchImageGen

with gr.Blocks(theme=gr.themes.Base(primary_hue="teal", secondary_hue="amber").set(
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
                 background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
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
                 background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%) !important;
               }
               """) as app:

    gr.HTML("<div style='text-align:center;overflow:hidden;padding:20px;'><h1 style='color:#14b8a6;text-shadow: 0 0 20px rgba(20, 184, 166, 0.4);'>🌐 SynthScope 👤</h1><p style='color:#94a3b8;'>Search, Visualize, and Listen to Information</p></div>")

    # Output Section
    with gr.Column(elem_classes="output-section"):
        gr.HTML("<div class='section-title'>📊 Search Results</div>")

        # Text and Image in a row
        with gr.Row():
            with gr.Column(scale=1):
                gr.HTML("<h4 style='color:#14b8a6; margin-bottom:10px; text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>📝 Text Summary</h4>")
                text_output = gr.Markdown(height=320, container=True)
            with gr.Column(scale=1):
                gr.HTML("<h4 style='color:#14b8a6; margin-bottom:10px; text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>🎨 Generated Image</h4>")
                image_output = gr.Image(label="", show_label=False, height=320, container=True)

        # Audio in its own row with proper spacing
        with gr.Row():
            with gr.Column():
                gr.HTML("<h4 style='color:#14b8a6; margin-bottom:10px; text-shadow: 0 0 10px rgba(20, 184, 166, 0.3);'>🔊 Audio Narration</h4>")
                audio_output = gr.Audio(
                    label="",
                    type="filepath",
                    show_label=False,
                    elem_classes="audio-container",
                    interactive=False
                )

    # Input Section
    with gr.Column(elem_classes="input-section"):
        gr.HTML("<div class='section-title'>🔧 Controls</div>")

        with gr.Row():
            with gr.Column(scale=2):
                text_input = gr.Textbox(
                    label="🔍 Search Query",
                    placeholder="Enter your search query here...",
                    lines=2
                )
            with gr.Column(scale=1):
                voice_input = gr.Dropdown(
                    label="👤Select Voice",
                    choices=["Kore", "Zephyr", "Orus", "Fenrir", "Charon", "Umbriel", "Schedar", "Iapetus", "Puck", "Gacrux"],
                    value="Kore"
                )
            with gr.Column(scale=1):
                language_input = gr.Dropdown(
                    label="👤Select Language",
                    choices=["English", "Spanish", "Thai", "German", "Italian", "Tamil", "Arabic", "French", "Romanian", "Turkish", "Dutch", "Polish", "Japanese", "Portuguese", "Russian"],
                    value="English"
                )
            with gr.Column(scale=1):
                radio_input = gr.Radio(
                    label="🎨 Image Style",
                    choices=["Comic", "Cartoon", "Disney", "Anime", "Ghibli", "Victorian", "Movie", "Star Wars", "Marvel", "Van Gogh", "Picasso"],
                    value="Comic"
                )

        with gr.Row():
            with gr.Column(scale=1):
                btn = gr.Button(
                    "🚀 Run SynthScope",
                    variant="primary",
                    size="lg"
                )
            with gr.Column(scale=1):
                clear_btn = gr.ClearButton(
                    [text_input, radio_input, language_input, voice_input, text_output, image_output, audio_output],
                    value="🗑️ Clear All",
                    variant="secondary",
                    size="lg"
                )

    # Event handlers
    btn.click(
        fn=GoogleSearchImageGen,
        inputs=[text_input, radio_input, voice_input, language_input],
        outputs=[text_output, image_output, audio_output],
        show_progress=True
    )

if __name__ == "__main__":
    app.launch()
