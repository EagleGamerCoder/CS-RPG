import random

class CharacterCreationMenu:
    def __init__(self):
        self.CharacterName = ""
        self.Stats = {
            "Strength" : 0,
            "Agility" : 0,
            "Intelligence" : 0
        }

    # === LOCAL ===

    def generateCharacterStats(self):
        self.Stats['Strength'] = random.randint(1, 20)
        self.Stats['Agility'] = random.randint(1, 20)
        self.Stats['Intelligence'] = random.randint(1, 20)

    def outputStats(self):
        print(f"Generated Stats -> Strength: {self.Stats['Strength']} | Agility: {self.Stats['Agility']} | Intelligence: {self.Stats['Intelligence']}")

    def saveCharacter(self):
        with open(self.CharacterName + ".txt", "w") as file:
            for i, v in self.Stats.items():
                file.write(str(v) + "\n")

    # === API ===

    def Open(self):
        print("===== CHARACTER CREATION =====")

        self.CharacterName = input("Enter Fighter Name: ")
        self.generateCharacterStats()
        self.outputStats()
        try:
            self.saveCharacter()
        except:
            print("[ERROR] Character saving failed.")

        print(f"[SUCCESS] Character saved to {self.CharacterName}.txt!")
        print("==============================")
        print()