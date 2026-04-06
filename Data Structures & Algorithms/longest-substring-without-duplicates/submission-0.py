class Solution:
    def lengthOfLongestSubstring(self, s: str):
        char_index = {}
        longest = 0
        left = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            longest = max(longest, right - left + 1)

        return longest