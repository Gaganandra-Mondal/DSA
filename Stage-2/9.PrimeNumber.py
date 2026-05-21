# Prime Number Check
import math
num = int(input("Enter Your Number: "))

def Solution():
    if(num<=1):
        return False
    for i in range(2,math.ceil(num**0.5)+1):
        if(num%i==0):
            return False
    return True
    
if(Solution()):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")