import random

def main():
    print("Welcome to the Be A Nerd app!")
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)

    answer = num1 + num2
    guess = 0

    while guess != answer:
        print(f"What is {num1} + {num2}?")
        guess = int(input("Your answer: "))

        if guess != answer:
            print("Incorrect.")
            
        elif guess == answer:
            print("Correct!")
            break

    print("streak!")

if __name__ == "__main__":
    main()
