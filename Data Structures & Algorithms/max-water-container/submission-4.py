class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans, L, R = 0, 0, len(heights) - 1

        while L < R:
            ans = max(ans, min(heights[L], heights[R]) * (R - L))
            if heights[R] >= heights[L]:
                L += 1
            else:
                R -= 1
        return ans                
