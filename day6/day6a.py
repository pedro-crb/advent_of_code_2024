with open('day6/input.txt', 'r') as file:
    input_str = bytearray(file.read(), 'utf-8')
    
directions = [-131, 1, 131, -1]
guard_pos = input_str.find(b'^')
direction_idx = 0
visit_count = 1
while True:
    next_pos = guard_pos + directions[direction_idx]
    if next_pos < 0 or next_pos > len(input_str):
        break
    
    if input_str[next_pos] == b'\n'[0]:
        break
    
    if input_str[next_pos] == b'#'[0]:
        direction_idx = (direction_idx + 1) & 0x03
        continue
        
    if input_str[next_pos] == b'.'[0]:
        visit_count += 1
    
    input_str[guard_pos] = b'X'[0]
    guard_pos = next_pos
    
print(visit_count)
    