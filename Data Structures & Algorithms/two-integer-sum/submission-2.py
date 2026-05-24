class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #brute force approach
        # iterate through each indices and calculate the sum
        # if sum is equal to target then retur the index
        hash_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hash_map:
                return [hash_map[difference],i]
            hash_map[nums[i]] = i
        


       



        