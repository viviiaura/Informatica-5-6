
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


    name = input("What's your name?:")
    color = input("Fav color?:")
    adj = input("Give me an adjective:")
    goal = input("What's a goal you would like to achieve?:")

    print("Hello", name +"!")

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adj}. I decided \t today {goal}." )


if __name__ == "__main__":
    main()
