# Define the main function
# Create TXT file
# Make a list of the word we want to guess
# Open the TXT file in our code
# Define the TXT file
# Add a number of tries
# Create an if function if they got it wrong or right
# If they got it correct print the whole word
# Print the code
import random
def main():
    start_game()

def start_game():
    with open("words.txt") as hangman_words:
        words = hangman_words.read().splitlines()
        guess = random.choice(words)
        print(guess)

if __name__ == "__main__":
    main()
