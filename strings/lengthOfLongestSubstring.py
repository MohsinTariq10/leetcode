class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        hmap = {}
        maxi = 0
        local = 0
        while fast < len(s) and slow < len(s):
            if s[fast] in hmap:                
                hmap[s[slow]] = hmap[s[slow]] -1
                if hmap[s[slow]] == 0:
                    del hmap[s[slow]]
                slow +=1
                local -= 1    
            else:
                hmap[s[fast]] = 1
                local +=1
                fast +=1
                
            
            maxi = max(local, maxi)
        return maxi