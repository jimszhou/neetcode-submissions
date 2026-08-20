class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            greedy + bisect

            tails = []
            maintain tail of a decrease number

            if nums[i] < tails[j]:
                tails[j] = nums[i]
            else:
                tails.append(nums[i])

            for find 'j' could use bisect.bisect_left(tails, nums[i])
        '''

        tails = []
        for num in nums:
            import bisect
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails): # means no smaller
                tails.append(num)
            else:
                tails[idx] = num # replace
        return len(tails)