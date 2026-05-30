# Check palindrome recursively
def peli(arr,first,last):
    if first>=last:
        return arr
    else:
        arr[first],arr[last]=arr[last],arr[first]
        return peli(arr,first+1,last-1)
string = input("Enter Your Word: ")
arr = list(string)
first = 0
last = len(arr)-1
if(string=="".join(peli(arr,first,last))):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")