def main():
    transnum = 17800000000
    yrs = int(input("How many years into the future? "))

    transnum *= 2 ** (yrs / 2)

    print(transnum)


if __name__ == "__main__":
    main()
