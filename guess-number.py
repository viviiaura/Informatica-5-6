import random

def main():
    print("Hello! What's your name?")
    name = input("")
    print(f"Well, {name}, I am thinking of a number between 1 and 100.")

    number = random.randint(1,100)
    guess = 0 # Initialize

    while guess != number:
        guess = int(input("Take a guess. "))

        if guess > number:
           print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")

    print("Good job",name,"you guessed my number!")

if __name__ == "__main__":
    main()



