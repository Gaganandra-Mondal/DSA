# Factorial using Loop
num= int(input("Enter Your number for factorial : "))
fact = 1
for i in range(1,num+1):
    fact*=i
print(f"Your Factorial of {num} is = {fact}")