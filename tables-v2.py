def main():
    print("Welcome to the Times Table Quiz!")

    while True
        times_table = input("Enter a times table that you would like to be tested on: ").lower().strip()

        if times_table == "exit":
            break

        elif times_table in valid_nums:
            max_value = int(input("Enter maximum value for the times table: "))

            print(f"Here is the {times_table} times table")

            for x in range(1, max_value +1):
                answer = x * times_table
                print(f"{x} times {times_table} is {answer}")
        else:
            print("Invalid command.")
            
        max_value = int(input("Enter the maximum value for your times table: "))

if __name__ == "__main__":
    main()
