class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}          # frequency map of s1
        window = {}        # frequency map of current window in s2

        for c in s1:
            need[c] = need.get(c, 0) + 1

        matches = 0        # how many chars have matching frequencies
        required = len(need)
        left = 0

        for right in range(len(s2)):
            # expand window — add right character
            c = s2[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                matches += 1

            # window too large — shrink from left
            if right - left + 1 > len(s1):
                l = s2[left]
                if l in need and window[l] == need[l]:
                    matches -= 1          # about to break a match
                window[l] -= 1
                left += 1

            # all characters matched
            if matches == required:
                return True

        return False