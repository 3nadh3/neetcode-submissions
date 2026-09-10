class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_s = len(s)
        length_t = len(t)

        if length_s != length_t:
            return False
        
        dict_s = {}

        for i in s:
            dict_s[i] = dict_s.get(i,0) +1
        
        dict_t = {}
        for i in t:
            dict_t[i] = dict_t.get(i,0) +1

        if dict_s == dict_t:
            return True
        
        return False