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

#####
# 5 #
#####

lines = []
with open('data/input_5.txt') as f: 
    for _ in f:
        lines.append(_)

seeds = [x for x in lines if 'seeds' in x]
seeds = seeds[0].replace('seeds: ', '').split(' ')
seeds = [int(x.strip()) for x in seeds]

def clean_split(lines):
    lines_cleaned = []
    current_label = None
    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            current_label = line[:-1]
        else:
            if line != '':
                lines_cleaned.append((line, current_label))
    return [(data, label) for data, label in lines_cleaned if not data[0].isalpha() and not data[0].isspace()]
                
lines = clean_split(lines) 

s_to_l = []
s_to_f = []
f_to_w = []
w_to_l = []
l_to_t = []
t_to_h = []
h_to_l = []

for line in lines:
    if line[1] == 'seed-to-soil map':
        s_to_l.append(line[0])
    if line[1] == 'soil-to-fertilizer map':
        s_to_f.append(line[0])
    if line[1] == 'fertilizer-to-water map':
        f_to_w.append(line[0])
    if line[1] == 'water-to-light map':
        w_to_l.append(line[0])
    if line[1] == 'light-to-temperature map':
        l_to_t.append(line[0])
    if line[1] == 'temperature-to-humidity map':
        t_to_h.append(line[0])    
    if line[1] == 'humidity-to-location map':
        h_to_l.append(line[0]) 

steps = [
        s_to_l,
        s_to_f,
        f_to_w,
        w_to_l,
        l_to_t,
        t_to_h,
        h_to_l
        ]

def through_steps(seed, step):
    for line in step:
        splitted_step = line.split(' ')
        splitted_ints = [int(x) for x in splitted_step]
        d = splitted_ints[0]
        s = splitted_ints[1]
        r = splitted_ints[2]
        if s <= seed < s + r:
            seed = seed - s + d
            return seed
    return seed

def seed_to_loc(seed):
        for step in steps:
            seed = through_steps(seed, step)
        return seed

def min_loc(seeds):
    locs = []
    for seed in seeds:
        loc = seed_to_loc(seed)
        locs.append(loc)
    return min(locs)

print('Solution n°5: ', min_loc(seeds))

#####
# 6 #
#####

lines = []
with open('data/input_6.txt') as f: 
    for _ in f:
        lines.append(_)

times = []
distances = []
for line in lines:
    if line.startswith('Time:'):
        line = line.replace('Time:', '')
        nums = line.split(' ')
        nums = [x for x in nums if x != ' ' and x != '']
        for num in nums:
            times.append(int(num))
    if line.startswith('Distance:'):
        line = line.replace('Distance:', '')
        nums = line.split(' ')
        nums = [x for x in nums if x != ' ' and x != '']
        for num in nums:
            distances.append(int(num))
         
def winning_count_mult(times, distances):
    winning_count = 1
    for time, distance in zip(times, distances):
        winning_push_list = []
        push_t = 0
        while push_t <= time:
            dist = push_t * (time - push_t)
            if dist > distance:
                winning_push_list.append(dist)
            push_t += 1
        winning_count *= len(winning_push_list)
    return winning_count
        
print('Solution n°6: ', winning_count_mult(times, distances))

#####
# 7 #
#####

from collections import Counter

lines = []
with open('data/input_7.txt') as f: 
    for _ in f:
        lines.append(_)
        
# lines = [
# '32T3K 765',
# 'T55J5 684',
# 'KK677 28',
# 'KTJJT 220',
# 'QQQJA 483'
# ]

order_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order_hand = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card']

