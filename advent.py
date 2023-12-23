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
    
print('Solution n° 1: ', get_first_get_last(lines))

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
                 
print('Solution n° 2: ', get_id_sum(lines))

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
        
print('Solution n° 3: ', nums_near_symb(lines))

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
            
print('Solution n° 4: ', get_points(lines))

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

print('Solution n° 5: ', min_loc(seeds))

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
        
print('Solution n° 6: ', winning_count_mult(times, distances))

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
        bet = line.split(' ')[1].replace('\n', '')
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
    sorted_hands = sorted(counted, key=lambda x: (x[3][0], x[3][1], x[3][2], x[3][3], x[3][4]))
    sorted_data = sorted(sorted_hands, key=lambda x : order_hand.index(x[1]), reverse=True)
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
    
print('Solution n° 7: ', get_total_winnings(lines))

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

print('Solution n° 8: ', steps_to_zzz(begin, 0, 0)) 

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

def get_next_vals(values):  
    next_values = []
    for line_values in values:
        next_val = line_values[-1]
        diffs = get_diff(line_values, [])
        diffs = list(reversed(diffs))
        result_sum = sum(sublist[-1] for sublist in diffs)
        next_values.append(next_val + result_sum)
    return next_values

print('Solution n° 9: ', sum(get_next_vals(values)))

######
# 10 #
######

lines = []
with open('data/input_10.txt') as f: 
    for _ in f:
        lines.append(_)

start = 'S'
start_coord = tuple()
for index_y, line in enumerate(lines):
    for index_x, letter in enumerate(line):
        if letter == start:
            start_coord = (index_x, index_y)

directions = ['up', 'down', 'left', 'right']

def move(x, y, steps = []):
    char = lines[y][x]
    connections = []
    steps.append((x, y))
    for direction in directions:
        up, down, left, right = '.', '.', '.', '.'
        if y - 1 >= 0:
            up = lines[y - 1][x]
        if y + 1 < len(lines):
            down = lines[y + 1][x]
        if x + 1 < len(lines[0]):
            right = lines[y][x + 1]
        if x - 1 >= 0:
            left = lines[y][x - 1]
        if direction == 'up' and (up == '|' or up == '7' or up == 'F' or up == 'S') and (char == '|' or char == 'L' or char == 'J' or char =='S'):
            connections.append((x, y - 1, up))
        if direction == 'down' and (down == '|' or down == 'L' or down == 'J' or down == 'S') and (char == '|' or char == '7' or char == 'F' or char =='S'):
            connections.append((x, y + 1, down))
        if direction == 'left' and (left == '-' or left == 'F' or left == 'L' or left == 'S') and (char == '-' or char == 'J' or char == '7' or char =='S'):
            connections.append((x - 1, y, left))
        if direction == 'right' and (right == '-' or right == '7' or right == 'J' or right == 'S') and (char == '-' or char == 'L' or char =='F' or char =='S'):
            connections.append((x + 1, y, right))
    if len(connections) == 2:
        for connection in connections:
            if (connection[0], connection[1]) not in steps: 
                return move(connection[0], connection[1], steps)
    return len(steps) // 2
             
# print('Solution n°10: ', move(start_coord[0], start_coord[1]))
print('Solution n°10:  6714')

######
# 11 #
######

lines = []
with open('data/input_11.txt') as f: 
    for _ in f:
        lines.append(_)

def expanded(lines):
    expanded = []
    for line in lines:
        if any(x == '#' for x in line): 
            expanded.append(line)
        else:
            expanded.append(line)
            expanded.append(line)             
    return expanded

def sub_nums(map):
    sub_map = []
    num = 1
    nums = []
    for line in map:
        new_line = ''
        for x in line:
            if x == '#':
                new_line += str(num)
                nums.append(num)
                num += 1  
            if x == '.':
                new_line += '.'
        sub_map.append(new_line)
    return sub_map, nums

def pair_nums(nums):
    pairs = []
    for num in nums:
        num = str(num)
        for i in range(len(nums)):
            i += 1
            i = str(i)
            if i != num and ((i, num) not in pairs) and ((num, i) not in pairs):
                pairs.append((num, i))
    return pairs

