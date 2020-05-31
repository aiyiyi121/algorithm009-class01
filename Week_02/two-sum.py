class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind, num in enumerate(nums):
            hash_map[num] = ind
        for i, num in enumerate(nums):
            j = hash_map.get(target - num)
            if j is not None and i != j:
                return [i, j]
