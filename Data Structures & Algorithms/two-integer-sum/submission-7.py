class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, t in enumerate(nums):
            if t in track:
                return [track[t], i]
            else:
                track[target - t] = i