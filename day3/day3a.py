import re

with open('./input.txt', 'r') as file:
    input_str = file.read()
    
pattern = re.compile(r'mul\((\d+),(\d+)\)')
regex_result = re.findall(pattern, input_str)
result = sum([int(a)*int(b) for (a, b) in regex_result]) 

print(result)