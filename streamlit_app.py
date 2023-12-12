import streamlit as st
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

def generate_image(prompt, api_key):
    client = OpenAI(api_key=api_key)

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url

        image_data = requests.get(image_url).content
  
        image = Image.open(BytesIO(image_data))

        return image

    except Exception as e:
        st.error(f"Error generating image: {str(e)}")


def main():
    st.title("OpenAI DALL-E Image Generator")

    api_key = st.text_input("Enter your OpenAI API key:", type="password")

    prompt = st.text_input("Enter a prompt for image generation:")

    if st.button("Generate Image"):
        if api_key:

            generated_image = generate_image(prompt, api_key)
            if generated_image:
                st.image(generated_image, caption="Generated Image", use_column_width=True)
        else:
            st.warning("Please enter your OpenAI API key.")

if __name__ == "__main__":
    main()
