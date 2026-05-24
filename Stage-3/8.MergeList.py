# Merge two List
arr1 = [3,4,34,45,45]
arr2 = [0,2,5,7,20,39,60]
# for i in arr2:
#     arr1.append(i)
arr1+=arr2
# selection sort
for j in range(len(arr1)):
    smallIndex = j
    for k in range(j+1, len(arr1)):
        if arr1[k] < arr1[smallIndex]:
            smallIndex = k
    temp = arr1[j]
    arr1[j] = arr1[smallIndex]
    arr1[smallIndex] = temp
print(arr1)
