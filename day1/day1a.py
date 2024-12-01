left_list = []
right_list = []

with open('./input.txt', 'r') as file:
    for line in file:
        line_data = line.split('')
        left_list.append(line_data[0])
        right_list.append(line_data[1])
        
left_list.sort()
right_list.sort()

differences = [abs(lft - rgt) for lft, rgt in zip(left_list, right_list)]

result = sum(differences)

print(result)