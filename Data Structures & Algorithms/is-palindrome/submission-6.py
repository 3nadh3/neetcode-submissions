class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        length = len(s)
        
        required_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
        
        palindrome =''
        for i in range(length):
            if s[i] in required_characters:
                palindrome +=s[i]

        reverse = palindrome[::-1]


        if palindrome == reverse:
            return True
    
        return False