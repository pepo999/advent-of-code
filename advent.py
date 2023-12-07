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
        if values[0] == 5:
            counted.append((counter, 'Five of a kind', int(bet)))
        if values[0] == 4:
            counted.append((counter, 'Four of a kind', int(bet)))
        if values[0] == 3 and values[1] == 2:
            counted.append((counter, 'Full house', int(bet)))
        if values[0] == 3 and values[1] == 1:
            counted.append((counter, 'Three of a kind', int(bet)))
        if values[0] == 2 and values[1] == 2:
            counted.append((counter, 'Two pair', int(bet)))
        if values[0] == 2 and values[1] == 1:
            counted.append((counter, 'One pair', int(bet)))
        if values[0] == 1:
            counted.append((counter, 'High card', int(bet)))
    sorted_values = sorted(counted, key=lambda x: order_cards.index(x[0].most_common()[0][0]))
    sorted_hands = sorted(sorted_values, key=lambda x : order_hand.index(x[1]))
    return sorted_hands

sorted_counted = sort_and_count(lines)
        
def total_winnings(data):
    total_win = 0
    for index, tup in enumerate(data):
        total_win += ((index + 1) * tup[2])
    return total_win

print('Solution n°7: ', total_winnings(sorted_counted))

# 248113761

        
    

        
        




    



            