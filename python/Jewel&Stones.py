class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        check_j = set(J)
        total = 0
        for st in S:
            if st in check_j:
                total += 1
        return total