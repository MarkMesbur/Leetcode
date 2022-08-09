class Solution:
    def countAsterisks(self, s: str) -> int:
        pair = 0
        count = 0
        for char in s:
            if char == "|":
                pair += 1
            
            if pair % 2 == 0:
                if char == "*":
                    count += 1
        return count