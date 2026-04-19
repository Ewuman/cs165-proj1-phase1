import math

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


def shell_sort2(nums: list[int]):
    num_comparisons = 0
    n = len(nums)

    k = 1
    prev_gap = None
    while True:
        gap = 2 * (n // (2 ** (k+1))) + 1
        if gap <= 0 or gap == prev_gap:
            break

        prev_gap = gap

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

        k += 1
    
    return num_comparisons


def shell_sort3(nums: list[int]):
    num_comparisons = 0
    n = len(nums)

    k = int(math.log2(n))
    gaps = []
    while k >= 1:
        gaps.append((2 ** k) + 1)
        k -= 1
    
    gaps.append(1)

    for gap in gaps:
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
    
    return num_comparisons


def shell_sort4(nums: list[int]):
    num_comparisons = 0
    n = len(nums)

    gaps = set()
    p = 0
    while 2 ** p < n:
        q = 0
        while (2 ** p) * (3 ** q) < n:
            gaps.add((2 ** p) * (3 ** q))
            q += 1
        p += 1
    gaps = sorted(gaps, reverse=True)
    
    for gap in gaps:
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
    
    return num_comparisons