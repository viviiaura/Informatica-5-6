def main():
    tasks = [] #empty list

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)

        command = input("What do you want to do? (add,complete, exit): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "complete":
            comp_task = input("Which task did you complete?: ")
            tasks.remove(comp_task)
        elif command == "exit":
            print("Byebye!")
            break


if __name__ == "__main__":
    main()
