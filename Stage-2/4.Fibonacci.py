# Fibonacci Sequence..
# Fibonacci Sequence
num = int(input("Enter your Fibonacci Limit : "))

fib_seri = []
a = 0
b = 1

for _ in range(num):
    fib_seri.append(a)
    a, b = b, a + b

print(f"Your Fibonacci Series is : {fib_seri}")
#01123
# O(n)