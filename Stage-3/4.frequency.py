# Find frequency of characters
string = "the quick brown fox jumps over the lazy dog"
arr = []
for i in string:
    if i not in arr:
       arr.append(i)
for i in arr:
    print(f"{i}:{string.count(i)}")