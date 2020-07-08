from random import randint

class Yahtzee: 
    _rolls = 3 
    _total = 5   
    def __init__(self):               
        self.dieSides = 6
        self.keptDice = []

    def __rollDice(self):
        rolledDice = randint(1, self.dieSides)
        return rolledDice

    def rollTotal(self):         
        if self.__class__._rolls <= 3 and self.__class__._rolls > 0:            
            rolledDie = [self.__rollDice() for die in range(self.__class__._total)] 
            self.__class__._rolls -= 1
            return rolledDie, self.__class__._rolls
        if self.__class__._rolls == 0:
            self.__class__._total = 5
            self.__class__._rolls = 3
            return "No more rolls", exit(0)

    def keptDie(self):        
        return self.keptDice

    def die_to_be_kept(self, dice):
        if len(self.keptDice) + len(dice) <= 5:
            self.__class__._total -= len(dice)
            for die in dice:            
                self.keptDice.append(int(die))
        else:
            print("Sorry, You can't add that that many dice")

    def gameEnd(self):
        answer = input("Are You Sure?: ")
        if "yes" in answer.lower():
            exit(0)
        if "no" in answer.lower():
            pass        


if __name__ in "__main__":
    game = Yahtzee()
    try:
        while True:
            question = input('Do you wanna roll?: ')
            if "yes" in question.lower():
                print(game.rollTotal())
                keep = input("What Dice Do You Want to Keep?: ")
                if "none" in keep.lower():
                    pass
                else:                    
                    game.die_to_be_kept(keep.split())
            elif "no" in question.lower():
                game.gameEnd()
            elif "keptdie" in question.lower():
                print(game.keptDie())
    except (EOFError, KeyboardInterrupt):
        exit(0)
    
    

    
        