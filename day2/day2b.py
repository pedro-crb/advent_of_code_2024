safe_count = 0
with open('day2/input.txt', 'r') as file:
    for line in file:
        line_data = list(map(int, line.split()))
        is_safe = True
        diffs = [line_data[i+1] - line_data[i] for i in range(len(line_data) - 1)]
        check_sign = sum([d/abs(d) for d in diffs[:3] if d != 0])
        if check_sign == 0:
            continue
        check_sign /= abs(check_sign)
        check_set = {check_sign*1, check_sign*2, check_sign*3}

        i = 0
        has_error = False
        while is_safe and i < len(diffs):
            if diffs[i] in check_set: 
                i += 1
            elif has_error:
                is_safe = False
                break
            elif (i==0 or (diffs[i-1] + diffs[i] in check_set)) and ((i == len(diffs) - 1) or (diffs[i + 1] in check_set)):
                has_error = True
                i += 2
            elif (i == len(diffs) - 1) or (diffs[i] + diffs[i + 1] in check_set):
                has_error = True
                i += 2
            else:
                is_safe = False
                break
        
        if is_safe:
            safe_count += 1
                   
print(safe_count)