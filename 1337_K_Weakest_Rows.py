import numpy as np

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        soldiers = []
        weakest = []
        for i in range(len(mat[0])):
            soldiers.append(sum(mat[i]))
        print(soldiers)
        while len(soldiers) >= k:
            self.popMin(soldiers, weakest)
        return soldiers, weakest
    
    def popMin(self, soldiers, weakest):
        index_min = np.argmin(soldiers)
        soldiers.pop(index_min)
        weakest.append(index_min)
        return soldiers, weakest



solution = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(solution.kWeakestRows(mat, k))