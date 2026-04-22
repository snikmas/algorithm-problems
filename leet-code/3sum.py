def threeSum(nums: list[int]) -> list[list[int]]:
    # 1. sort arr
    nums.sort()

    res = []
    # 2. iterate throguh it
    for index, value in enumerate(nums):
        if index > 0 and value == nums[index - 1]:
            continue

        l, r = index + 1, len(nums) - 1
        while l < r:
            sum = value + nums[r] + nums[l]
            if sum == 0:
                res.append([value, nums[r], nums[l]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1 
            elif sum < 0:
                l += 1
            else: r -= 1
    return res

#


nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(threeSum(nums))

nums = [0,1,1]
print(threeSum(nums))

nums = [0,0,0]
print(threeSum(nums))

# Output: [[0,0,0]]