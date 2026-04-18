def tim_sort(nums: list[int]):
    num_comparisons = 0
    runs = []
    stack = []
    while runs:
        run = runs.pop()
        stack.append(run)

        while True:
            height = len(stack)
            if height >= 3 and len(stack[0]) > len(stack[2]):
                tim_merge(stack[1], stack[2], stack)
            elif height >= 2 and len(stack[0]) >= len(stack[1]):
                tim_merge(stack[0], stack[1], stack)
            elif height >= 3 and len(stack[0]) + len(stack[1]) >= len(stack[2]):
                tim_merge(stack[0], stack[1], stack)
            elif height >= 4 and len(stack[1]) + len(stack[2]) >= len(stack[3]):
                tim_merge(stack[0], stack[1], stack)
            else:
                break

    while len(stack) != 1:
        tim_merge(stack[0], stack[1], stack)

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



def tim_merge(run1: list[int], run2: list[int], stack: list[int]):
    # Edits stack and returns num_comparisons
    pass