def find_coordinates(map, num):
    num_str = str(num)
    num_len = len(num_str)
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if line[j : j + num_len] == num_str:
                x_to_sub = numbers_b4_in_line(line, j)
                j -= x_to_sub
                return i, j
            
def numbers_b4_in_line(line, x_coord):
    position = 0
    count = 0
    while position < x_coord:
        if x_coord < len(line):
            if line[position].isdigit() and line[position + 1].isdigit() and line[position + 2].isdigit():
                count += 2
                position += 2
            elif line[position].isdigit() and line[position + 1].isdigit():
                count += 1
                position += 1
            else:
                position += 1
    return count
            
def shortest_path_between_pairs(map, pair):
    start, end = pair 
    start_coords = find_coordinates(map, start)
    end_coords = find_coordinates(map, end)
    start_y, start_x = start_coords
    end_y, end_x = end_coords
    distance = abs(start_x - end_x) + abs(start_y - end_y)
    return distance

def get_sum_distances(lines):
    expanded_x = expanded(lines)
    inverted_map = [''.join(row[i] for row in expanded_x) for i in range(len(expanded_x[0]))]
    expanded_y = expanded(inverted_map)
    expanded_map = [''.join(row[i] for row in expanded_y) for i in range(len(expanded_y[0]))]
    sub_map, nums = sub_nums(expanded_map)
    pairs = pair_nums(nums)
    paths_len = []    
    for pair in pairs:
        distance = shortest_path_between_pairs(sub_map, pair)
        paths_len.append(distance)
    return sum(paths_len)

# print('Solution n°11: ', get_sum_distances(lines))
print('Solution n°11:  9329143')

######
# 12 #
######

from itertools import product

lines = []
with open('data/input_12.txt') as f: 
    for _ in f:
        lines.append(_)

def clean(lines):
    puzzs = []
    instructions = []
    for line in lines:
        line_instr = []
        chars = line.split(' ')[0]
        instr = line.split(' ')[1]
        puzzs.append('.' + chars + '.')
        blocks = instr.split(',')
        for block in blocks:
            transf = '.' + ('#' * int(block)) + '.'
            line_instr.append(transf)
        instructions.append(line_instr)
    return puzzs, instructions

def possible_lines(input_string):
    possible_values = ['.', '#']
    combinations = product(possible_values, repeat=input_string.count('?'))
    result_strings = []
    for combination in combinations:
        result = ''
        for char in input_string:
            if char == '?':
                result += combination[0]
                combination = combination[1:] + combination[:1]
            else:
                result += char
        result_strings.append(result)
    return result_strings

def check_order(input_string, blocks_list):
    in_str = []
    nu_block = ''
    for i, char in enumerate(input_string):
        if char == '#':
            nu_block += char
        elif nu_block:
            in_str.append(nu_block)
            nu_block = ''
    if nu_block:
        in_str.append(nu_block)
    blocks_list = [block[1:-1] for block in blocks_list]
    return in_str == blocks_list

def perms(lines):
    puzzs, instructions = clean(lines)
    counts = []
    for puzz, instr in zip(puzzs, instructions):
        possible_combs = possible_lines(puzz)
        count = 0
        for poss in possible_combs:
            og_poss = poss
            poss_count = 0
            for inst in instr:
                if inst in poss:
                    poss_count += 1 
                    index = poss.find(inst)
                    poss = poss[:index + 1] + poss[index + len(inst):]              
            if poss_count == len(instr) and (og_poss.count('#') == ''.join(instr).count('#')):
                ordered = check_order(og_poss, instr)  
                if ordered:
                    count += 1
        counts.append(count)
    return counts
        
# print('Solution n°12: ', sum(perms(lines)))
print('Solution n°12:  7251')

######
# 13 #
######

lines = []
with open('data/input_13.txt') as f: 
    for _ in f:
        lines.append(_)

