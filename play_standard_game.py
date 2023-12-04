from main_menu import MainMenu

MAIN_MENU = MainMenu()

def show_play_standard_game():
    print("----------------------------")
    print ("Coming Soon!")
    print("----------------------------")
    MAIN_MENU.show_menu()

def showIntro():
        print(
        """
        In a world torn by ancient prophecies, you awaken as a chosen hero in a small village.\n 
        The land of Etheria is fractured, its kingdoms scattered. A looming darkness threatens all. \n
        Your journey begins now, as you step forward to discover your destiny, wielding magic and courage\n 
        in a quest to restore balance and save Etheria from impending doom.\n\n

        The key to saving the land of Etheria lies in the power of the ancient Stone of Eternity.\n
        As you are about to embark on this dangerous quest to find the stone, you turn to say goodbye to \n
        your village one last time, fearing you may never return. You continue along \n
        the road and eventually you come to a fork in the road. \n
        """
    )

def chooseDirection():
      pass

def standardGameLoop():
      showIntro()
      while True:
        chooseDirection()
