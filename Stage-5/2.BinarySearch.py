# Binary Search
def binary(arr,target,first,last):
    if(first>last):
        return -1
    mid = (first+last)//2
    if(target==arr[mid]):
        return mid
    elif(target>arr[mid]):
        return binary(arr,target,mid+1,last)
    else:
        return binary(arr,target,first,mid-1)
length = int(input("Enter Your Length of the Number of array: "))
arr = [int(input(f"Enter Your number at index_{i}: ")) for i in range(length)]
arr.sort()
target = int(input("Enter Your Target Number: "))
first = 0
last = length-1
print(f"Your Target Value at index: {binary(arr,target,first,last)}")
print(f"Your array: {arr}")