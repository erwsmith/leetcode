from operator import itemgetter

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        ranks = []
        # create list of tuples, preserving the original index
        for i, row in enumerate(mat):
            ranks.append((i, sum(row)))
        # sort list of tuples using second item as key
        ranks = sorted(ranks, key=itemgetter(1))
        # take slice of ranks to get just first k items
        ranks = ranks[:k]
        output = []
        # create list of just the original indices
        for i in range(len(ranks)):
            output.append(ranks[i][0])
        return output

solution = Solution()
mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
print(solution.kWeakestRows(mat, k))