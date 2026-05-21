# D
# DE
# DEB
# DEBO
# DEBOT
# DEBOTT
# DEBOTTA
# DEBOTTAM
name = "Debottam".upper()
for i in range(len(name)):
    for j in range(i+1):
        print(name[j],end="")
    print("")


for i in range(len(name)):
    for j in range(len(name)-i):
        print(name[j],end="")
    print("")


arr = list(name)
for i in range(len(name)):
    print("".join(arr))
    arr.pop()