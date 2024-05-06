#SalutSpeech Python API Wrapper

This repository hosts the SalutSpeech Python API Wrapper, a convenient tool for integrating the SalutSpeech API's speech synthesis and recognition services into your Python applications.
Features

    Speech Synthesis: Easily convert text into spoken audio, with robust support for the Russian language.
    Speech Recognition: Convert spoken audio into text, facilitating effective human-computer interaction.
    Manages access tokens effectively: user don't have to update access tokens manually

Getting Started
Prerequisites

Ensure Python is installed on your machine. Additionally, you'll need the requests library, which can be installed via pip:
    
    pip install requests

Installation

To get started with the SalutSpeech Python API Wrapper, clone this repository:


    git clone https://github.com/yourusername/salutspeech-python-wrapper.git
    cd salutspeech-python-wrapper

Usage

Obtain an API key from SalutSpeech, then initialize the API client:

python
    
    from salutwrapper import SalutWrapper
    
    api_key = 'your_api_key_here'
    salut_speech = SalutWrapper(api_key)

Synthesizing Speech

Convert text to speech:

    response = salut_speech.synthesize_speech("Привет, как дела?", "ru")

Recognizing Speech

Transcribe audio to text:


    response = salut_speech.recognize_speech("path/to/your/audio/file.mp3", "ru")

Documentation

For detailed API usage and parameters, see the SalutSpeech API Documentation.
Contributing

Contributions are welcome! Please fork the repository, apply your changes, and submit a pull request.
License

This project is under the MIT License. For more details, see the LICENSE file.
