import heapq
in short:
    bucks = [[] for _ in range(n_bucket)]
    print(bucks)

    # let's use load balancing
    heap = [(0, i) for i in range(n_bucket)]
    heapq.heapify(heap) #put the smallest ot hte up[last]

    for el in arr:
        load, i = heapq.heappop(heap)

        bucks[i].append(el)
        load += 1

        heapq.heappush(heap, (load, i))