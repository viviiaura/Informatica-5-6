import random
import time

def main():
    ideas = ["Cultural Background", "Lessons from failure", "Personal Challenges", "Debates on technology", "Education System", "Historical turning points", "Psycology concepts", "Literature"]
    rndm = random.choice(ideas)
    time.sleep(1)
    print("Cant think of ideas for your essay? ")
    time.sleep(1)
    help = input("Do you need help? ").lower().strip()

    if help == "yes":
        print("Okay I got your back! ")
    else:
        print("I'm gonna help you anyway ")

    time.sleep(1)
    print("Heres an idea that might help you out ")
    time.sleep(1)
    print(rndm)
    time.sleep(1)
    help2 = input("Does this help? ").lower().strip()
    while help2 != "yes":
        time.sleep(1)
        help3 = input("Want another idea? ").lower().strip()
        if help3 == "yes":
            time.sleep(1)
            print("Heres another idea! ")
            rndm2 = random.choice(ideas)
            print(rndm2)

        else:
            time.sleep(1)
            print("Glad I could Help! ")
            break


if __name__ == "__main__":
    main()
