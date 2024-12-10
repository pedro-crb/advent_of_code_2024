import re
import time

t0 = time.perf_counter()
final_sum = 0
with open('day7/input.txt', 'r') as file:
    for line in file:
        match = list(map(int, re.findall(r'\d+', line)))
        target = match[0]
        nums = match[1:]
        for i in range(1<<(len(nums)-1)):
            result = nums[0]
            for j, n in enumerate(nums[1:]):
                if ((1<<j) & i) == 0:
                    result += n
                else:
                    result *= n
            if result == target:
                final_sum += target
                break

print(final_sum)
              