def split_in_blocks(lines):
    empty_line_indices = [i for i, line in enumerate(lines) if not line.strip()]
    blocks = [lines[i:j] for i, j in zip([0] + empty_line_indices, empty_line_indices + [None]) if i != j]
    cleaned = [[line.replace('\n', '') for line in block if line.strip()] for block in blocks]
    return cleaned
        
blocks = split_in_blocks(lines)

def find_symm(block, axis):
    ress = []
    if axis == 'x':
        transposed_block = list(zip(*block))
        block = [''.join(row[::-1]) for row in transposed_block]
    len_b = len(block)
    for i in range(1, len_b):
        lines_before = []
        lines_after = []
        for j in range(i, 0, -1):
            lines_before.append(block[j - 1])
        for k in range(i, len_b):
            lines_after.append(block[k])
        equal_lines = []
        for before, after in zip(lines_before, lines_after):
            if before == after:
                equal_lines.append(before)
            if before != after:
                break
        if equal_lines != [] and ( i - len(equal_lines) <= 0 or (i + len(equal_lines)) >= len_b):
            if axis == 'x':
                res = i
                ress.append(res)
            if axis == 'y':
                res = i * 100
                ress.append(res)
    if ress != []:
        return sum(ress)

def get_result(blocks):
    res = []
    for block in blocks:
        res_x = find_symm(block, 'x')
        res_x__y = []
        if res_x:
            res_x__y.append(res_x) 
        res_y = find_symm(block, 'y')
        if res_y:
            res_x__y.append(res_y)
        res.append(sum(res_x__y))
    return sum(res)
    
print('Solution n°13: ', get_result(blocks)) 

######
# 14 #
######

lines = []
with open('data/input_14.txt') as f: 
    for _ in f:
        lines.append(_) 

def create_line(info):
    line = ['.'] * info['len_line']
    for hash_index in info['hash']:
        line[hash_index] = '#'
    for dot_block in info['dots']:
        for dot_index in dot_block:
            line[dot_index] = 'O'
    return ''.join(line) 
    
def move_circs(lines):
    turned_mat = list(zip(*lines))
    turned_mat = [''.join(row[::-1]) for row in turned_mat]
    moved = []
    for index, line in enumerate(turned_mat):
        indexes = {"line_index": index, "len_line": len(line), "dots": [], "hash": []}
        for k, char in enumerate(line):
            if char == 'O':
                indexes['dots'].append(k)
            if char == '#':
                indexes['hash'].append(k)
        indexes['hash'].append(len(line))
        splitted_dots = []
        prev_hash = -1
        for h in indexes['hash']:
            dot_block = [o for o in indexes['dots'] if prev_hash < o < h]
            splitted_dots.append(dot_block)
            prev_hash = h
        dot_block = [o for o in indexes['dots'] if o > prev_hash]
        splitted_dots.append(dot_block)
        splitted_dots = [dot_block for dot_block in splitted_dots[:-1]]
        moved_dots = []
        for dot_block, hash_idx in zip(splitted_dots, indexes['hash']):
            moved_dots.append([i for i in range(hash_idx -1, hash_idx - len(dot_block) - 1, -1)])
        moved_dots = [x for x in moved_dots if x != []]    
        indexes['dots'] = moved_dots
        indexes['hash'] = indexes['hash'][:-1]
        nu_line = create_line(indexes)
        moved.append(nu_line)
    turned_back = list(zip(*moved))
    turned_back = [''.join(row) for row in reversed(turned_back)]
    return turned_back
    
def count_points(lines):
    points = 0
    for index, line in enumerate(lines[::-1]):
        dot_count = 0
        for char in line:
            if char == 'O':
                dot_count += 1
        points += dot_count * (index + 1)
    return points
    
moved = move_circs(lines)

print('Solution n°14: ', count_points(moved))

######
# 15 #
######

lines = ''
with open('data/input_15.txt') as f: 
    for _ in f:
        lines += _
    
lines = lines.split(',')

def get_value(char, current_val):
    current_val += ord(char)
    current_val *= 17
    current_val = current_val % 256
    return current_val

def get_block_hash(block):
    res = 0
    for char in block:
        res = get_value(char, res)
    return res

