blocking_map: dict[int, set[int]] = {}

with open('day5/input.txt', 'r') as file:
    file_lines = file.readlines()

i = 0
while True:
    line = file_lines[i]
    i += 1
    if len(line) < 2:
        break
    nums = list(map(int, line.split('|')))
    if nums[1] not in blocking_map:
        blocking_map[nums[1]] = set()
    blocking_map[nums[1]] |= set([nums[0]])

mid_sum = 0
while i < len(file_lines):
    line = file_lines[i]
    i += 1
    if len(line) < 2:
        break
    nums = list(map(int, line.split(',')))
    blocked_numbers = set()
    is_safe = True
    
    for num in nums:
        if num in blocked_numbers:
            is_safe = False
            break
        blocked_numbers |= blocking_map[num]
        
    if is_safe:
        mid_sum += nums[len(nums)//2]
        
print(mid_sum)       
