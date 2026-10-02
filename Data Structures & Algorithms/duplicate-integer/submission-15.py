class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}
        for i in nums:
            if i in track:
                return True
            else:
                track[i] = 1
        return False