from openai import OpenAI
from AI.audio_generator import AudioGenerator

class GeneratorFactory():
    # This key will be revoked after project is graded
    CLIENT = OpenAI(api_key="")

    @staticmethod
    def get_image_generator():
        pass

    @staticmethod
    def get_audio_generator():
        return AudioGenerator(GeneratorFactory.CLIENT)

    @staticmethod
    def get_text_genrator():
        pass


