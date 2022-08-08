class Solution:
    def countPoints(self, rings: str) -> int:
        hsh = {}
        count = 0
        for i in range(1, len(rings), 2):
            if rings[i] in hsh:
                hsh[rings[i]] += rings[i-1]
            else:
                hsh[rings[i]] = rings[i-1]
        
        for key, value in hsh.items():
            if "B" in value and "G" in value and "R" in value:
                count += 1
        return count