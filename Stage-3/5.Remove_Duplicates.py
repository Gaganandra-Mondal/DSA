# Remove Duplicates from string
string = "the quick brown fox jumps over the lazy dog"
letter = 0
s = ""
arr = []
for i in string:
    letter = string.count(i)
    if(letter==1 or i ==" "):
        arr.append(i)
# for j in arr:
#     s+=j
# print(s)
print("".join(arr))