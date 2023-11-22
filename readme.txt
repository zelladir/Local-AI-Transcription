Audio Transcription and Summarization Tool
Introduction
This tool is designed to transcribe audio files and provide summaries of the transcribed text. It supports various audio formats and uses OpenAI's Whisper API for transcription and GPT models for summarization.

Dependencies
Python 3.x
requests
pydub
python-dotenv
openai
FFmpeg (external dependency)
Installation
First, clone the repository or download the source code to your local machine.

Install Python Dependencies
Run the following command to install the required Python packages:

bash
Copy code
pip install requests pydub python-dotenv openai
Setting Up FFmpeg
FFmpeg is required for audio file conversion. Follow the instructions on the FFmpeg download page to install it on your system.

Environment Variables
The script uses an environment variable for the OpenAI API key. Set this up by creating a .env file in your project directory with the following content:

makefile
Copy code
OPENAI_API_KEY=your_api_key_here
Replace your_api_key_here with your actual OpenAI API key.

Usage
To run the script, navigate to the project directory and execute the Python script:

bash
Copy code
python transcription_script.py
The script will prompt you to select an audio file for transcription and summarization.

Notes
Ensure that your audio files are in a compatible format (e.g., .mp3, .wav, .ogg, .flac).
The script splits audio based on silence detection to ensure accurate transcription without cutting words.
Summaries are generated for each transcription segment and combined into a single output file.