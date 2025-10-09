class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)
        current_permutation = []
        def backtrack(results, current_permutation, nums):
            # base case: 모든 숫자를 다 사용했으면 결과에 추가
            if not nums:
                results.append(list(current_permutation))
                return

            # 재귀 호출
            for i in range(len(nums)):
                # 현재 숫자를 순열에 추가
                current_permutation.append(nums[i])
                
                # 다음 숫자를 선택하기 위해 재귀 호출
                # (현재 사용한 숫자를 제외한 나머지 목록을 넘겨줌)
                backtrack(results, current_permutation, nums[:i] + nums[i+1:])
                
                # 백트래킹: 다음 반복을 위해 마지막에 추가했던 숫자 제거
                current_permutation.pop()

        backtrack(results, current_permutation, nums)
        return results