def get_values(lines):
    res = 0
    for block in lines:
        block = block.replace('\n', '')
        hash = get_block_hash(block)
        res += hash
    return res

print('Solution n°15: ', get_values(lines))

######
# 16 #
######

import time
import os

lines = []
with open('data/input_16.txt') as f: 
    for _ in f:
        lines.append(_.replace('\n', '')) 

def print_steps(steps, lines):
    len_x = len(lines[0])
    len_y = len(lines)
    final_grid = [['.' for _ in range(len_x)] for _ in range(len_y)]
    for step in steps:
        x, y = step[0]
        final_grid[y][x] = '#'
    for row, line in zip(final_grid, lines):
        # print(''.join(row), '    ', line)
        print(''.join(row))
    time.sleep(0.1)
    os.system('clear' if os.name == 'posix' else 'cls')
    
directions = [(1, 0, 'r'), (0, 1, 'd'), (-1, 0, 'l'), (0, -1, 'u')]
        
def move_beam(position=(-1, 0), direction=(1, 0, 'r'), steps=[]):
    steps.append((position, direction[2]))
    # print_steps(steps, lines)
    if position[0] + direction[0] >= len(lines[0]) or position[0] + direction[0] < 0:
        return steps
    if position[1] + direction[1] >= len(lines) or position[1] + direction[1] < 0:
        return steps
    position = (position[0] + direction[0], position[1] + direction[1])
    if (position, direction[2]) in steps:
        return steps
    next_pos = lines[position[1]][position[0]]
    if next_pos == '.':
        same_dir = [x for x in directions if x[2] == direction[2]][0]
        steps += move_beam(position, same_dir, steps.copy())
    elif next_pos == '-' and (direction[2] == 'r' or direction[2] == 'l'):
        same_dir = [x for x in directions if x[2] == direction[2]][0]
        steps += move_beam(position, same_dir, steps.copy())
    elif next_pos == '-' and (direction[2] == 'u' or direction[2] =='d'):
        a = move_beam(position, directions[0], steps.copy())
        b = move_beam(position, directions[2], steps.copy())
        steps += a + b
    elif next_pos == '|' and (direction[2] == 'u' or direction[2] == 'd'):
        same_dir = [x for x in directions if x[2] == direction[2]][0]
        steps += move_beam(position, same_dir, steps.copy())
    elif next_pos == '|' and (direction[2] == 'l' or direction[2] == 'r'):
        a = move_beam(position, directions[3], steps.copy())
        b = move_beam(position, directions[1], steps.copy())
        steps += a + b
    elif next_pos == '\\' and direction[2] == 'r':
        steps += move_beam(position, directions[1], steps.copy())
    elif next_pos == '\\' and direction[2] == 'l':
        steps += move_beam(position, directions[3], steps.copy())
    elif next_pos == '\\' and direction[2] == 'u':
        steps += move_beam(position, directions[2], steps.copy())
    elif next_pos == '\\' and direction[2] == 'd':
        steps += move_beam(position, directions[0], steps.copy())
    elif next_pos == '/' and direction[2] == 'r':
        steps += move_beam(position, directions[3], steps.copy())
    elif next_pos == '/' and direction[2] == 'l':
        steps += move_beam(position, directions[1], steps.copy())
    elif next_pos == '/' and direction[2] == 'u':
        steps += move_beam(position, directions[0], steps.copy())
    elif next_pos == '/' and direction[2] == 'd':
        steps += move_beam(position, directions[2], steps.copy())
    return steps

def count_energized(lines):
    count = 0
    steps = move_beam()
    len_x = len(lines[0])
    len_y = len(lines)
    final_grid = [['.' for _ in range(len_x)] for _ in range(len_y)]
    for step in steps:
        x, y = step[0]
        final_grid[y][x] = '#'
    for row in final_grid:
        for char in row:
            if char == '#':
                count +=1
    return count

# print('Solution n°16: ', count_energized(lines))
print('Solution n°16:  7482')

######
# 17 #
######

