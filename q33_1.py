class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = l + (r - l) // 2
            if nums[middle] == target: return middle

            if nums[l] <= nums[middle]:
                # first half
                if nums[l] <= target and target < nums[middle]: r = middle - 1
                else: l = middle + 1
            else:
                # second half
                if nums[middle] < target and target <= nums[r]: l = middle + 1
                else: r = middle - 1
        
        return -1
