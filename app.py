import gradio as gr
from synthscope import GoogleSearchImageGen

with gr.Blocks(theme=gr.themes.Default(primary_hue="teal", secondary_hue="amber"),
               css="footer {display: none !important;}") as app:
    gr.HTML("<div style='text-align:center;overflow:hidden;'><h2>&#127760; SynthScope &#127912;</h2></div>")
    
    with gr.Column():
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("<h4>Google Search Result</h4>")
                text_output = gr.Markdown(height=300)
            with gr.Column(scale=1):
                gr.Markdown("<h4>Search Result Image</h4>")
                image_output = gr.Image(label="", show_label=False,height=300)

        with gr.Column():
            with gr.Row():
                text_input = gr.Textbox(label="Query Field", placeholder="Type in your search query")
                radio_input = gr.Radio(label="Select Search Result Image Style", choices=["Comic", "Cartoon", "3D", "Anime", "Ghibli", "Victorian"]) 

            with gr.Row():          
                btn = gr.Button("Run SynthScope")
                clear_btn = gr.ClearButton([text_input, radio_input, text_output, image_output], value="Clear")

    btn.click(fn=GoogleSearchImageGen, inputs=[text_input, radio_input], outputs=[text_output, image_output])

if __name__ == "__main__":
    app.launch()