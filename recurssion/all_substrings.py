s = ["bbcc"]
dp = {}

def all_substrings(s, dp):
    if len(s) == 0:
        return [""]
    
    if s not in dp:
        all_substrings(s[1:], dp)
        all_substrings(s[:-1], dp)
        dp[s] = 1
    return dp[s]
all_substrings(s, dp)
print(dp.keys())
