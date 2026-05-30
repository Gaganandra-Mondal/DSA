# Power function using recursion
def Power(num,powr,flag):
    if powr<=1:
        return num
    elif flag==powr:
        return num
    else:
        return Power(num*num,powr-1,flag+1)
num = int(input("Input the Number: "))
powr = int(input("Input the Power: "))
flag = 0
print(f"{num} to the Power {powr} is: {Power(num,powr,flag)}")