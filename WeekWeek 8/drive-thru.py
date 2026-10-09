def main():

    welcome()
    get_item()

def welcome():
    print("Welcome to Burgatory!")
    print("Here's the menu:")
    menu = ["Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie"]
    for i in range(len(menu)):
        print(f"{i + 1} {menu[i]}")

def get_item():
    choice = input("Which option would you like to order? (1-5): ")
    if choice == "1":
        print("🫴🍔")
    elif choice == "2":
        print("🫴🍟")
    elif choice == "3":
        print("🫴🥤")
    elif choice == "4":
        print("🫴🍦")
    elif choice == "5":
        print("🫴🍪")
    else:
        print("Please enter an option 1 to 5")

if __name__ == "__main__":
    main()
