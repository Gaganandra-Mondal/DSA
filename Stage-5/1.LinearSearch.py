# Linear search (Optional: Recursivly)
def Liner(arr,target,index):
    if (index>=len(arr)):
        return -1
    if(target == arr[index]):
        return index
    else:
        return Liner(arr,target,index+1)

arr = [1,4,2,7,5,3,6]
target = int(input("Enter Your Target: "))
index = 0
print(f"your number is at index {Liner(arr,target,index)}")