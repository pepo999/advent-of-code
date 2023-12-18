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
with open('data/input_18_x.txt') as f: 
    for _ in f:
        lines.append(_.replace('\n', '')) 
        
# lines = [
#         'R 6 (#70c710)',
#         'D 5 (#0dc571)',
#         'L 2 (#5713f0)',
#         'D 2 (#d2c081)',
#         'R 2 (#59c680)',
#         'D 2 (#411b91)',
#         'L 5 (#8ceee2)',
#         'U 2 (#caa173)',
#         'L 1 (#1b58a2)',
#         'U 2 (#caa171)',
#         'R 2 (#7807d2)',
#         'U 3 (#a77fa3)',
#         'L 2 (#015232)',
#         'U 2 (#7a21e3)'
#         ]

def clean_split(lines):
    cleaned = []
    for line in lines:
        line = line.split(' ')
        line[1] = int(line[1])
        cleaned.append(line)
    return cleaned

lines = clean_split(lines)

# def flood_fill(line):
#     hash_indexes = [i for i, char in enumerate(line) if char == '#']
#     valid_indexes = [x for x in hash_indexes if x + 1 not in hash_indexes or x - 1 not in hash_indexes]
#     print('original', hash_indexes, 'valid indexes', valid_indexes)
#     splitted_line = ['!']
#     splitted_line += list(line)
#     splitted_line.append('!')
#     result = []
#     for i in range(0, len(valid_indexes), 2):
#         if i + 1 < len(valid_indexes):
#             result.append((valid_indexes[i], valid_indexes[i + 1]))
#         else:
#             result.append((valid_indexes[i], len(line)))
#     for tup in result:
#         for i in range(tup[0], tup[1]):
#             valid_indexes.append(i)
#     valid_indexes = []
#     hash_indexes += valid_indexes
#     splitted_line = [x for x in splitted_line if x != '!']
#     for index in hash_indexes:
#         splitted_line[index] = '#'
#     print('after', sorted(list(set(hash_indexes))))
#     return ''.join(splitted_line)

def flood_fill(line):
    splitted_line = ['!']
    splitted_line += list(line)
    splitted_line.append('!')
    valid_indexes = []
    for i, char in enumerate(line):
        between = False
        # if (splitted_line[i -1] == '.' and splitted_line[ i + 2] == '.' and char == '#'):
        #     valid_indexes.append(i)
        if (splitted_line[i - 1] == '.' or splitted_line[i + 2] == '.' or splitted_line[i - 1] == '!' or splitted_line[i +2] == '!') and char == '#':
            valid_indexes.append(i)
    print(line, '|', valid_indexes[:10], '...')
            

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
    filled_table = []
    for line in table:
        filled_table.append(flood_fill(line))
    return filled_table

table = draw_g(lines)

for line in table:
    print(line)

count = 0
for line in table:
    for char in line:
        if char == '#':
            count += 1

# 50746            
print('Solution n°18: ', count)


        
        
            
    