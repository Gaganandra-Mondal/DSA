# number = input("Enter Your number for reverse : ")
# arr = list(number)
# arr.reverse()
# print("".join(arr))
number = int(input("Enter Your number for reverse : "))
rev = 0
while(number>0):
    digit = number%10
    number = number//10
    rev = rev*10+digit
print(rev)

# O(log10(n))