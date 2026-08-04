class Solution:
    def removeDuplicates(self, nums):
        # If array is empty
        if len(nums) == 0:
            return 0

        # Pointer for unique elements
        i = 0

        # Traverse the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # Number of unique elements
        return i + 1