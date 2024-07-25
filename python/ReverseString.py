#input [ "h","e","l","l","o"]
#output ["o","l","l","e","h"]
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        while left<  right:
            hold = s[left]
            s[left] = s[right]
            s[right]= hold
            left += 1
            right -=1