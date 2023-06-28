def ans(nums):
    total_xor = 0
    n = len(nums)

    for mask in range(1 << n):
        subset_xor = 0
        for i in range(n):
            if (mask >> i) & 1:
                subset_xor ^= nums[i]
        total_xor += subset_xor

    return total_xor

y = ans([1,5,6])
print(y)