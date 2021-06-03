class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha=''
        for char in s:
            if char.isalpha() or char.isdigit():
                alpha+=char.lower()
        ans=''
        n=len(alpha)
        for i in range(n-1,-1,-1):
            ans+=alpha[i]
        return ans==alpha