class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        def find_closest(heaters, house):
            left = 0
            right = len(heaters)-1

            while left <= right:
                mid = (left + right) //2

                if heaters[mid] == house:
                    return 0
                elif heaters[mid] > house:
                    right = mid - 1
                else:
                    left = mid + 1
            dist1 = float('inf')
            dist2 = float('inf')

            if left < len(heaters):
                dist1 = abs(heaters[left] - house)

            if right >= 0:
                dist2 = abs(heaters[right] - house)

            return min(dist1, dist2)
        
        radius = 0
        for house in houses:
            closest = find_closest(heaters, house)
            radius = max(radius, closest)

        return radius
