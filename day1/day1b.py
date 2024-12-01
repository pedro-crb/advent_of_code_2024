number_counts: dict[int, list[int]] = {}

with open('day1/input.txt', 'r') as file:
    for line in file:
        line_data = line.split()
        lft_num = int(line_data[0])
        rgt_num = int(line_data[1])
        
        if lft_num in number_counts:
            number_counts[lft_num][0] += 1
        else:
            number_counts[lft_num] = [1, 0]
        
        if rgt_num in number_counts:
            number_counts[rgt_num][1] += 1
        else:
            number_counts[rgt_num] = [0, 1]

result = 0
for number, counts in number_counts.items():
    result += number * counts[0] * counts[1]

print(result)