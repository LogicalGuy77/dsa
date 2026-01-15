def countDistinct(s):
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1

    last_occur = {}

    for i in range(1, n+1):
        ch = s[i-1]
        dp[i] = 2*dp[i-1]

        if ch in last_occur:
            dp[i] = dp[i] - dp[last_occur[ch] - 1]

        last_occur[ch] = i

    return dp[n]


def betterString(n1, n2):
    x = countDistinct(n1)
    y = countDistinct(n2)

    print(n1) if x >= y else print(n2)

betterString("gfg", "ggg")