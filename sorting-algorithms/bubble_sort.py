def bubble_sort(arr: list[int]) -> list[int]:
    is_sorted = True
    for i in range(len(arr)):
        for ii in range(len(arr) - i - 1):
            if arr[ii] > arr[ii + 1]:
                is_sorted = False
                temp = arr[ii + 1]
                arr[ii + 1] = arr[ii]
                arr[ii] = temp
        if is_sorted: 
            print('is sorted, go out')
            return arr # no need for sort
    return arr



a = [4, 6, 2, 1, 5, 6, 6, 6, 9, 21]
print(bubble_sort(a))

a = []
print(bubble_sort(a))

a = [1, -6]
print(bubble_sort(a))

a = [1, 5]
print(bubble_sort(a))

## stable
# to: worst case O(n^2)
# rarely used
#chinese name mao4pao4 renleifa