# Reverse a string
string = input("Enter Your Word to reverse: ")
strList = list(string)
rev = []
for i in range(len(strList)):
    temp = strList.pop()
    rev.append(temp)
print("".join(rev), f" is the reverse of {string}")

# print(string[::-1])