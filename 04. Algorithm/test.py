import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  sorted_nums = []
  while nums:
    sorted_nums.append(heapq.heappop(nums))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))