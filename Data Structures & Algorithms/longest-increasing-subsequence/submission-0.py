class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            dp[i] means LIS at nums[i]
            base case dp[i] = 1 because thats the min of IS
            j is [0, i-1]
            dp[i] = max(dp[i], dp[j] + 1)
        '''

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)