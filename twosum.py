nums = [1, 3, 11, 2, 7]
target = 9


def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i

print(two_sum(nums, target))