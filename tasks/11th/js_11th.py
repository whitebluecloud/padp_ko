dp = [-1 for i in range(80)]
def fibo(n):
    dp[0] = 1
    dp[1] = 1
    if dp[n] is  not -1: return dp[n]
    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]

def solution(N):
    return 2*(fibo(N)+fibo(N-1))
