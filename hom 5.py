function
longest_common_increasing_subsequence(arr1, arr2):
n = len(arr1)
m = len(arr2)

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i from 1 to n:
    for j from 1 to m:
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = 1 + max(dp[x][j - 1] for x
            from

            1
            to
            i - 1 if arr1[x - 1] < arr1[i - 1])
            else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

result = max(max(row) for row in dp)
return result
