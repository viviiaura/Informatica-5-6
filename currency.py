def main():

    col = float(input("How much Columbian pesos?"))
    per = float(print("How much Peruvian soles? "))
    braz = float(print("How much Brazilian reais? "))


    cpp = (col * 0.0054)
    cpd = (col * 0.00032)
    print("pesos to MX:", cpp)
    print("pesos to USD:", cpd)

    perp = (per * 5.07)
    perd = (per * 0.30)
    print("soles to MX:", perp)




if __name__ == "__main__":
    main()
