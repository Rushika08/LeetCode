class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = {}
        start = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in myDict and myDict[char] >= start:
                start = myDict[char] + 1

            myDict[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length