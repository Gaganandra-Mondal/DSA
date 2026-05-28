# Recursive Binary Search
def binary(arr,first,last,target):
    if(first>last):
        return -1
    else:
        mid = (first+last)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            return binary(arr,first,mid-1,target)
        else:
            return binary(arr,last,mid+1,target)
length = int(input("Enter Your array length: "))
arr = [int(input(f"Enter {i}th Element: "))for i in range(length)]
target = int(input("Enter your target value= "))
first = 0
last = len(arr)-1
print(f"Your Target value found: {binary(arr,first,last,target)}")
print(arr)