lines = []
with open('data/input_17.txt') as f: 
    for _ in f:
        lines.append(_.replace('\n', '')) 
        
lines = [
        '2413432311323',
        '3215453535623',
        '3255245654254',
        '3446585845452',
        '4546657867536',
        '1438598798454',
        '4457876987766',
        '3637877979653',
        '4654967986887',
        '4564679986453',
        '1224686865563',
        '2546548887735',
        '4322674655533'
        ]
        
ints = [[[(x, y), int(weight), float('inf'), None] for x, weight in enumerate(line)] for y, line in enumerate(lines)]
ints[0][0][2] = 0

directions = [(1, 0, 'r'), (0, 1, 'd'), (-1, 0, 'l'), (0, -1, 'u')]

def shortest_paths(ints):
    start_coords, weight_start, shortest_start, previous_start = ints[0][0]
    end_coords, weight_end, shortest_end, previous_end = ints[-1][-1]
    hist = []
    for y in ints:
        for x in y:
            current_coords, current_weight, current_shortest, current_prev = x
            for dir in directions:
                next_coords = (current_coords[0] + dir[0], current_coords[1] + dir[1])
                if 0 <= next_coords[0] < len(ints[0]) and 0 <= next_coords[1] < len(ints):
                    next_cell = ints[next_coords[1]][next_coords[0]]
                    new_shortest = current_shortest + next_cell[1]
                    
                    # here insert conditions:
                    # # no more than three steps in the same direction
                    # # never going back
                    if new_shortest < next_cell[2]:
                        hist.append(dir[2])
                        next_cell[2] = new_shortest
                        next_cell[3] = current_coords
    # print('hist', hist, 'len', len(hist))
    return ints

ints = shortest_paths(ints)

def get_path(end_cell, path=None):
    if path is None:
        path = [end_cell]
    if end_cell[3] == (0, 0):
        path.append(end_cell[0])
        return path
    previous_cell_coords = end_cell[3]
    previous_cell = ints[previous_cell_coords[1]][previous_cell_coords[0]]
    path.append(previous_cell)
    return get_path(previous_cell, path)

shortest_path = get_path(ints[-1][-1])
# print(shortest_path)
count = 0
for x in shortest_path:
    # print(x[0])
    count += x[1]
count += ints[-1][-1][1]
# 902

print('Solution n°17: ', count)

######
# 18 #
######

lines = []
with open('data/input_18.txt') as f: 
    for _ in f:
        lines.append(_.replace('\n', '')) 

def clean_split(lines):
    cleaned = []
    for line in lines:
        line = line.split(' ')
        line[1] = int(line[1])
        cleaned.append(line)
    return cleaned

lines = clean_split(lines)

def draw_g(lines):
    x_axis, y_axis = [], []
    x, y = 0, 0
    for line in lines:
        if line[0] == 'R':
            x += line[1]
            x_axis.append(x)
        if line[0] == 'L':
            x -= line[1]
            x_axis.append(x)
        if line[0] == 'D':
            y += line[1]
            y_axis.append(y)
        if line[0] == 'U':
            y -= line[1]
            y_axis.append(y)
    x, y = max(x_axis), max(y_axis)
    start = [0, 0]
    coords = [(0, 0)]
    for line in lines:
        if line[0] == 'R':
            for i in range(1, line[1] + 1):
                start[0] += 1
                coords.append((start[0], start[1]))
        if line[0] == 'L':
            for i in range(1, line[1] + 1):
                start[0] -= 1
                coords.append((start[0], start[1]))
        if line[0] == 'D':
            for i in range(1, line[1] + 1):
                start[1] += 1
                coords.append((start[0], start[1]))
        if line[0] == 'U':
            for i in range(1, line[1] + 1):
                start[1] -= 1
                coords.append((start[0], start[1]))
    min_x = min([x[0] for x in coords]) * -1
    min_y = min([x[1] for x in coords]) * -1
    table = []
    for i in range(y + 1 + min_y):
        line = ''
        for j in range(x + 1 + min_x):
            line += '.'
        table.append(line)
    for coord in coords:
        x, y = coord
        x += min_x
        y += min_y
        table[y] = table[y][:x] + '#' + table[y][x + 1:]
    return table, coords

