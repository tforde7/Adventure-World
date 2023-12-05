import threading
from AI.generator_factory import GeneratorFactory
from AI.database.database import is_connected

class AIGame:
    
    def __init__(self, main_menu, player):
        self.main_menu = main_menu
        self.player = player
        self.image_generator = GeneratorFactory.get_image_generator()
        self.audio_generator = GeneratorFactory.get_audio_generator()
        self.text_generator = GeneratorFactory.get_text_genrator()
        
        self.text_generator.set_player(self.player)
    
    def play_game(self):
        if not is_connected:
            print("AI game not available right now.\nPlease try again later.")
            self.main_menu.show_menu()
        else:
            print("\nStarting AI game..\n")
            while True:
                text = self.text_generator.generate()

                generated_image_response = self.image_generator.generate_image(text)
                image = self.image_generator.convert_response_to_image(generated_image_response)
                self.image_generator.save_image(image)

                generated_audio_response = self.audio_generator.generate_audio(text)
                self.audio_generator.save_audio(generated_audio_response)

                image_thread = threading.Thread(target=self.image_generator.display_image, args=(image,))
                audio_thread = threading.Thread(target=self.audio_generator.play_audio)

                image_thread.start()
                audio_thread.start()

                image_thread.join()
                audio_thread.join()

                print(text)
                print("\n")

                if "The end." in text:
                    break

                human_input = input("Your reply: ")
                self.text_generator.set_human_input(human_input)
            
