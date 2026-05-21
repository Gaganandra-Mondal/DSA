# Armstrong number checker
num = int(input("Enter your number: "))
temp = num
n = len(str(num))
sum = 0

while (temp > 0):
    digit = temp % 10
    temp = temp// 10
    sum += digit ** n
    

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")