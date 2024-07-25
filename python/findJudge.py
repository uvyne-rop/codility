class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        for person1, person2 in trust:
            trust_count[person1] -1
            trust_count[person2] += 1
        #print (trusted)
        for i in range(1, N+1):
            if trust_count[i] == N-1:
                return i
        return -i