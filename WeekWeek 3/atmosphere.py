def main():

    layer = input("Descent atmosphere layer: ").lower()

    if layer == "exosphere":
        print("Your altitude level will be between 700 km and 10,000 km")
    elif layer == "thermosphere":
        print("Your altitude level will be between 85 km and 700 km")
    elif layer == "mesosphere":
        print("Your altitude level will be between 50 km and 85 km")
    elif layer == "stratosphere":
        print("Your altitude level will be between 12 km and 50 km")
    elif layer == "troposphere":
        print("Your altitude level will be between 0 km and 12 km")
    else:
        print("Error")

    exalt = float(input("Enter exact altitude "))

    if layer == "exosphere":
         exosphereTime = (exalt + 230.0 + 175.0 + 506.7 + 600.0)/2000
         print(f"Total descent time:", exosphereTime)
    elif layer == "thermosphere":
        thermosphereTime = (exalt + 230.0 + 175.0 + 506.7 + 600.0)/ 500
        print("Total descent time:",thermosphereTime)
    elif layer == "mesosphere":
        mesosphereTime = (exalt / 200)
    elif layer == "stratosphere":
        stratosphereTime = (exalt / 75)
    elif layer == "troposphere":
        troposphereTime = (exalt / 20)

    







if __name__ == "__main__":
    main()
