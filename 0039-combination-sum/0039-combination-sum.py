class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(remaining_target, current_combination, start_index):
            # Base case 1: A valid combination is found
            if remaining_target == 0:
                # Add a copy of the current combination to the results
                results.append(list(current_combination))
                return
            
            # Base case 2: The sum has exceeded the target, invalid path
            if remaining_target < 0:
                return

            # Explore further combinations
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # Add the candidate to the current combination
                current_combination.append(candidate)
                
                # Recursively call with the new state
                # We pass 'i' as the start_index because we can reuse the same element
                backtrack(remaining_target - candidate, current_combination, i)
                
                # Backtrack: remove the last added candidate to explore other possibilities
                current_combination.pop()

        # Initial call to start the backtracking process
        backtrack(target, [], 0)
        
        return results