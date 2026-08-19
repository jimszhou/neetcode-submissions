class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        window = {}

        while right < len(s):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            right += 1

            while window[c] > 1:
                d = s[left]
                window[d] -= 1
                left += 1

            # this part means no repeat
            ans = max(ans, right - left)

        return ans
