from openai import OpenAI
import base64
from apikey import api_data

client = OpenAI(api_key=api_data)

def imgai(query):
    prompt = f"sir: {query}"

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="512x512"
    )

    # Get Base64 image data
    image_base64 = response.data[0].b64_json

    # Decode base64 and save file
    image_bytes = base64.b64decode(image_base64)

    with open("image.png", "wb") as f:
        f.write(image_bytes)

    print("Image saved as image.png")
    return "image.png"
