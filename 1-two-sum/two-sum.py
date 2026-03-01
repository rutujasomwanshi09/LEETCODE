# ////Rutuja
class Solution:
    def twoSum(self, nums, target):
        seen = {}   # dictionary to store number : index

        for i in range(len(nums)):
            required = target - nums[i]

            if required in seen:
                return [seen[required], i]

            seen[nums[i]] = i

# nums = [2, 7, 11, 15]
# target = 9
obj = Solution()
print(obj.twoSum([2,7,11,15],9))
# result = twoSum(nums,target)
# print(result)  # Output: [0, 1]