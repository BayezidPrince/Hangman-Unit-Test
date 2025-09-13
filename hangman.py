import random
import sys
import select

class Hangman:
    def __init__(self, level='basic'):
        self.dictionary_basic = ['python', 'hangman', 'testing', 'development', 'assignment']
        self.dictionary_intermediate = ['test driven development', 'unit testing tool', 'hangman game', 'python programming']
        if level == 'basic':
            self.puzzle = random.choice(self.dictionary_basic)
        else:
            self.puzzle = random.choice(self.dictionary_intermediate)
        self.masked = ''.join(['_' if c.isalpha() else c for c in self.puzzle])
        self.lives = 6
        self.guessed = set()

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            return self.masked
        self.guessed.add(letter)
        if letter in self.puzzle.lower():
            self.masked = ''.join([c if c.lower() == letter else m for c, m in zip(self.puzzle, self.masked)])
        else:
            self.lives -= 1
        return self.masked

    def is_won(self):
        return self.masked == self.puzzle

    def is_lost(self):
        return self.lives <= 0

def play_game():
    level = input("Choose level (basic/intermediate): ").strip().lower()
    game = Hangman(level)
    print(f"Puzzle: {game.masked}")
    print(f"Lives: {game.lives}")

    while not game.is_won() and not game.is_lost():
        print("You have 15 seconds to guess...")
        i, _, _ = select.select([sys.stdin], [], [], 15)
        if i:
            guess = sys.stdin.readline().strip().lower()
        else:
            print("Time's up!")
            game.lives -= 1
            print(f"Lives: {game.lives}")
            continue

        if guess == 'quit':
            print(f"Answer was: {game.puzzle}")
            break
        elif len(guess) == 1 and guess.isalpha():
            updated = game.guess(guess)
            print(f"Puzzle: {updated}")
            print(f"Lives: {game.lives}")
        else:
            print("Invalid input. Try again.")

    if game.is_won():
        print("You won!")
    elif game.is_lost():
        print("You lost! Answer was:", game.puzzle)

if __name__ == "__main__":
    play_game()