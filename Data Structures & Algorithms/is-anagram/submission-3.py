class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        seen_s = {}
        for i in range(len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] = seen_s[s[i]] +1
            else:
                seen_s[s[i]] = 1
       
        seen_t = {}
        for i in range(len(t)):
            if t[i] in seen_t:
                seen_t[t[i]] = seen_t[t[i]] +1
            else:
                seen_t[t[i]] =1
    
        if seen_s == seen_t:
            return True
        
        return False