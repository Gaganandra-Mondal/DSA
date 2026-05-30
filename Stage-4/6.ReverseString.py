# Reverse String Recursively


# string = "ABCDEF"
# arr = list(string)
# for i in range((len(arr))//2):
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
# print(arr)


def Reverse(arr,first,last):
    # if first==last:
    if first>=last:
        return arr
    else:
        arr[first],arr[last]=arr[last],arr[first]
        return Reverse(arr,first+1,last-1)
string = input("Enter Your String to Reverse: ")
arr = list(string)
first = 0
last = len(arr)-1
print("".join(Reverse(arr,first,last)))