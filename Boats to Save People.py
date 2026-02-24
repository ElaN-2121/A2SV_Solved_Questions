class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # limit = boat max weight
        min_boat = 0
        people.sort()
        left = 0
        right = len(people) -1

        while left <= right:
            if people[left] + people[right] <=limit:
                left +=1
            right -= 1
            min_boat += 1

        return min_boat

            
