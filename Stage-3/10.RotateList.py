# Rotate a list by K rotations
# arr = [7, 8, 9, 2, 3, 5, 10, 21, 13]
# k = 2
# n = len(arr) - 1
# for i in range(k):
#     arr[i], arr[n-i] = arr[n-i], arr[i]
# print(arr)



# Rotate a list by K positions
arr = [7, 8, 9, 2, 3, 5, 10, 21, 13]
k = 4
arr =  arr[k+1:] + arr[:k+1]
print(arr)
# 5 10 21 13 7 8 9 2 3