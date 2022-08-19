class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = [i for i in range(1, m+1)]
        
        for i in range(len(queries)):
            index = perm.index(queries[i])
            perm.insert(0, perm.pop(index))
            queries[i] = index
        
        return queries