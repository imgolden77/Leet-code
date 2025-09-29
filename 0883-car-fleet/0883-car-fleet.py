class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= sorted(zip(position, speed), key=lambda x:x[0], reverse = True)
        stack =[]
        for pos, speed in cars:
            time_target = (target-pos)/speed
            
            if not stack or time_target > stack[-1]:
                stack.append(time_target)

        return len(stack)