class Solution:
    def stepcount(self, n, s, xstart, ystart, i):
        count = 0
        for j in range(i, len(s)):
            if s[j] == "R":
                xstart += 1
            elif s[j] == "L":
                xstart -= 1
            elif s[j] == "U":
                ystart -= 1
            elif s[j] == "D":
                ystart += 1
            
            if xstart < 0 or ystart < 0 or xstart >= n or ystart >= n:
                return count
            count += 1
        return count
    
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        l = len(s)
        executed = [0 for i in range(l)]
        for i in range(l):
            executed[i] = self.stepcount(n, s, startPos[1], startPos[0], i)
        return executed
    
    