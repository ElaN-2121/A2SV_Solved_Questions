class Solution:
    def numRabbits(self,answers):
        # Count how many times each answer appears
        freq = Counter(answers)
    
        total = 0
        for a, count in freq.items():
            group_size = a + 1
            # Number of groups needed for this answer
            groups = math.ceil(count / group_size)
            # Each group contributes group_size rabbits
            total += groups * group_size
    
        return total
