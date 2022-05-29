from subset_sum import subset_sum

def equal_sum_partition(arr: list[int]):
    length = len(arr)

    if len(arr) <= 1:
        return False
    
    total = sum(arr)

    if total % 2 != 0:
        return False

    return subset_sum(arr, total // 2)


print(equal_sum_partition([1, 6, 4, 3]))


    