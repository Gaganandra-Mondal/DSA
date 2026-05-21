# Print all primes in range
import math
num = int(input(" Enter Your Range : "))
def Solution():
    primes = []
    for i in range(2,num+1):
        flag = True
        for j in range(2,math.ceil(i**0.5)):
            if(i%j==0):
                flag = False
                break
        if(flag):
            primes.append(i)
    return primes

print(Solution())