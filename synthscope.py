from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
from google.colab import userdata
from google.genai import types
from PIL import Image
from io import BytesIO


def GoogleSearchImageGen(prompt, image_style):
    # Define style-specific prompts
    style_prompts = {
        "Comic": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates a comic book-style image.",
        "Cartoon": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates a cartoon-style image.",
        "3D": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates a Pixar-style 3D image.",
        "Anime": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates an Anime-style image.",
        "Ghibli": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates a Ghibli-style image.",
        "Victorian": f"{prompt}. Convert the search result into a well-crafted text-to-image prompt that generates a Victorian-era image."
    }
    
    # Check if the image_style is supported
    if image_style in style_prompts:
      image_gen_prompt = style_prompts[image_style]
    
    # Initialize variables to avoid UnboundLocalError
    search_result = ""
    image = None
    
    try:
        # Get search result to be displayed to the user
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config=GenerateContentConfig(
                tools=[google_search_tool],
                response_modalities=["TEXT"],
            )
        )

        # Extract search result
        for each in response.candidates[0].content.parts:
            if each.text:
                search_result += each.text

        # Generate image prompt from search result
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

        # Generate image
        if prompt_image:  # Only generate image if we have a prompt
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=prompt_image,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )

            # Extract image from response
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    pass  # Handle text if needed
                elif part.inline_data is not None:
                    image = Image.open(BytesIO(part.inline_data.data))
                    break  # Exit loop once we find the image

    except Exception as e:
        print(f"Error occurred: {e}")
        # Return default values in case of error
        return search_result or "No search result available", None

    return search_result, image
