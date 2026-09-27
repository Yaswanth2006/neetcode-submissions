class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        x = 0
        while L < R:
            x = max(min(heights[L], heights[R]) * (R - L), x)
            if (heights[L] >= heights[R]):
                R -= 1
            else:
                L += 1
        return x
