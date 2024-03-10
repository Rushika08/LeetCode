class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        maxArea = 0

        while left_index < right_index:
            shorter = min(height[left_index], height[right_index])
            width = right_index - left_index
            area = shorter * width

            if area > maxArea:
                maxArea = area

            if shorter == height[left_index]:
                left_index += 1
            else:
                right_index -= 1

        return maxArea
