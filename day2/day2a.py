
safe_count = 0
with open('day2/input.txt', 'r') as file:
    for line in file:
        line_data = line.split()
        prev_diff = 0
        is_safe = True
        for i in range(len(line_data) - 1):
            diff = int(line_data[i + 1]) - int(line_data[i])
            if (diff not in (-3, -2, -1, 1, 2, 3)) or (diff * prev_diff < 0):
                is_safe = False
                break
            prev_diff = diff
        if is_safe:
            safe_count += 1
            
print(safe_count)
            
            