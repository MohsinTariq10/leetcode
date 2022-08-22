def canPermutePalindrome(self, s: str) -> bool:
    hmap = {}
    countOdds = 0
    for c in s.lower():
        hmap[c] = hmap.get(c, 0) +1
        if hmap[c]%2 == 0:
            countOdds -=1
        else:
            countOdds +=1
            
    return countOdds<=1