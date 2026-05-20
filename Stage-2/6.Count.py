# Count digits in a number
number = 123.34
count = 0
while(number>0):
    digit = number%10
    number = number//10
    count+=1
print(count)
