def main():

#easy
    # num = int(input("Type an integer number: "))

   # if num < 0:
       # print(num * -1)
  #  else:
       # print(num)
#medium
   # num1 = int(input("Give me a number: "))
   # num2 = int(input("Give me another number: "))
   # calc = input("Do you want to add, subtract, or multiply? ")

  #  if calc == "add":
    #    print(num1 + num2)
   # elif calc == "subtract":
    #    print(num1 - num2)
  #  elif calc == "multiply":
    #    print(num1 * num2)
  #  else:
   #     print("Blowing up computer..")
#hard
    oper = input("Enter your aritemetic operation: ")
    parts = oper.split( )

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    print(float(num1))
    print(operator)
    print(float(num2))

    if operator == "+":
        total = num1 + num2



if __name__ == "__main__":
    main()
