class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        prev = chars[-1]
        i = len(chars)-2
        
        while (i > -1):
            if prev == chars[i]:
                count +=1
            else: 
                if count > 1:
                    chars[i+1:i+1+count] = list(prev+str(count))
                    count = 1
            prev = chars[i]
            i -= 1
        if count > 1:
            chars[i+1:i+1+count] = prev+str(count)
        return len(chars)