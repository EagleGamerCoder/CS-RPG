import random

class BattleService:
    def __init__(self):
        self.Fighter1Found = False
        self.Fighter2Found = False
        self.Fighter1 = ""
        self.Fighter2 = ""

        self.Fighter1Stats = {}
        self.Fighter2Stats = {}
        self.Scores = {
            "Fighter1" : 0,
            "Fighter2" : 0
        }

    # === LOCAL ===

    def attemptFileOpen(self, CurrentFighter):
        try:
            with open(CurrentFighter + ".txt", "r") as file:
                lines = file.readlines()
                return {
                    "Strength" : int(lines[0].strip()),
                    "Agility" : int(lines[1].strip()),
                    "Intelligence" : int(lines[2].strip())
                }, True
                
        except FileNotFoundError:
            print(f"[ERROR] Fighter {CurrentFighter} not found!")
            return {}

    def roundLogic(self, roundnum):
        roundnum+=1
        print()
        print(f"=== ROUND {roundnum} ===")
        category = ["Strength", "Agility", "Intelligence"][random.randint(0,2)]
        print(f"Category selected: {category}")
        print(f"{self.Fighter1} ({self.Fighter1Stats[category]}) vs {self.Fighter2} ({self.Fighter2Stats[category]})")
        if self.Fighter1Stats[category] > self.Fighter2Stats[category]: #f1 wins
            print(f"Point to {self.Fighter1}!")
            self.Scores["Fighter1"] += 1
        elif self.Fighter1Stats[category] < self.Fighter2Stats[category]: #f2 wins
            print(f"Point to {self.Fighter2}!")
            self.Scores["Fighter2"] += 1
        elif self.Fighter1Stats[category] == self.Fighter2Stats[category]: #draw no points awarded
            print(f"Draw! No points awarded!")

    def getTotalRounds(self):
        return self.Scores["Fighter1"] + self.Scores["Fighter2"]

    def calculateResult(self):
        if self.Scores["Fighter1"] > self.Scores["Fighter2"]:
            return {
                "Winner" : self.Fighter1,
                "WinnerScore" : self.Scores["Fighter1"],
                "LoserScore" : self.Scores["Fighter2"]
            }
        elif self.Scores["Fighter1"] < self.Scores["Fighter2"]:
            return {
                "Winner" : self.Fighter2,
                "WinnerScore" : self.Scores["Fighter2"],
                "LoserScore" : self.Scores["Fighter1"]
            }
        return {} # wont reach - for type checking
    
    # === API ===
    
    def Open(self):
        print("===== BATTLE =====")
        while not self.Fighter1Found:
            self.Fighter1 = input("Select Fighter 1: ")
            self.Fighter1Stats, self.Fighter1Found = self.attemptFileOpen(self.Fighter1)

        while not self.Fighter2Found:
            self.Fighter2 = input("Select Fighter 2: ")
            self.Fighter2Stats, self.Fighter2Found = self.attemptFileOpen(self.Fighter2)
        print("==================")

        while self.getTotalRounds() != 3:
            
            self.roundLogic(self.getTotalRounds() + 1)

        Result = self.calculateResult()
        print()
        print(f"FINAL RESULT: {Result["Winner"]} wins {Result["WinnerScore"]}-{Result["LoserScore"]}!")
        print()
        