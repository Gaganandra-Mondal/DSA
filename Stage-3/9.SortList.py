# Sort List Manually
arr = [3,1,9,10,5,2,7,3,1,2,5,7,10]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if(arr[min_index]>arr[j]):
            min_index = j
    # temp = arr[i]
    # arr[i] = arr[min_index]
    # arr[min_index]=temp
    if i!=min_index:
        arr[i],arr[min_index] = arr[min_index],arr[i]
print(arr)