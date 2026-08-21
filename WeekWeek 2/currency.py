def main():

    col = float(input("How much Columbian pesos? "))
    per = float(input("How much Peruvian soles? "))
    braz = float(input("How much Brazilian reais? "))

    usd = (col * 0.00032) + (per * 0.30) + (braz * 0.19)
    mxn = round(usd * 17.07, 2)

    print(f"USD: {round(usd, 2)}")
    print(f"MXN: {mxn}")



if __name__ == "__main__":
    main()