def sort_and_count(lines):
    counted = []
    for line in lines:
        hand = line.split(' ')[0]
        bet = line.split(' ')[1]
        counter = Counter(hand)
        count = counter.values()
        values = []
        for value in count:
            values.append(value)
        values = sorted(values, key= lambda x : x, reverse=True)
        hand_values = []
        for v in hand:
            if v == '2':
                hand_values.append(1)
            if v == '3':
                hand_values.append(2)
            if v == '4':
                hand_values.append(3)
            if v == '5':
                hand_values.append(4)
            if v == '6':
                hand_values.append(5)
            if v == '7':
                hand_values.append(6)
            if v == '8':
                hand_values.append(7)
            if v == '9':
                hand_values.append(8)
            if v == 'T':
                hand_values.append(9)
            if v == 'J':
                hand_values.append(10)
            if v == 'Q':
                hand_values.append(11)
            if v == 'K':
                hand_values.append(12)
            if v == 'A':
                hand_values.append(13)
        if values[0] == 5:
            counted.append((counter, 'Five of a kind', int(bet), hand_values))
        if values[0] == 4:
            counted.append((counter, 'Four of a kind', int(bet), hand_values))
        if values[0] == 3 and values[1] == 2:
            counted.append((counter, 'Full house', int(bet), hand_values))
        if values[0] == 3 and values[1] == 1:
            counted.append((counter, 'Three of a kind', int(bet), hand_values))
        if values[0] == 2 and values[1] == 2:
            counted.append((counter, 'Two pair', int(bet), hand_values))
        if values[0] == 2 and values[1] == 1:
            counted.append((counter, 'One pair', int(bet), hand_values))
        if values[0] == 1:
            counted.append((counter, 'High card', int(bet), hand_values))
    sorted_hands = sorted(counted, key=lambda x: (x[3][0], x[3][1], x[3][2], x[3][3], x[3][4]), reverse=True)
    sorted_data = sorted(sorted_hands, key=lambda x : order_hand.index(x[1]))
    # for _ in sorted_data:
    #     print(_[1], _[3])
    return sorted_data
        
def total_winnings(data):
    total_win = 0
    for index, tup in enumerate(data):
        total_win += ((index + 1) * tup[2])
    return total_win

def get_total_winnings(lines):
    sorted_counted = sort_and_count(lines)
    tot_win = total_winnings(sorted_counted)
    return tot_win
    
print('Solution n°7: ', get_total_winnings(lines))

# 248113761

#####
# 8 #
#####

import sys

sys.setrecursionlimit(25000)

lines = []
with open('data/input_8.txt') as f: 
    for _ in f:
        lines.append(_)

def clean_split(lines):
    instruct = lines[0]
    tups = []
    for line in lines[1:]:
        if line != '' and line != ' ':
            name = line[:3]
            l = line[7:10]
            r = line[12:15]
            tups.append((name, l, r))
    return instruct, tups
        
instr, tups = clean_split(lines) 

begin = [x for x in tups if x[0] == 'AAA'][0]
step = 0

def steps_to_zzz(begin, step, index_instr):
    i = instr[index_instr]
    if begin[0] == 'ZZZ':
        return step
    l = begin[1]
    r = begin[2]
    if i == 'L':
        begin = [x for x in tups if x[0] == l][0]
    if i == 'R':
        begin = [x for x in tups if x[0] == r][0]
    step += 1
    index_instr += 1
    if index_instr == len(instr):
        index_instr = 0
        step -= 1
    return steps_to_zzz(begin, step, index_instr) 

print('Solution n°8: ', steps_to_zzz(begin, 0, 0)) 

#####
# 9 #
#####

lines = []
with open('data/input_9.txt') as f: 
    for _ in f:
        lines.append(_)

def clean(lines):
    line_values = []
    for line in lines:
        values = []
        splitted = line.split(' ')
        for split in splitted:
            values.append(int(split))
        line_values.append(values)
    return line_values

values = clean(lines)

def get_diff(line_values, list_diffs = []):
    diffs = []
    for index, value in enumerate(line_values):
        if index + 1 == len(line_values):
            break
        else:
            diff = value - line_values[index + 1]
            diffs.append(diff * -1)
    if all(value == 0 for value in diffs): 
        list_diffs.append(diffs)
        return list_diffs
    else:
        list_diffs.append(diffs)
        return get_diff(diffs, list_diffs)

def get_next_val(values):  
    next_values = []
    for line_values in values:
        next_val = line_values[-1]
        diffs = get_diff(line_values, [])
        diffs = list(reversed(diffs))
        result_sum = sum(sublist[-1] for sublist in diffs)
        next_values.append(next_val + result_sum)
    return next_values

print('Solution n°9: ', sum(get_next_val(values)))
            
            
        
    


        
    
    
        
            
        

        
    

        
        




    



            