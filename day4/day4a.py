with open('day4/input.txt', 'r') as file:
    input_str = file.read()

char_map = {
    'X': 0,
    'M': 1,
    'A': 2,
    'S': 3,
    '\n': 4,
}
    
xmas_count = 0
for i in range(len(input_str)):
    character_id = char_map[input_str[i]]
    if character_id == 0:
        sequence_step = 1
    elif character_id == 3:
        sequence_step = -1
    else:
        continue
    
    for direction in [1, 140, 141, 142]:
        next_char_id = character_id + sequence_step
        next_position = i + direction
        if next_position >= len(input_str):
            break
        while char_map[input_str[next_position]] == next_char_id:
            next_char_id += sequence_step
            if next_char_id < 0 or next_char_id > 3:
                xmas_count += 1
                break
            next_position += direction
            if next_position >= len(input_str):
                break
            
print(xmas_count)