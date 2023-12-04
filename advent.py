#####
# 1 #
#####

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
    
print('Solution n°1: ', get_first_get_last(lines))

#####
# 2 #
#####

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
                 
print('Solution n°2: ', get_id_sum(lines))

#####
# 3 #
#####

import re

lines = []
with open('data/input_3.txt') as f: 
    for _ in f:
        lines.append(_)

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
        tot_symb_indexes = index_symb_prev + index_symb_curr + index_symb_next
        for num, indexes in zip(nums, grouped_indexes):
            adj = False
            for index in indexes:
                for sym_ind in tot_symb_indexes:
                    if (int(index) == sym_ind) or (int(index) - 1 == sym_ind) or (int(index) + 1 == sym_ind):
                        adj = True
            if adj == True:
                adj_nums.append(num)
    return sum(adj_nums)
                                
def get_nums_and_pos(line):
    position_nums = []
    nums_in_line = []
    num_line = ''
    for pos, char in enumerate(line):
        if char.isdigit():
            num_line += char
            position_nums.append(pos)
        pattern = re.compile(r'[^\w\s.]')
        if char == '.' or pattern.match(char): 
            nums_in_line.append(num_line)
            num_line = ''
    nums_in_line.append(num_line)
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
    return grouped_nums       
        
print('Solution n°3: ', nums_near_symb(lines))

#####
# 4 #
#####

lines = []
with open('data/input_4.txt') as f: 
    for _ in f:
        lines.append(_)

def get_points(lines):
    result = 0
    for line in lines:
        values = line.split(': ')[1:]
        winning = values[0].split('|')[0]
        winning = winning.split(' ')
        winning = [x for x in winning if x != '']
        extracted = values[0].split('|')[1]
        extracted = extracted.split(' ')
        extracted = [x.strip() for x in extracted if x != '']
        points = 0
        win_count = 0
        for win_n in winning:
            if win_n in extracted:
                win_count += 1
        if win_count == 0:
            points = 0
        elif win_count > 0:
            points = pow(2, win_count - 1)
        result += points
    return result
            
print('Solution n°4: ', get_points(lines))


            