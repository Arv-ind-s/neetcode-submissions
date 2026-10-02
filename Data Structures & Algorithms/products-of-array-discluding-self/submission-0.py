class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        answer = [1]*n
        for  i in range(n):
            answer[i] = prefix
            prefix = prefix*nums[i]
        for i in range(n-1,-1,-1):
            answer[i]= answer[i]*suffix
            suffix =suffix*nums[i]
        return answer
        
        