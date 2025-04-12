res = []


def fast_sort(nums):
    if nums:
        if len(nums) == 1:
            res.append(nums[0])
        # elif len(nums)== 2:
        #     mid = nums[1]
        #     if nums[0] < mid:
        #         res.extend([nums[0], nums[1]])
        #     else:
        #         res.extend([nums[1], nums[0]])
        else:
            mid = nums[-1]
            left = []
            right = []
            for i in nums[0:-1]:
                if i < mid:
                    left.append(i)
                else:
                    right.append(i)
            fast_sort(left)
            res.append(mid)
            fast_sort(right)


fast_sort([1, 5, 6, 7, 1, 2, 3])
print(res)
