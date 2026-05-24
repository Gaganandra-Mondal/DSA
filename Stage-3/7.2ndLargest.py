# Find second largest element
arr = [3,432,24,4,53,545,334,54,453]
largest = arr[0]
sec_larg = arr[0]
for i in arr:
    if(largest<i):
        largest = i
    if(i>sec_larg and i<largest):
        sec_larg = i
    
print(f"Largest Value:{largest} and 2nd Largest is {sec_larg}")