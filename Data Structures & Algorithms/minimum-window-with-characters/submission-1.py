class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        l = float('inf')
        start = 0

        left, right = 0, 0

        # increase window
        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            # shrink window
            while have == need_count:
                if right - left + 1 < l:
                    l = right - left + 1
                    start = left

                c = s[left]
                window[c] -= 1
                if c in need and window[c] < need[c]:
                    have -= 1
                left += 1
            right += 1
        return '' if l == float('inf') else s[start:start+l]

