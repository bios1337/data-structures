from count_subset_sum import count_subset_sum

def count_sum_diff(arr: list[int], diff: int) -> int:
    total = sum(arr)

    if (total + diff) % 2 != 0:
        return 0

    target = (total + diff) // 2
    return count_subset_sum(arr, target)


print(count_sum_diff([1,2,3,3,2,1], 2))
