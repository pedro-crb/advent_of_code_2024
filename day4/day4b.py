with open('day4/input.txt', 'r') as file:
    input_str = file.read()
    
xmas_count = 0
for i in range(142, len(input_str) - 142):
    if input_str[i] == 'A':
        diag1 = input_str[i-142] + input_str[i+142] 
        diag2 = input_str[i-140] + input_str[i+140] 
        if 'S' in diag1 and 'M' in diag1 and 'S' in diag2 and 'M' in diag2:
            xmas_count += 1
            
print(xmas_count)