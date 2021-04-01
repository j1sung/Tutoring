'''
def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print(n-1 + n-2)

n = int(input("0이상 숫자 입력: "))
fibonacci(n)
'''

dp = [0, 1, 1]
def fibo(N):
    for i in range(3, N + 1):
        dp.append(dp[i - 2] + dp[i - 1])
N = int(input())
print(dp[N])