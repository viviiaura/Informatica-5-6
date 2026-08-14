
def main():
    # planet = input("planet:")

    # #separation
    # print("Hello", planet)

    # #concentation
    # print("Hello " + planet)

    # #fromatted strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hello", end=" ")
    # print(planet)


    name = input("What's your name?:").strip().title()
    color = input("Fav color?:").strip().lower()
    adj = input("Give me an adjective:").strip().lower()
    goal = input("What's a goal you would like to achieve?:").strip().lower()

    print("Hello", name +"!")
    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today {goal}." )

    print(f"AT DAWN THE SKY TURNED {color.strip().upper()}, AND THE AIR FELT {adj.strip().upper()}. I DECIDED TODAY {goal.strip().upper()}.")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided today {goal}.".upper())

if __name__ == "__main__":
    main()
