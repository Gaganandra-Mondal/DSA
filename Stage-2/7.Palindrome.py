# Palindrome number checker
number = 1212121
ori = number
rev = 0
while(number>0):
    digit = number%10
    number = number//10
    rev = rev*10+digit
if(rev==ori):
    print("Palidrome")
else:
    print("Not")