from main_menu import MainMenu
from openai import OpenAI

OPENAI_CLIENT = None # Comment out this line when api key is inserted. Uncomment lines below
# os.environ['OPENAI_API_KEY'] = "Insert api key here" 
# OPENAI_CLIENT = OpenAI()

MAIN_MENU = MainMenu(OPENAI_CLIENT)

if __name__ == "__main__":

    MAIN_MENU.show_menu()




