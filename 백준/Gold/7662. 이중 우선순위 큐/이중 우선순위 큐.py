import heapq
import sys

input = sys.stdin.readline


def is_empty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


def dual_priority_queue(operations):
    min_heap = []
    max_heap = []
    nums = {}

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if op == 'I':
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)

        elif op == 'D':
            if not is_empty(nums.items()):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del nums[temp]
                    nums[-max_heap[0]] -= 1
                elif num == -1:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del nums[temp]
                    nums[min_heap[0]] -= 1

    if is_empty(nums.items()):
        return "EMPTY"
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        return f"{-max_heap[0]} {min_heap[0]}"


T = int(input().strip())
results = []

for _ in range(T):
    k = int(input().strip())
    operations = [input().strip() for _ in range(k)]
    results.append(dual_priority_queue(operations))

for result in results:
    print(result)