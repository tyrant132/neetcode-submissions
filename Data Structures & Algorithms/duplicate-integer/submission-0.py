class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n1,n2 = len(set(nums)),len(nums)
        if n1==n2:
            return False
        return True
        