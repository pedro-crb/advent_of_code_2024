import re

with open('./input.txt', 'r') as file:
    input_str = file.read()
    
pattern = re.compile(r"mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))")
regex_result = re.findall(pattern, input_str)

enable = True
total = 0
for match in regex_result:
    if match[2] != '':
        enable = False
    elif match[3] != '':
        enable = True
    elif enable:
        total += int(match[0])*int(match[1])
        
print(total)