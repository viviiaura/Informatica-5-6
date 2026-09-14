def main():
    pets = ["cat", "dog", "bird"]
    pets.append("horse")
    print(pets)
    pets.insert(0,"horse")
    print(pets)
    numbers = [10, 2, 5, 3, 4, 8, 7]
    numbers.sort()
    print(numbers)
    numbers.sort(reverse = True)
    print(numbers)

    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))

if __name__ == "__main__":
    main()
