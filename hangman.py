from random import choice

# specify the file containing all the possible words, all on a new line in any order
dictionary_file = "dictionary.txt"


def import_dictionary(filename):
    dictionary = {length: [] for length in range(1, 13)}
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                length = len(word)
                if length <= 12:
                    dictionary[length].append(word)
    except Exception as e:
        print(f"Error occurred while importing dictionary: {e}")
    return dictionary


def print_dictionary(dictionary):
    for length, words in dictionary.items():
        print(f"Words of length {length}: {words}")


class Hangman:
    def __init__(self, word, lives=5):
        self.word = word.upper()
        self.letters_guessed = []
        self.hidden_letters = self.initialize_hidden_letters()
        self.lives = lives

    def initialize_hidden_letters(self):
        hidden = []
        for letter in self.word:
            if letter.isalpha():
                hidden.append("__ ")
            elif letter == "-":
                hidden.append("-")
        return hidden

    def guess_letter(self):
        new_letter = input("Please choose a new letter >\n").upper()
        if new_letter in self.letters_guessed:
            print("You have already chosen this letter.")
            return
        elif len(new_letter) > 1:
            print("Only guess one letter at a time!")
            return
        self.letters_guessed.append(new_letter)
        if new_letter in self.word:
            for index, letter in enumerate(self.word):
                if letter == new_letter:
                    self.hidden_letters[index] = new_letter
            print("You guessed right!")
        else:
            self.lives -= 1
            print("You guessed wrong, you lost one life.")

    def get_game_options(self):
        """
        ask the user to input game options such as a dictionary word size and a number of lives
        return: tuple of (wordsize, number of lives)
        """
        word_size = input(
            "Please choose a size of a word to be guessed [3 - 12, default any size]: \n")
        if word_size.isdigit() and int(word_size) in range(3, 13):
            word_size = int(word_size)
            print(f"The word size is set to {word_size}.")
        else:
            word_size = None
            print("A dictionary word of any size will be chosen.")

        num_lives = input(
            "Please choose a number of lives [1 - 10, default 5]: \n")
        if num_lives.isdigit() and int(num_lives) in range(1, 11):
            num_lives = int(num_lives)
            print(f"You have {num_lives} lives.")
        else:
            num_lives = 5
            print("You have 5 lives.")

        return word_size, num_lives

    def hang_game(self):
        self.word, self.lives = self.get_game_options()

        word_list = dictionary[self.word] if self.word is not None else []
        if not word_list:
            for size_words in dictionary.values():
                word_list.extend(size_words)
        self.word = choice(word_list).upper()
        self.hidden_letters = self.initialize_hidden_letters()

        while True:
            print("Letters chosen:", ", ".join(self.letters_guessed))
            print(" ".join(self.hidden_letters),
                  f" lives: {self.lives}", "0" * self.lives)
            self.guess_letter()

            if "__ " not in self.hidden_letters:
                print(f"Congratulations!!! You won! The word is {self.word}!")
                break
            elif self.lives == 0:
                print(f"You lost! The word is {self.word}!")
                break


if __name__ == "__main__":
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # print_dictionary(dictionary)

    print("Welcome to the Hangman Game!")
    while True:
        game = Hangman(word="")
        game.hang_game()

        play_again = input("Would you like to play again [Y/N]? ").upper()
        if play_again != "Y":
            print("Goodbye!")
            break
