import streamlit as st
import base64
import os
import asyncio
from google import genai
from dotenv import load_dotenv
load_dotenv()
from google.genai import types
import base64
import nest_asyncio

nest_asyncio.apply()  #Crucial: Apply nest_asyncio

# Replace with your actual API key or load from environment
GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")

async def generate_content_async(base64_string,user_input):
    """Asynchronous function to generate content using Gemini."""
    try:
        client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
        )
        model = "gemini-2.0-flash"
        contents = []

        contents.append(types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(mime_type="image/png", data=base64.b64decode(base64_string),),
                types.Part.from_text(
                    text=user_input
                ),
            ],
        ),)

        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_mime_type="text/plain",
            system_instruction=[
            types.Part.from_text(
                text="""Hey you are a friendly model helps user's by answering users questions on the images that they uploaded."""
            ),
        ]
        )

        response=client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )
        contents.append(types.Content(
                role="model",
                parts=[
                    types.Part.from_text(
                        text=response.text
                    ),
                ],
            ))
        print(response.text, end="")
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None


async def main():
    st.title("Gemini Image Processing Demo")

    uploaded_files = st.file_uploader(
        "Choose an image file", type=["png", "jpg", "jpeg"], accept_multiple_files=True
    )
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            base64_data = base64.b64encode(bytes_data)
            base64_string = base64_data.decode('utf-8')
            print("Image uploaded!!")

            st.image(bytes_data, caption=f"Uploaded Image: {uploaded_file.name}", use_container_width=True)
            title = st.text_input(label="Question",placeholder="Provide the question for image uploaded")
            # st.write("The current movie title is", title)
            print(title)

            if st.button(f"Explain Image: {uploaded_file.name}"):
                with st.spinner(f"Generating explanation for {uploaded_file.name}..."):
                    response_text = await generate_content_async(base64_string,title)
                    if response_text:
                        st.write("Explanation:")
                        st.write(response_text)
                    else:
                        st.error("Failed to generate explanation.")


if __name__ == "__main__":
    asyncio.run(main())