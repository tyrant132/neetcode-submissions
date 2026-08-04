class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        valid = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
        while i<=j:
            while i<len(s) and s[i] not in valid:
                i+=1
            while j>=0 and s[j] not in valid:
                j-=1
            if j>=0 and i<len(s) and s[i].lower()!=s[j].lower():
                return False
            j-=1
            i+=1
        return True