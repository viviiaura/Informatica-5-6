def main():
    reciever = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Bowser", "Princess Peach", "Toadette", "Wario", "Waluigi", "Rosalina"]

    for letter in reciever:
        if letter != "Princess Peach":
            print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {letter},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {reciever[6]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")

if __name__ == "__main__":
    main()
