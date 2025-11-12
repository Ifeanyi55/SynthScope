from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from google.genai import types
from PIL import Image
from io import BytesIO
import wave
import os

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

google_search_tool = Tool(
    google_search=GoogleSearch()
)

model_id = "gemini-2.0-flash"


def GoogleSearchImageGen(prompt, image_style, voices, language):
    """
    Returns Google Search results as translated text, audio, and image
    Args:
        prompt: A natural language query for Google Search
        image_style: A list of different styles for the generated image
        voice: A list of different voices for the generated audio
        language: A list of different languages for the generated text
        and audio
    Returns:
        Text, image, audio.
    """
    def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm)

    # define audio output voice
    select_voice = {
        "Kore": "Kore",
        "Zephyr": "Zephyr",
        "Orus": "Orus",
        "Fenrir": "Fenrir",
        "Charon": "Charon",
        "Umbriel": "Umbriel",
        "Schedar": "Schedar",
        "Iapetus": "Iapetus",
        "Puck": "Puck",
        "Gacrux": "Gacrux"
    }

    try:
        # get search result to be displayed to the user
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=GenerateContentConfig(
                tools=[google_search_tool],
                response_modalities=["TEXT"],
            )
        )

        # initialize variables to avoid UnboundLocalError
        search_result = ""
        image = None

        # extract search result
        for each in response.candidates[0].content.parts:
            if each.text:
                search_result += each.text

        # define style-specific prompts
        style_prompts = {
            "Comic": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a comic book-style image.",
            "Cartoon": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a cartoon-style image.",
            "Disney": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Disney-style image.",
            "Anime": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates an Anime-style image.",
            "Ghibli": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Ghibli-style image.",
            "Victorian": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Victorian-era image.",
            "Movie": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Movie-style image.",
            "Star Wars": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Star Wars-style image.",
            "Marvel": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Marvel-style image.",
            "Van Gogh": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Van Gogh-style image.",
            "Picasso": f"Convert the {search_result} into a well-crafted text-to-image prompt that generates a Picasso-style image"
        }

        # check if the image_style is supported
        if image_style in style_prompts:
            image_gen_prompt = style_prompts[image_style]
        else:
            return "Invalid image style", None, None

        # define translation options
        translation_prompt = {
            "English": f"Read out the {search_result}",
            "Spanish": f"Translate {search_result} into Spanish. Return only the translated text.",
            "French": f"Translate {search_result} into French. Return only the translated text.",
            "German": f"Translate {search_result} into German. Return only the translated text.",
            "Italian": f"Translate {search_result} into Italian. Return only the translated text.",
            "Japanese": f"Translate {search_result} into Japanese. Return only the translated text.",
            "Tamil": f"Translate {search_result} into Tamil. Return only the translated text.",
            "Arabic": f"Translate {search_result} into Arabic. Return only the translated text.",
            "Russian": f"Translate {search_result} into Russian. Return only the translated text.",
            "Portuguese": f"Translate {search_result} Portuguese. Return only the translated text.",
            "Dutch": f"Translate {search_result} into Dutch. Return only the translated text.",
            "Thai": f"Translate {search_result} into Thai. Return only the translated text.",
            "Turkish": f"Translate {search_result} into Turkish. Return only the translated text.",
            "Romanian": f"Translate {search_result} into Romanian. Return only the translated text.",
            "Polish": f"Translate {search_result} into Romanian. Return only the translated text."
        }

        # updated search result
        trans_resp = client.models.generate_content(
            model=model_id,
            contents=translation_prompt[language]
        )

        # generate audio from search result
        audio_resp = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=trans_resp.text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=select_voice[voices],
                        )
                    )
                ),
            )
        )

        data = audio_resp.candidates[0].content.parts[0].inline_data.data

        audio_output_file = "out.wav"
        wave_file(audio_output_file, data)

        # generate image prompt from search result
        output = client.models.generate_content(
            model=model_id,
            contents=image_gen_prompt,
            config=GenerateContentConfig(
                tools=[google_search_tool],
                response_modalities=["TEXT"],
            )
        )

        prompt_image = ""
        for single in output.candidates[0].content.parts:
            if single.text:
                prompt_image += single.text

        # generate image
        if prompt_image:
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=prompt_image,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )

            # extract image from response
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    pass
                elif part.inline_data is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    break

    except Exception as e:
        print(f"Error occurred: {e}")
        # return default values in case of error
        return trans_resp.text or "No search result available", None, None

    return trans_resp.text, image, audio_output_file
