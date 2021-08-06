# palindrome-number

# 1. str으로 변환 
# 2. Slicing
# 3. 다시 int로 변환

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x) 
        if a==a[::-1]:
            a = int(a)
            return True