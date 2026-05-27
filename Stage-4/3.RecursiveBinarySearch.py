# Recursive Binary Search
def binary(arr,first,last,target):
    if(first>last):
        return -1
    else:
        mid = (first+last)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid]>target):
            return binary(arr,first,mid-1,target)
        else:
            return binary(arr,mid+1,last,target)
        
n = int(input("Enter Your array length: "))
arr = [int(input("Enter an item: ")) for _ in range(n)]
target = int(input("Enter Your target Number: "))
first = 0
last = len(arr)-1
print(f"Your Target is found at {binary(arr,first,last,target)} index")
print(arr)