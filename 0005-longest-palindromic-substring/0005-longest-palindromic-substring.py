class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Helper function to check if a substring is a palindrome
        def check(i: int, j: int) -> bool:
            left, right = i, j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Length of the input string
        n = len(s)

        # Iterate over decreasing lengths of substrings
        for length in range(n, 0, -1):
            # Iterate over starting positions for substrings of the current length
            for start in range(n - length + 1):
                # Extract the substring based on the current length and start
                substring = s[start:start + length]

                # Check if the substring is a palindrome using the check function
                if check(start, start + length):
                    # If palindrome, return the substring (first palindrome found)
                    return substring

        # Return an empty string if no palindrome is found
        return "" 
        