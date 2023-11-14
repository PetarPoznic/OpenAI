# Text-to-Speech Python Script (tts.py)

## Overview
`tts.py` is a Python script that utilizes the OpenAI API to convert text into spoken audio. The script offers customizable settings for voice, speed, output format, and filename for the generated audio file.

## Features
- **Customizable Voice**: Choose from different voices including echo, alloy, fable, onyx, nova, and shimmer.
- **Adjustable Speed**: Set the speech speed from 0.25 to 4.0.
- **Output Format Selection**: Select from various output formats such as mp3, opus, aac, and flac.
- **Filename Option**: Specify a custom filename for the output.

## Installation

### Prerequisites
- Python 3.x
- OpenAI API key
- `openai` Python package

### Setup
1. Install the `openai` package using pip:
   ```bash
   pip install openai
   ```
2. Save your OpenAI API key in a file named `openaiapikey.txt` in the same directory as the script.

### Usage

#### Command Line Arguments
- `--speed <SPEED>`: Speed of the speech (default 1.0).
- `--voice <VOICE>`: Voice for the speech (default 'echo').
- `--format <FORMAT>`: Output format of the audio file (default 'mp3').
- `--filename <FILENAME>`: Filename for the output audio file (default 'speech').

#### Running the Script
Run the script from the command line, specifying the desired options. For example:
   ```bash
   python tts.py --voice alloy --speed 1.5 --format mp3 --filename my_speech
   ```

### Output
The script will generate an audio file in the specified format and with the specified filename in the script's directory.

### Notes
- Ensure the `text_to_speech.txt` file contains the text you wish to convert to speech.
- The `openaiapikey.txt` file should be present in the same directory as the script with your OpenAI API key.