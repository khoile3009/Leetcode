class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, num in enumerate(nums):
            print(hmap.get(target - num))
            if hmap.get(target - num) != None:
                return [hmap.get(target - num), i]
            hmap[num] = i
        