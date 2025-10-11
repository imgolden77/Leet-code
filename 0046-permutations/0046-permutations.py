class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr =[]
        n= len(nums)
        visited =[False]*n

        def backtrack():
            if visited == [True]*n:
                res.append(list(curr))
                return

            for i in range(n):
                if visited[i] == False:
                    curr.append(nums[i])
                    visited[i] = True

                    backtrack()

                    visited[i] = False
                    curr.pop()

        backtrack()
        return res

