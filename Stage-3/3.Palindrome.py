# Check palindrome string
string = input("Enter Your Word: ")
print(("not_palindrome", "palindrome")[string[::-1] == string])
