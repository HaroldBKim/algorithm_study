N = int(input())
lst = [0]+list(map(int, input().split()))

# dp테이블 생성 및 초기화(dp[0]=0)
dp = [0]*(N+1)

for i in range(1, N+1):
    mx = 0
    for j in range(0, i):   # 0 ~ i-1 중에서 max값(나보다 작은 값 중)
        if lst[i]>lst[j]:
            mx = max(mx, dp[j])
    dp[i] = mx+1

# 주의: 중간에 최대값이 있을 수 있으므로, max 찾아야 함!
print(max(dp))