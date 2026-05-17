# find the largest number in three
num1 = int(input("Enter your 1st number : "))
num2 = int(input("Enter your 2nd number : "))
num3 = int(input("Enter your 3rd number : "))
if(num1>num2>num3):
    print(f"{num1} is the largest number")
elif(num2>num1>num3):
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")