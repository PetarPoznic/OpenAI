# Text-to-Speech Streamlit Application

## Overview
This application, `tts_app.py`, is a Streamlit-based interface that allows users to convert text into speech using the OpenAI API. It provides options for selecting voice, speed, output format, and a custom filename for the generated audio file.

## Features
- **Text Input**: Enter the text you want to convert into speech.
- **Voice Selection**: Choose from a range of voices (echo, alloy, fable, onyx, nova, shimmer).
- **Speed Adjustment**: Set the speed of the speech (range from 0.25 to 4.0).
- **Output Format**: Choose the format of the output audio file (mp3, opus, aac, flac).
- **Filename Customization**: Specify a custom filename for the output audio file.

## Installation

### Prerequisites
- Python 3.x
- Streamlit
- OpenAI Python package

### Setting Up
1. **Clone or download this repository** to your local machine.
2. **Install the required packages** using the command:
   ```bash
   pip install -r requirements.txt
   ```
3. **Place your OpenAI API key in a file named** `openaiapikey.txt` in the same directory as the script.

### Running the Application
1. **Navigate to the directory** containing `tts_app.py`.
2. **Run the application** using Streamlit:
   ```bash
   streamlit run tts_app.py
   ```
3. The application should open in your default web browser.

### Usage
- Fill in the text area with the text you want to convert.
- Select your desired voice, speed, and output format.
- Enter a filename for your output audio file.
- The generated audio file will be saved in the same directory as the script.

### Notes
- Ensure the `openaiapikey.txt` file is present in the same directory as the script for the application to function correctly.
- The generated audio file will be saved in the same directory as the `tts_app.py` script.