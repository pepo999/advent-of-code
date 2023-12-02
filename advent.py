###############################
# 1

tups = [
        (1, 'one'),
        (2, 'two'),
        (3, 'three'),
        (4, 'four'),
        (5, 'five'),
        (6, 'six'),
        (7, 'seven'),
        (8, 'eight'),
        (9, 'nine')
          ]
          

lines = []
with open('data/input_1.txt') as f: 
    for _ in f:
        lines.append(_)
        
def get_first_get_last(lines):
    nums = []
    for line in lines:
        first = ''
        last = ''
        int_first = get_digit(line)
        int_last = get_digit(line[::-1])
        num = str(int_first) + str(int_last)
        nums.append(int(num))
    return sum(nums)
        
def get_digit(line):
    for char in line:
        if char.isdigit():
            return char
    return '', -1
    
print(get_first_get_last(lines))

###############################
# 2



            