# Find GCD using recursion
# def GCD(fN,sN):
#     if(fN<sN):
#         fN,sN=sN,fN
#     remain = fN%sN
#     if remain==0:
#         return sN
#     else:
#         return GCD(fN,remain)

# fN = int(input("Enter Your 1st Number: "))
# sN = int(input("Enter Your 2nd Number: "))
# print(f"Your GCD is : {GCD(fN,sN)}")


def GCD(last, SecLast):
    if last < SecLast:
        SecLast, last = last, SecLast
    remain = last % SecLast
    if remain == 0:
        return SecLast
    else:
        return GCD(SecLast, remain)


nums = int(input("Enter your limit: "))
arr = [int(input(f"Enter your {i+1}th number: ")) for i in range(nums)]
last = arr[0]
SecLast = arr[1]
remain = GCD(last, SecLast)
for i in range(2, len(arr)):
    remain = GCD(arr[i], remain)
print(remain)
