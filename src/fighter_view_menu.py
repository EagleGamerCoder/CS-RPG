class FighterViewMenu:
    def __init__(self):
        self.CurrentFighter = ""
        self.FighterFound = False

    # === LOCAL ===
    
    def attemptFileOpen(self):
        try:
            with open(self.CurrentFighter + ".txt", "r") as file:
                lines = file.readlines()
                self.FighterFound = True
                return {
                    "Strength" : int(lines[0].strip()),
                    "Agility" : int(lines[1].strip()),
                    "Intelligence" : int(lines[2].strip())
                }
                
        except FileNotFoundError:
            print(f"[ERROR] Fighter {self.CurrentFighter} not found!")
            return {}


    # === API ===

    def Open(self):
        print("===== VIEW FIGHTER =====")

        Stats = {}
        while not self.FighterFound:
            self.CurrentFighter = input("Enter fighter name to inspect: ")
            Stats = self.attemptFileOpen()

        print("========================")
        print(f"Fighter Profile: {self.CurrentFighter}")
        print(f"Strength: {Stats['Strength']}")
        print(f"Agility: {Stats['Agility']}")
        print(f"Intelligence: {Stats['Intelligence']}")
        print(f"Total Power: {Stats['Strength'] + Stats['Agility'] + Stats['Intelligence']}")
        print("========================")
        print()