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

    new_run = True
    descending = False
    cur_run = []
    for i in range(len(nums)):
        if new_run:
            cur_run.append(nums[i])
            new_run = False
        else:
            if descending:
                if nums[i] < cur_run[-1]:
                    cur_run.append(nums[i])
                else:
                    runs.append(cur_run)
                    cur_run = []
                    cur_run.append(nums[i])
                    descending = False
            else:
                if len(cur_run) == 1:
                    if nums[i] < cur_run[-1]:
                        descending = True
                    cur_run.append(nums[i])
                    continue

                if nums[i] < cur_run[-1]:
                    descending = True
                    runs.append(cur_run)
                    cur_run = []
                    cur_run.append(nums[i])
                else:
                    cur_run.append(nums[i])

    if cur_run:
        runs.append(cur_run)
    
    return runs


def tim_merge(run1: list[int], run2: list[int], stack: list[int], index):
    # index: index of run to remove from stack
    num_comparisons = 0
    if (run1[0] > run1[-1]):
        run1.reverse()
    if (run2[0] > run2[-1]):
        run2.reverse()

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
