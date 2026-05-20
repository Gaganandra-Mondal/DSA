# Convertion of Fah to Cel and Cel to Fah
Choice = int(input("Enter 1 for Fahrenheit -> Celsius or Enter 2 for Fahrenheit : "))
match Choice:
    case 1:
        F_Num = float(input("Enter your Fahrenheit number : "))
        Calculation_1 = F_Num*(9/5)+32
        print(f"Your Temp is : {Calculation_1} C")
    case 2:
        C_Num = float(input("Enter your Celsius number : "))
        Calculation_2 = (C_Num-32)*(5/9)
        print(f"Your Temp is : {Calculation_2} F")
    case _:
        print("Enter Valid Option")
# O(1)