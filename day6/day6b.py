import copy

with open('day6/input.txt', 'r') as file:
    input_str = bytearray(file.read(), 'utf-8')

directions = [-131, 1, 131, -1]
direction_chars = [b'^'[0], b'>'[0], b'V'[0], b'<'[0]]
guard_pos = input_str.find(b'^')
obstruction_count = 0
direction_idx = 0
count = 0
while True:
    next_pos = guard_pos + directions[direction_idx]
    
    if next_pos < 0 or next_pos > len(input_str):
        break
    if input_str[next_pos] == b'\n'[0]:
        break
    
    if input_str[next_pos] == b'#'[0]:
        direction_idx = (direction_idx + 1) & 0x03
        continue
    
    old_guard_pos = guard_pos
    old_direction = direction_idx
    old_next_pos = next_pos
    
    # navigate separate map with obstruction
    if input_str[next_pos] not in direction_chars:
        obstructed_str = copy.copy(input_str)
        obstructed_str[next_pos] = b'#'[0]
        while True:
            next_pos = guard_pos + directions[direction_idx]
            if next_pos < 0 or next_pos > len(input_str):
                break
            if obstructed_str[next_pos] == b'\n'[0]:
                break
            if obstructed_str[next_pos] == b'#'[0]:
                direction_idx = (direction_idx + 1) & 0x03
                continue
            if direction_chars[direction_idx] == obstructed_str[guard_pos]:
                obstruction_count += 1
                break
            obstructed_str[guard_pos] = direction_chars[direction_idx]
            guard_pos = next_pos
            
    guard_pos = old_guard_pos
    direction_idx = old_direction
    input_str[guard_pos] = direction_chars[direction_idx]
    guard_pos = old_next_pos

print(obstruction_count)