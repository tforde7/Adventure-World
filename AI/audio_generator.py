import subprocess

class AudioGenerator:
    """
    A class for generating and handling audio using OpenAI's text-to-speech API.

    Attributes:
    - client (object): The client for interacting with the OpenAI API.
    - AUDIO_FILE_PATH (str): Path to the generated audio file.

    Methods:
    - generate_audio(prompt): Generates audio based on the given prompt using the text-to-speech model.
    - save_audio(audio_response): Saves the generated audio to a file.
    - play_audio(): Plays the generated audio file using the default system audio player.
    """

    AUDIO_FILE_PATH = "audio.mp3"

    def __init__(self, client):
        self.client = client

    def generate_audio(self, prompt):
        audio_response = self.client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=f"{prompt}"
        )
        return audio_response

    def save_audio(self, audio_response):
        audio_file_path = AudioGenerator.AUDIO_FILE_PATH
        audio_response.stream_to_file(audio_file_path)

    def play_audio(self):
        audio_file_path = AudioGenerator.AUDIO_FILE_PATH
        subprocess.run(['afplay', audio_file_path])