def fill_flood(table, cell, old, new, print_t):
    x, y = cell
    if old == None:
        old = table[y][x]
    if table[y][x] != old:
         return 
    table[y][x] = new
    if print_t:
        for line in table[len(table) - 185:]:
            print(''.join(line))
        print('\n' * 5)
        sys.stdout.write('\033[H')
        sys.stdout.flush()
    if x + 1 < len(table[0]) - 1:
        fill_flood(table, (x + 1, y), old, new, print_t)
    if y + 1 < len(table) - 1:
        fill_flood(table, (x, y + 1), old, new, print_t)
    if x - 1 > 0:
        fill_flood(table, (x - 1, y), old, new, print_t)
    if y - 1 > 0:
        fill_flood(table, (x, y - 1), old, new, print_t)

table, coords = draw_g(lines)

center = (len(table[0])//2, len(table)//2 + 1)

table = [[x for x in y] for y in table]

# fill_flood(table, center, None, '#', print_t=False)

count = 0
for line in table:
    for char in line:
        if char == '#':
            count += 1
        
# print('Solution n°18: ', count)
print('Solution n°18:  50746')

######
# 19 #
######

workflows = {}
part_ratings = []

with open('data/input_19.txt') as f: 
    parts = False
    for _ in f:
        if _ == '\n':
            parts = True
        if parts and _ != '\n':
            part = _.replace('{', '').replace('}', '').replace('\n', '').split(',')
            part_list = {}
            for block in part:
                block = block.split('=')
                part_list[block[0]] = int(block[1])
            part_ratings.append(part_list)
        elif not parts and _ != '\n':
            _ = _.replace('\n', '')
            name = _.split('{')[0]
            rules = _.split('{')[1].replace('}', '').split(',')
            for i, rule in enumerate(rules):
                if not any([x.isdigit() for x in rule]):
                    rules[i - 1] += f',{rule}'
                    rules.pop(i)
            formatted_rules = []
            for rule in rules:
                rating = re.split('[<>:]', rule)
                operator = '>'
                if '<' in rule:
                    operator = '<'
                formatted_rule = (rating[0], operator, int(rating[1]), ':', rating[2].split(','))
                formatted_rules.append(formatted_rule)    
            workflows[name] = formatted_rules
    
start = [x for x in workflows if 'in' in x]   

def a_or_r(part_rating, work_name='in', res=None):
    xmas = sum(part_rating.values())
    if res == 'A':
        return xmas
    if res == 'R':
        return 'R'
    start = workflows.get(work_name)
    for workflow in start:
        variable, operator, value = workflow[:3]
        variable = part_rating.get(variable)
        do = workflow[4][0]
        el = None
        if len(workflow[4]) > 1:
            el = workflow[4][1]
        condition = None
        if operator == '<':
            condition = variable < value
        elif operator == '>':
            condition = variable > value
        if condition:
            if len(do) >= 2:
                return a_or_r(part_rating, do)
            else:
                return a_or_r(part_rating, do, do)
        if not condition:
            if el:
                if len(el) >= 2:
                    return a_or_r(part_rating, el)
                else:
                    return a_or_r(part_rating, el, el)

def sum_ratings(part_ratings):
    res = 0            
    for part_rating in part_ratings:
        if a_or_r(part_rating) != 'R':
            res += a_or_r(part_rating)
    return res
        
print('Solution n°19: ', sum_ratings(part_ratings))

######
# 20 #
######

formatted_input = []
with open('data/input_20_1.txt') as f:
    for _ in f:
        _ = _.replace('\n', '').split('-> ')
        type_name = _[0]
        cell = []
        if type_name[0] == '%':
            cell = [type_name[1:].strip(), '%', 0, _[1].split(', ')]
        if type_name[0] == '&':
            cell = [type_name[1:].strip(), '&', {}, _[1].split(', ')]
        if 'broadcaster' in type_name:
            cell = ['broadcaster', '', '', _[1].split(', ')]
        formatted_input.append(cell)


def create_memory_conjs():
    conjs = [x for x in formatted_input if x[1] == '&']
    outs = [[x[0], x[3]] for x in formatted_input]
    for conj in conjs:
        for out in outs:
            out_names = out[1]
            for out_name in out_names:
                if conj[0] == out_name:
                    conj[2][out[0]] = 0
            
create_memory_conjs()

tot_pulses = [0, 0]

def current(cell_name, in_signal, started=False):
    cell = [x for x in formatted_input if x[0] == cell_name][0]
    print('curr cell', cell, 'in signal', in_signal)
    print(tot_pulses)
    flip_states = sum([x[2] for x in formatted_input if x[1] == '%'])
    ###### END CONDITIONS
    if started == True and flip_states == 0:
        print('all flips off')
        return
    started = True
    if cell[3][0] not in [x[0] for x in formatted_input]:
        print('escape cell reached')
        return
    ####### SIGNAL PROCESSING
    out_signal = None
    if cell[1] == '%':
        if in_signal == 0:
            if cell[2] == 0:
                out_cells = [x for x in formatted_input if x[0] in cell[3]]
                for out_cell in out_cells:
                    pass
                    out_cell[2] ^= 1
                for out_cell_name in cell[3]:
                    tot_pulses[1] += 1
                    current(out_cell_name, 1, started=True)
            if cell[2] == 1:
                for out_cell_name in cell[3]:
                    tot_pulses[0] += 1
                    current(out_cell_name, 0, started=True)
    if cell[1] == '&':
        signals = cell[2].values()
        signals = list(signals)
        if sum(signals) < len(signals):
            out_signal = 1
        else:
            out_signal = 0
        for out_cell_name in cell[3]:
            out_cell = [x for x in formatted_input if x[0] == out_cell_name][0]
            if out_signal == 0 and out_cell[2] == 0:
                out_cell[2] ^= 1
            tot_pulses[out_signal] += 1
            print(f'current({out_cell_name, {out_signal}})')
            current(out_cell_name, out_signal, started=True)
    if cell[0] == 'broadcaster':
        out_signal = in_signal
        out_cells = [x for x in formatted_input if x[0] in cell[3]]
        for out_cell in out_cells:
            if out_signal == 0 and out_cell[2] == 0:
                out_cell[2] ^= 1
        for out_cell_name in cell[3]: 
            tot_pulses[out_signal] += 1
            current(out_cell_name, out_signal, started=True)

# current('broadcaster', 0)
print('Solution n°20:  -----')

######
# 21 #
######

lines = []
with open('data/input_21.txt') as f:
    for _ in f:
        lines.append(_.replace('\n', ''))
    
def get_coords(char, lines):
    coords = []
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == char:
                coords.append((x, y, char))
    return coords

start_x, start_y, char = get_coords('S', lines)[0]
    
def move(start_x, start_y, steps):
    global plots
    if plots == None:
        plots = {}
        for i in range(-1, steps + 1):
            plots[i + 1] = set()
    plots[steps + 1].add((start_x, start_y))
    if steps <= 0:
        return len(plots[1])
    if start_x - 1 >= 0:
        left = lines[start_y][start_x - 1]
        if left == '.' or left == 'S':
            plots[steps].add((start_x - 1, start_y))
    if start_x + 1 <= len(lines[0]) - 1:
        right = lines[start_y][start_x +1]
        if right == '.' or right == 'S':
            plots[steps].add((start_x + 1, start_y))
    if start_y - 1 >= 0:
        up = lines[start_y - 1][start_x]
        if up == '.' or up == 'S':
            plots[steps].add((start_x, start_y -1))
    if start_y + 1 <= len(lines) - 1:
        down = lines[start_y + 1][start_x]
        if down == '.' or down == 'S':
            plots[steps].add((start_x, start_y + 1))
    for to_visit in plots[steps]:
        move(to_visit[0], to_visit[1], steps - 1) 

plots = None   
# move(start_x, start_y, 64)
# print('Solution n°21: ', len(plots[1]))
print('Solution n°21:  -----')

######
# 22 #
######

import copy

lines = []
max_x = 0
max_y = 0
max_z = 0

with open('data/input_22.txt') as f:
    f = sorted(list(f), key = lambda x : x.replace('\n', '').split(',')[-1])
    for i, _ in enumerate(f, 1):
        _ = _.replace('\n', '').split('~')
        for coord in _:
            coord = coord.split(',')
            if coord[0].isdigit() and int(coord[0]) > max_x:
                max_x = int(coord[0])
            if coord[1].isdigit() and int(coord[1]) > max_y:
                max_y = int(coord[1])
            if coord[2].isdigit() and int(coord[2]) > max_z:
                max_z = int(coord[2])
        x = _[0].split(',')
        y = _[1].split(',')
        x = [int(_) for _ in x]
        y = [int(_) for _ in y]
        lines.append((x, y, str(i)))

front = [['.' for x in range(max_x + 1)] for z in range(max_z + 1)]
side = [['.' for y in range(max_y + 1)] for z in range(max_z + 1)]

front[0] = '-' * len(front[0])
side[0] = '-' * len(side[0])

coords ={}

for line in lines:
    start_front = [line[0][0], line[0][2]]
    end_front = [line[1][0], line[1][2]]
    start_side = [line[0][1], line[0][2]]
    end_side = [line[1][1], line[1][2]]
    char = line[2]
    coords[char +'f'] = []
    coords[char +'s'] = []
    for x in range(start_front[0], end_front[0] + 1):
        for z in range(start_front[1], end_front[1] + 1):
            coords[char + 'f'].append((x, z))
            front[z][x] = '#'
    for y in range(start_side[0], end_side[0] + 1):
        for z in range(start_side[1], end_side[1] + 1):
            coords[char +'s'].append((y, z))
            side[z][y] = '#'
            
front_old = copy.deepcopy(front)
side_old = copy.deepcopy(side)

def fall(brick, id):
    can_fall = False
    coords_f = brick[0]
    coords_s = brick[1]
    min_z = min([x[1] for x in coords_f])
    front_bool = []
    for i in range(len(coords_f)):
        front_bool.append(False)
    for i, coord in enumerate(coords_f):
        if front[min_z - 1][coord[0]] == '.':
            front_bool[i] = True
    side_bool = []
    for i in range(len(coords_s)):
        side_bool.append(False)
    for i, coord in enumerate(coords_s):
        if side[min_z - 1][coord[0]] == '.':
            side_bool[i] = True
    if all(front_bool) == True or all(side_bool) == True:
        can_fall = True
    if can_fall:
        new_coords_f = []
        for coord in coords_f:
            front[coord[1]][coord[0]] = '.'
        for coord in coords_f:
            front[coord[1]- 1][coord[0]] = '#'
            new_coords_f.append((coord[0], coord[1]- 1)) 
        coords[id + 'f'] = new_coords_f 
        new_coords_s = []
        for coord in coords_s:
            side[coord[1]][coord[0]] = '.'
        for coord in coords_s:
            side[coord[1]- 1][coord[0]] = '#'
            new_coords_s.append((coord[0], coord[1]-1))
        coords[id + 's'] = new_coords_s 
    else: 
        return

def gravity(coords_arg): 
    coords_arg_old = copy.deepcopy(coords_arg)            
    for i in range(len(coords_arg)//2):
        i = str(i + 1) 
        coord_f = coords_arg[i + 'f']
        coord_s = coords_arg[i +'s']
        brick = [coord_f, coord_s]
        fall(brick, i)
    if coords_arg_old == coords:
        return
    else:
        gravity(coords)
            
gravity(coords)
gravity(coords)

for line_front, line_side, line_front_old, line_side_old in zip(front[::-1], side[::-1], front_old[::-1], side_old[::-1]):
    print(''.join(line_front), ' | ', ''.join(line_side), ' ||| ', ''.join(line_front_old), ' | ', ''.join(line_side_old))  

# print(coords)
           


    


        

        




        
        
            
    