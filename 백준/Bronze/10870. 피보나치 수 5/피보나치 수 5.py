N = int(input())

def fibo(n):
    if (n <= 2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

if (N == 0):
    print(0)
else:
    print(fibo(N))