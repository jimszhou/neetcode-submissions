class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def is_sub(window, need: dict):
            for k, v in need.items():
                if window.get(k, 0) < v:
                    return False
            return True

        need = {}
        window = {}
        l = float('inf')
        start = 0
        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right = 0, 0
        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            right += 1
            while is_sub(window, need):
                if right - left < l:
                    l = right - left
                    start = left
                c = s[left]
                window[c] = window.get(c, 0) - 1
                left += 1
        return '' if l == float('inf') else s[start:start + l]

