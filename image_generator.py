import requests
from PIL import Image
from io import  BytesIO

class ImageGenerator:
    """
    A class for generating and handling images using OpenAI's DALL-E API.

    Attributes:
    - client (object): The client for interacting with the OpenAI API.
    - image_identifier (int): Identifier to keep track of generated images.

    Methods:
    - generate_image(prompt): Generates an image based on the given prompt using the DALL-E model.
    - convert_response_to_image(generated_response): Converts the API response to an image object.
    - save_image(image): Saves the generated image to a file in PNG format.
    - display_image(image): Displays the image.
    """

    def __init__(self, client):
        self.client = client
        self.image_identifier = 0

    def generate_image(self, prompt):
        image_response =  self.client.images.generate(
            model="dall-e-3",
            prompt=f"{prompt}",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        return image_response

    def convert_response_to_image(self, generated_response):
        image_url = generated_response.data[0].url
        image_data = requests.get(image_url)
        image_as_bytes = BytesIO(image_data.content)
        image = Image.open(image_as_bytes)
        return image

    def save_image(self, image):
        image.save(f'images/image_{self.image_identifier}.png')
        self.image_identifier += 1

    def display_image(self, image):
        image.show()