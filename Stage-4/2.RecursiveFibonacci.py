# Recursive Fibonacci



# def Fibonacci(num):
#     fibo = []
#     a=0
#     b=1
#     for _ in range(num):
#         fibo.append(a)
#         a,b=b,a+b
#     return fibo
# print(Fibonacci(5))



# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# for i in range(6):
#     print(fibonacci(i), end=" ")



n = int(input("Enter the value:"))
arr = []
for i in range(n + 1):
   arr.append(0)

def fibo(n):
    if(n == 0):
       return 0
    elif(n == 1):
       return 1
    elif(arr[n] != 0):
       return arr[n]
    else:
       p = fibo(n - 1) + fibo(n - 2)
       arr[n] = p
       return(p)
for i in range(n + 1):
    print(fibo(i), end=" | ")