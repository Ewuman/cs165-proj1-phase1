from insertion_sort import insertion_sort
from tim_sort import tim_sort
from shell_sort import shell_sort1, shell_sort2, shell_sort3, shell_sort4, shell_sort5
import random
import math
import time

def uniform_permutation(n):
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr

def almost_sorted_permutation(n):
    arr = list(range(1, n + 1))
    
    num_swaps = int(math.log2(n))  # or math.log(n)
    
    for _ in range(num_swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def two_run_permutation(n):
    odds = list(range(1, n + 1, 2))
    evens = list(range(2, n + 1, 2))
    return odds + evens



if __name__ == "__main__":
