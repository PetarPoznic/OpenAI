import argparse
import openai
from pathlib import Path

# Set up argument parsing
parser = argparse.ArgumentParser(description='Generate speech from text with specified settings.')
parser.add_argument('--speed', type=float, default=1.0, help='Speed of the speech, range from 0.25 to 4.0. Default is 1.0.')
parser.add_argument('--voice', type=str, default='echo', choices=['echo', 'alloy', 'fable', 'onyx', 'nova', 'shimmer'], help='Voice for the speech. Choices are echo (default), alloy, fable, onyx, nova, and shimmer.')
parser.add_argument('--format', type=str, default='mp3', choices=['mp3', 'opus', 'aac', 'flac'], help='Output format of the audio file. Supported formats are mp3 (default), opus, aac, and flac.')
parser.add_argument('--filename', type=str, default='speech', help='Filename for the output audio file. Default is "speech".')

# Parse arguments from the command line
args = parser.parse_args()
speech_speed = args.speed
selected_voice = args.voice
output_format = args.format
output_filename = args.filename

# Check if the speed is within the allowed range
if not 0.25 <= speech_speed <= 4.0:
    raise ValueError('Speed must be between 0.25 and 4.0.')

# Define the path to your API key file, text file, and the output MP3 file
api_file_path = Path('api.txt')
text_file_path = Path('text_to_speech.txt')
speech_file_path = Path(f'{output_filename}.{output_format}')  # Use the selected filename and format

# Read the API key from the file
with api_file_path.open('r') as file:
    openai.api_key = file.read().strip()

# Read the text from the file
with text_file_path.open('r') as file:
    text_to_speak = file.read()

# Send the text to the OpenAI API to convert it into speech
try:
    response = openai.audio.speech.create(
        model="tts-1",
        voice=selected_voice,
        input=text_to_speak,
        speed=speech_speed,
        response_format=output_format
    )

    # Save the audio stream to the specified file
    with speech_file_path.open('wb') as out:
        out.write(response.content)

    print(f"Speech successfully saved to {speech_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
