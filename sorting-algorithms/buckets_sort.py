# 1. we have an array = [1, 3, 5, 2, 6, -2, 7]
# 2. create an array with N empty buckets: = [[], [], []]
# 3. according to some algorithm distribute all numbers in their buckets
# 4. using some algorithms to sort things inside those buckets
# 5. merge all buckets to one list
import heapq

def bucket_sort(arr: list[int]) -> list[int]:
    # create N bucket, usually best: ^0.5
    n_bucket = int(len(arr) ** 0.5)
    bucks = [[] for _ in range(n_bucket)]
    print(bucks)

    for i in arr:
        # do distributing accoridng to its value
        index = ((i - min(arr)) * n_bucket / (max(arr) - min(arr) + 1)) 
        bucks[int(index)].append(i)
    
    for ar in bucks:
        for i in range(len(ar)):
            ii = i
            while ii > 0 and ar[ii - 1] > ar[ii]:
                temp = ar[ii]
                ar[ii] = ar[ii - 1]
                ar[ii - 1] = temp
                ii -= 1
    res = [el for ar in bucks for el in ar]
    print(bucks)
    return res

arr = [1, 5, -5, 32, 654, 13, -6, 4, 0, 4, 4, 32] #12 root -> 3

print(bucket_sort(arr))