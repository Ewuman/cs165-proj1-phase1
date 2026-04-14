# Example file: insertion_sort.py
# Each sorting function should accept a list of integers as the single required
# parameter, as shown below. The input list should be sorted upon completion.
def insertion_sort(nums: list[int]):
    num_comparisons = 0
    for i in range(len(nums)):
        current = i
        if i == 0:
            continue

        ## Compare with previous nums
        while (current > 0):
            num_comparisons += 1
            if nums[current] < nums[current-1]:
                nums[current], nums[current-1] = nums[current-1], nums[current]
                current -= 1
            else:
                break

    return num_comparisons
