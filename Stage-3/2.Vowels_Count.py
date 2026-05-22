# Count vowels in String
string = input("Enter Your Word: ").lower()
# method 1
# strList = list(string)
# Vow = []
# for i in strList:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         Vow.append(i)
# print(len(Vow))


# method 2
# count = 0
# for i in string:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         count +=1
# print(count)


# method 3
print(
    sum(
        [
            string.count("a"),
            string.count("e"),
            string.count("i"),
            string.count("o"),
            string.count("u"),
        ]
    )
)
