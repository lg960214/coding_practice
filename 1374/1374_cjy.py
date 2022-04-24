import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[2]))
finish_times = []
result = 0
for lecture in lectures:
    if not finish_times:
        heapq.heappush(finish_times, lecture[2])
        result += 1
    else:
        if finish_times[0] > lecture[1]:
            result += 1
            heapq.heappush(finish_times, lecture[2])
        else:
            heapq.heappop(finish_times)
            heapq.heappush(finish_times, lecture[2])
        
print(result)
