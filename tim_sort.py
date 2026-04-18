def tim_sort(nums: list[int]):
    num_comparisons = 0
    runs = gen_runs(nums)
    stack = []

    while runs:
        run = runs.pop(0)
        stack.append(run)

        while True:
            height = len(stack)
            if height >= 3 and len(stack[-1]) > len(stack[-3]):
                num_comparisons += tim_merge(stack[-3], stack[-2], stack, len(stack) - 3)
            elif height >= 2 and len(stack[-1]) >= len(stack[-2]):
                num_comparisons += tim_merge(stack[-2], stack[-1], stack, len(stack) - 2)
            elif height >= 3 and len(stack[-1]) + len(stack[-2]) >= len(stack[-3]):
                num_comparisons += tim_merge(stack[-2], stack[-1], stack, len(stack) - 2)
            elif height >= 4 and len(stack[-2]) + len(stack[-3]) >= len(stack[-4]):
                num_comparisons += tim_merge(stack[-2], stack[-1], stack, len(stack) - 2)
            else:
                break

    while len(stack) != 1:
        num_comparisons += tim_merge(stack[-1], stack[-2], stack, len(stack) - 2)

    return num_comparisons


def gen_runs(nums: list[int]):
    runs = []

    i = 0
    n = len(nums)
    while i < n:
        run = [nums[i]]
        i += 1

        if i == n:
            runs.append(run)
            break

        # determine direction
        if nums[i] < nums[i - 1]:
            # descending
            while i < n and nums[i] < nums[i - 1]:
                run.append(nums[i])
                i += 1
            run.reverse()
        else:
            # non-descending
            while i < n and nums[i] >= nums[i - 1]:
                run.append(nums[i])
                i += 1

        runs.append(run)
    
    return runs


def tim_merge(run1: list[int], run2: list[int], stack: list[int], index):
    # index: index of run to remove from stack
    num_comparisons = 0

    merged = []
    i = j = 0
    while i < len(run1) and j < len(run2):
        num_comparisons += 1
        if run1[i] <= run2[j]:
            merged.append(run1[i])
            i += 1
        else:
            merged.append(run2[j])
            j += 1
    
    merged.extend(run1[i:])
    merged.extend(run2[j:])
    stack[index] = merged # R2 is now the merged runs
    stack.pop(index + 1)

    return num_comparisons
