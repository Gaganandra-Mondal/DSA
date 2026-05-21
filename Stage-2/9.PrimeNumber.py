# Prime Number Check
num = int(input("Enter Your Number: "))

def Solution():
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
    
if(Solution()):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")