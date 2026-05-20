#Basic Calculator
num1 = float(input("Enter your 1st number : "))
num2 = float(input("Enter your 2st number : "))
choice = int(input("for sum : 1, for multi: 2, for sub: 3, for div: 4 : "))
match choice:
    case 1:
        print(num1+num2)
    case 2:
        print(num1*num2)
    case 3:
        print(num1-num2)
    case 4:
        print(num1/num2)
    case _:
        print("Choice valid option")

# O(1)