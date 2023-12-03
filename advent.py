###############################
# 1

lines = []
with open('data/input_1.txt') as f: 
    for _ in f:
        lines.append(_)
        
def get_first_get_last(lines):
    nums = []
    for line in lines:
        int_first = get_digit(line)
        int_last = get_digit(line[::-1])
        num = str(int_first) + str(int_last)
        nums.append(int(num))
    return sum(nums)
        
def get_digit(line):
    for char in line:
        if char.isdigit():
            return char
    return None
    
print(get_first_get_last(lines))

###############################
# 2

lines = []
with open('data/input_2.txt') as f: 
    for _ in f:
        lines.append(_)

def get_id_sum(lines):
    res = []
    for line in lines:
        id = line.split(':')[0].replace('Game ', '')
        line = line.split(':')[1]
        sets = line.split(';')
        over = False
        for set_ in sets:
            draw = set_.split(', ')
            for couple in draw:
                couple = couple.strip()
                splitted = couple.split(' ')
                for cell in splitted:  
                    num = int(splitted[0])
                    color = splitted[1]
                    if color == 'red' and num > 12:
                        over = True
                    if color == 'green' and num > 13:
                        over = True
                    if color == 'blue' and num > 14:
                        over = True
        if over == False:
            res.append(int(id))
    return sum(res)
                 
print(get_id_sum(lines))

###############################
# 3

import re

lines = []
with open('data/input_3.txt') as f: 
    for _ in f:
        lines.append(_)

# lines = [
#         '467..114..',
#         '...*......',
#         '..35..633.',
#         '......#...',
#         '617*......',
#         '.....+.58.',
#         '..592.....',
#         '......755.',
#         '...$.*....',
#         '.664.598..'
#         ]

def nums_near_symb(lines):
    count_lines = len(lines)
    adj_nums = []
    for index, line in enumerate(lines):
        if index == 0:
            prev_line = ''
        else:
            prev_line = lines[index - 1]
        if index == count_lines - 1:
            next_line = ''
        else:
            next_line = lines[index + 1]
        nums, positions = get_nums_and_pos(line)
        index_symb_prev = get_index_symb(prev_line)
        index_symb_curr = get_index_symb(line)
        index_symb_next = get_index_symb(next_line)
        grouped_indexes = group_indexes(positions)
        print(grouped_indexes)
        tot_symb_indexes = index_symb_prev + index_symb_curr + index_symb_next
        for num, indexes in zip(nums, grouped_indexes):
            adj = False
            for index in indexes:
                for sym_ind in tot_symb_indexes:
                    if (int(index) == sym_ind) or (int(index) - 1 == sym_ind) or (int(index) + 1 == sym_ind):
                        adj = True
            if adj == True:
                adj_nums.append(num)
    adj_nums = set(adj_nums)
    return sum(list(adj_nums))
                                
def get_nums_and_pos(line):
    position_nums = []
    nums_in_line = []
    num_line = ''
    for pos, char in enumerate(line):
            if char.isdigit():
                num_line += char
                position_nums.append(pos)
            if char == '.': 
                nums_in_line.append(num_line)
                num_line = ''
    nums_in_line = [int(x) for x in nums_in_line if x != '']  
    return nums_in_line, position_nums  

def get_index_symb(line):
    indexes = []
    pattern = re.compile(r'[^\w\s.]')
    for index, char in enumerate(line):
        if pattern.match(char):
            indexes.append(index)
    return indexes
 
def group_indexes(nums):
    grouped_nums = []
    current_group = []
    for num in nums:
        if not current_group or num - current_group[-1] == 1:
            current_group.append(num)
        else:
            grouped_nums.append(current_group)
            current_group = [num]
    if current_group:
        grouped_nums.append(current_group)
    grouped_strings = [''.join(map(str, group)) for group in grouped_nums]
    return grouped_strings       
        
print(nums_near_symb(lines))



            