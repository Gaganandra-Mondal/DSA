# Find largest element in list
arr = [3,432,24,4,53,545,453,334,54]
largest = arr[0]
for i in range(1,len(arr)):
    if(arr[i]>largest):
        largest = arr[i]
print(f"largets value is : {largest}")