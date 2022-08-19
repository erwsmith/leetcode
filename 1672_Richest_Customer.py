class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            if wealth > max:
                max = wealth
        return max
    
solution = Solution()
accounts = [[1,2,3],[3,2,1,4],[5,1,3]]
print(solution.maximumWealth(accounts)) 