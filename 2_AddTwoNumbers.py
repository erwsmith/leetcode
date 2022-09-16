# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        c1 = [str(i) for i in l1]
        c2 = [str(i) for i in l2]
        s1 = int("".join(c1))
        s2 = int("".join(c2))
        return list(str(s1 + s2))[::-1]

solution = Solution()
list1 = [2, 4, 3]
list2 = [5, 6, 4]
print(solution.addTwoNumbers(list1, list2))
