class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        window = {}
        has_repeat = False

        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if window[c] != 1:
                has_repeat = True
            right += 1

            while has_repeat:
                c = s[left]
                if window[c] == 2:
                    has_repeat = False
                window[c] -= 1
                left += 1

            # this part means no repeat
            ans = max(ans, right - left)

        return ans
