def shell_sort1(nums: list[int]):
    num_comparisons = 0
    n = len(nums)

    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i

            while j >= gap and nums[j-gap] > temp:
                num_comparisons += 1
                nums[j] = nums[j-gap]
                j -= gap

            if j >= gap:
                num_comparisons += 1

            nums[j] = temp

        gap //= 2
    
    return num_comparisons