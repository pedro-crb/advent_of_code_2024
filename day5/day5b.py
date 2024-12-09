import copy

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

unordered = []
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
        
    if not is_safe:
        unordered.append(nums)
        
mid_sum = 0
for nums in unordered:
    final_list = []
    nums_set = set(nums)
    success_flag = True
    
    while success_flag:
        nums = copy.deepcopy(nums_set)
        if len(nums) == 0:
            break
        
        success_flag = False
        for num in nums:
            if len(nums_set & blocking_map[num]) == 0:
                final_list.append(num)
                nums_set.remove(num)
                success_flag = True

    mid_sum += final_list[len(final_list)//2]
    
print(mid_sum)
