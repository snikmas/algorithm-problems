def topKFrequent(nums: list[int], k: int) -> list[int]:
    #1. calculate everytihng
    counts = {}
    max_occurence = -1
    for el in nums:
        counts[el] = counts.get(el, 0) + 1
        if counts[el] > max_occurence:
            max_occurence = counts[el]

    # 2. do bucks:
    bucks = [[] for _ in range(1 + max_occurence)]
    
# 3. arrange them
    for key, value in counts.items():
        bucks[value].append(key)


    all_items = [el for buck in bucks for el in buck]
    return all_items[len(all_items) - k:]

nums = [1,2,2,3,3,3, 3]
k = 2
print(topKFrequent(nums, k))

# Output: [2,3]

nums = [7,7]
k = 1
print(topKFrequent(nums, k))
#output [7]

