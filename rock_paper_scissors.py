from random import choice

class Game():
    
      # r = rock, p = paper, s = scissors
    OUTCOMES = {('s', 's'): 0, ('p', 'p'): 0, ('r', 'r'): 0, # tie
                ('r', 'p'): -1, ('p', 's'): -1, ('s', 'r'): -1, # human player loses
                ('p', 'r'): 1, ('s', 'p'): 1, ('r', 's'): 1} # human player wins
    
    def __init__(self,rounds):
        self.rounds = rounds
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()
    
    def play(self):
        for i in range(self.rounds):
            self.play_round()
            self.summarise_score()
    
    def play_round(self):
        hum_choice=self.human.choose()
        computer_choice = self.computer.choose()
        print(f'You: {hum_choice}   |   Computer: {computer_choice}')
        print(self.settle_round(hum_choice,computer_choice ))
        
    def settle_round(self, human_choice, comp_choice):
        outcome = self.OUTCOMES[(human_choice, comp_choice)]
        if outcome == 1:
            print('You won this round!\n')
            self.human.score += 1
        elif outcome == -1:
            print('You lost this round!\n')
            self.computer.score += 1
        else:
            print('This round is a tie\n')
            
    def summarise_score(self):
        print('[Game summary] Your points:', self.human.score, ' | Computer points:', self.computer.score)
        if self.human.score > self.computer.score:
            print ("You won.")
        elif self.human.score < self.computer.score:
            print ("Computer won.")
        else:
            print ("It was a tie.")


class Player():
    def __init__(self):
        self.score = 0
            
class HumanPlayer(Player):
    def choose(self):
        while True:
            user_choice = input('Rock, paper or scissors [r/p/s]? ')
            if user_choice in ['r', 'p', 's']:
                return user_choice

class ComputerPlayer(Player):
    def choose(self):
        return choice(['r', 'p', 's'])


if __name__ == "__main__":
        print('=== Rock Paper Scissors Game ===')
        while True:
            rounds = input('How many rounds would you like to play? ')  
            if rounds.isnumeric():
                Game(int(rounds)).play()
            break

 