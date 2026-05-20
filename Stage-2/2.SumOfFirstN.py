# Sum of first N numbers
nums = int(input("Enter your fisrt N numbers : "))
sum = 0
for i in range(nums+1):
    sum +=i
print(f"Your fisrt {nums} numbers of sum is : ",sum)
#print(nums*(nums+1)/2) # O(1)
# O(n)