class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        ss = ""
        for i in range(len(s)):
            if ord(s[i]) in range(97,123) or s[i].isdigit():
                ss+=s[i]
        return ss==ss[::-1]