class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i,val in enumerate(nums):
            if target-val in d:
                return [d[target-val],i]
            else:
                d[val]=i