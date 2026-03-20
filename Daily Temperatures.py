class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        ans = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            if not mono_stack:
                mono_stack.append(index)
                continue
            while mono_stack and temperatures[mono_stack[-1]] <temperature:
                ans[mono_stack[-1]] =index - mono_stack[-1]
                mono_stack.pop()
            mono_stack.append(index)
            
        return ans

            
        

