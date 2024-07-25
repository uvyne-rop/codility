#s= "Leetcode"
#output = 0
class Solution:
    def firstUniqueChar(self, s: str)-> int:
        str_dict = {}
        for ch in s:
            if ch not in str_dict:
                str_dict[ch] = True
            else:
                str_dict[ch] = False

        for i,c in enumerate(s):
            if str_dict[c]:
                return i
        return -1