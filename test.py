def threeSum(nums):
    nums.sort()
    length = len(nums)
    res = []

    L = 0
    while 0 <= L < length - 1:
        R = length - 1
        while R - L > 1:
            i = L + 1
            while L + 1 <= i < R:
                print(L, i, R)
                dev = nums[L] + nums[R] + nums[i] - 0
                if dev == 0:
                    res.append([nums[L], nums[i], nums[R]])
                    break
                elif dev > 0:
                    break
                i += 1
            R = R - 1
            while R >= 0 and nums[R] == nums[R + 1]:
                R = R - 1
        L = L + 1
        while L < length and nums[L] == nums[L - 1]:
            L = L + 1
    return res


print(threeSum([3, 0, -2, -1, 1, 2]))
print(threeSum([-1, 0, 1, 2, -1, -4]))
