class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}  
        window = {}        

        for c in s1:
            need[c] = need.get(c, 0) + 1

        matches = 0       
        required = len(need)
        left = 0

        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                matches += 1

            if right - left + 1 > len(s1):
                l = s2[left]
                if l in need and window[l] == need[l]:
                    matches -= 1         
                window[l] -= 1
                left += 1

            if matches == required:
                return True

        return False