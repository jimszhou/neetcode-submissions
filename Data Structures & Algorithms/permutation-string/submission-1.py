class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1

        window = {}
        match, expect = 0, len(need)

        left, right = 0, 0

        while right < len(s2):
            c = s2[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                match += 1

            right += 1

            while match == expect:
                if right - left == len(s1):
                    return True
                c = s2[left]
                window[c] -= 1
                if c in need and window[c] < need[c]:
                    match -= 1
                left += 1
        
        return False