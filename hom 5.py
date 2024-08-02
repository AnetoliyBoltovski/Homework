def longest_common_increasing_subsequence(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    dp = [0] * (m + 1)
    for i in range(n):
        current = 0
        for j in range(m):
            if arr1[i] == arr2[j]:
                if current + 1 > dp[j + 1]:
                    dp[j + 1] = current + 1
            elif arr1[i] > arr2[j]:
                if dp[j + 1] > current:
                    current = dp[j + 1]

    return max(dp)


arr1 = [1, 3, 4, 1, 2, 3]
arr2 = [3, 4, 1, 2, 1, 3]
print(longest_common_increasing_subsequence(arr1, arr2))
