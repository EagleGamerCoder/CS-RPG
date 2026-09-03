import random

class FighterCreationMenu:
    def __init__(self):
        self.FighterName = ""
        self.Stats = {
            "Strength" : 0,
            "Agility" : 0,
            "Intelligence" : 0
        }

    # === LOCAL ===

    def generateFighterStats(self):
        self.Stats['Strength'] = random.randint(1, 20)
        self.Stats['Agility'] = random.randint(1, 20)
        self.Stats['Intelligence'] = random.randint(1, 20)

    def outputStats(self):
        print(f"Generated Stats -> Strength: {self.Stats['Strength']} | Agility: {self.Stats['Agility']} | Intelligence: {self.Stats['Intelligence']}")

    def saveFighter(self):
        with open(self.FighterName + ".txt", "w") as file:
            for i, v in self.Stats.items():
                file.write(str(v) + "\n")

    # === API ===

    def Open(self):
        print("===== FIGHTER CREATION =====")

        self.FighterName = input("Enter Fighter Name: ")
        self.generateFighterStats()
        self.outputStats()
        try:
            self.saveFighter()
        except:
            print("[ERROR] Fighter saving failed.")

        print(f"[SUCCESS] Fighter saved to {self.FighterName}.txt!")
        print("==============================")
        print()