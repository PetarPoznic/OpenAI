import streamlit as st
import openai
from pathlib import Path

# Function to generate speech
def generate_speech(api_key, text, voice, speed, format, filename):
    openai.api_key = api_key
    try:
        response = openai.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text,
            speed=speed,
            response_format=format
        )
        output_file = Path(__file__).parent / f"{filename}.{format}"
        with output_file.open('wb') as out:
            out.write(response.content)
        return output_file
    except Exception as e:
        return str(e)

# Streamlit App
def main():
    st.title('Text to Speech Generator')

    # Read API key from file
    api_key_path = Path(__file__).parent / 'openaiapikey.txt'
    if api_key_path.is_file():
        api_key = api_key_path.read_text().strip()
    else:
        st.error("API key file not found.")
        return

    # Input fields
    text = st.text_area("Enter Text to Convert to Speech")
    voice = st.selectbox("Select Voice", ('echo', 'alloy', 'fable', 'onyx', 'nova', 'shimmer'), index=0)
    format = st.selectbox("Select Output Format", ('mp3', 'opus', 'aac', 'flac'), index=0)
    speed = st.number_input("Select Speed", min_value=0.25, max_value=4.0, value=1.0, step=0.25)
    filename = st.text_input("Enter Filename for the Output Audio", 'speech')

    if st.button("Generate Speech"):
        if api_key and text:
            # Call the function to generate speech
            result = generate_speech(api_key, text, voice, speed, format, filename)
            if isinstance(result, Path):
                st.success(f"Speech successfully saved to {result}")
            else:
                st.error(result)
        else:
            st.error("Please fill all required fields.")

if __name__ == "__main__":
    main()
