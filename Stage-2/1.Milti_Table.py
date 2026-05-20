# Print multiplication Table
num = int(input("Enter your number to get multiplication : "))
for i in range(1,11):
    multi = num*i
    print(f"{num}x{i} = {multi}")
# O(n)