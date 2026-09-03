from src.fighter_creation_menu import FighterCreationMenu
from src.fighter_view_menu import FighterViewMenu
from src.battle_service import BattleService

class MainMenu:
    def __init__(self):
        self.user_inp = 0

    # === LOCAL ===

    def openSubMenu(self):
        if self.user_inp == 0 or self.user_inp >= 5:
            print("[ERROR] Invalid Choice - Open Main Menu first.")
            return

        if self.user_inp == 1:
            fightercreationmenu = FighterCreationMenu()
            fightercreationmenu.Open()
        elif self.user_inp == 2:
            fighterviewmenu = FighterViewMenu()
            fighterviewmenu.Open()
        elif self.user_inp == 3:
            battleservice = BattleService()
            battleservice.Open()
        elif self.user_inp == 4:
            return

        self.Open()

    # === API ===

    def Open(self):
        print("===== MAIN MENU =====")
        print("1. Create Fighter")
        print("2. View Fighter")
        print("3. Battle")
        print("4. Quit")
        print("=======================")

        self.user_inp = 0
        while not (self.user_inp>=1 and self.user_inp<=4):
            try:
                self.user_inp = int(input("Enter option (1-4): "))
                if not (self.user_inp>=1 and self.user_inp<=4):
                    print("[ERROR] Please enter a valid number (1-4)!")
            except ValueError:
                self.user_inp = 0
                print("[ERROR] Please enter a number!")

        print("=======================")
        print()
        
        self.openSubMenu()