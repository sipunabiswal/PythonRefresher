import random
from Hangman_word import wordlist

#wordlist = ['python', 'java', 'kotlin', 'javascript']
def get_random_word():
    return random.choice(wordlist)


def display_placeholder(wordpicked):
    placeholder = ''
    for leters in wordpicked:
        placeholder = placeholder + '_'
    return placeholder

wordpicked = get_random_word()
pholder = display_placeholder(wordpicked)
print("Guess the word!", pholder)

print("The word has", len(wordpicked), "letters.")

def check_if_word_guessed(pholder):
    if '_' not in pholder:
        print("Congratulations! You've guessed the word:", wordpicked)
        return True
    return False

def check_letter_in_word(wordpicked, user_input,pholder):
        for i in range(len(wordpicked)):
            if wordpicked[i] == user_input:
                pholder = pholder[:i] + user_input + pholder[i+1:]
        print("Good guess!", pholder)
        return pholder


def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           -
        """,
        """
           -----
           
        """,
    ]
    return stages[tries]

tries = 5


while not check_if_word_guessed(pholder):
        user_input = input("Enter a letter: ").lower()
        if user_input not in wordpicked:
            print("Oops! That letter is not in the word.")
            print(display_hangman(tries))    
            tries -= 1
            if tries == 0:
                print("Game Over! The word was:", wordpicked)
                break            
        else:
            pholder = check_letter_in_word(wordpicked, user_input, pholder)


       
