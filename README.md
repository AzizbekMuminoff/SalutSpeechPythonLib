
# SalutSpeech Python API Wrapper

This repository hosts the SalutSpeech Python API Wrapper, a convenient tool for integrating the SalutSpeech API's speech synthesis and recognition services into your Python applications.
The wrapper automatically manages access tokens and offers easier calls for speech synthesis and recognition with the SalutSpeech API.

## Getting Started
### Prerequisites

Ensure Python is installed on your machine. Additionally, you'll need the requests library, which can be installed via pip:
    
    pip install requests

### Installation

To get started with the SalutSpeech Python API Wrapper, clone this repository:


    git clone https://github.com/yourusername/salutspeech-python-wrapper.git
    cd salutspeech-python-wrapper

### Usage

Obtain an API key from SalutSpeech, then initialize the API client:
    
    from salutwrapper import SalutWrapper
    
    api_key = 'your_api_key_here'
    salut_speech = SalutWrapper(api_key)
    salute_speech.start()

#### Text-to-speech

    response = salut_speech.text_to_audio("Привет, как дела?", output_path)
    response = salut_speech.text_to_audio("Привет, как дела?", output_path, format="opus", output_format=".ogg", voice="ost_24000")
    

#### Recognizing Speech

    response = salut_speech.audio_to_text("path/to/your/audio/file.mp3")
    response = salut_speech.audio_to_text("path/to/your/audio/file.mp3", content_type="audio/ogg;codecs=opus;")


### For detailed API usage and parameters, see the SalutSpeech API Documentation.
