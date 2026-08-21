def main():

    l = 5
    w = int(input("What is the width? "))
    print("0" * w)
    print("0" * w)
    print("0" * w)
    print("0" * w)
    print("0" * w)

    p = (2 * l) + (2 * w)
    print("Perimeter:", p)

    a = (l * w)
    print("area:", a)

    d = (l ** 2 + w ** 2) ** 1/2
    print("Diagonal:", d)

if __name__ == "__main__":
    main()
