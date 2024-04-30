# solution is unpotimized, O(n^2) runtime, will fix it in _O solution later


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range( len(nums) ):
            value = target - nums[i]
            if value in visited.values():
                list_key = list( visited.keys() )
                list_value = list( visited.values() )
                index = list_key[ list_value.index(value) ]
                return [ index, i ]
            else:
                visited[i] = nums[i]
        return []