def partition(arr: list[int], start: int, end: int) -> int:
    pivot = arr[end]
    i = start - 1
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quickSort(arr: list[int], start: int, end: int) -> None:
    if start >= end:
        return
    
    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)


arr = [5, 2, 9, 1, 5, 6]
quickSort(arr, 0, len(arr) - 1)
print(arr)

