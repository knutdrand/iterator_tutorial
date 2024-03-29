from itertools import groupby, accumulate, product, dropwhile
# builtins max, map, filter

def map_example(sequences):
    # return map(lambda x: len(
    return [len(sequence) for sequence in sequences]

def filter_example(sequences):
    return filter(lambda x: len(x) > 5, sequences)

def max_of_function(binary_func):
    return max(binary_func(x, y) for x, y in product(range(100), repeat=2))


    # max_value = None
    # 
    # for x in range(100):
    #     for y in range(100):
    #         val = binary_func(x, y)
    #         if max_value is None:
    #             max_value = val
    #         else:
    #             max_value = max(val, max_value)
    # 
    # return max_value

def longest_repeat(sequence):
    "aaaccccttgga"

    return max(len(list(values)) for char, values in groupby(sequence))

    #  cur_char = None
    #  cur_len = 0
    #  max_len = -1
    #  for char in sequence:
    #      if char == cur_char:
    #          cur_len+=1
    #      else:
    #          max_len = max(max_len, cur_len)
    #          cur_len = 1
    #          cur_char = char
    #  
    #  return max(max_len, cur_len)

def location_from_steps(steps, start=0):
    ret = list(accumulate(steps, initial=start))
    print(steps)
    print(ret)
    return accumulate(steps, initial=start)


    # locations = [start]
    # for step in steps:
    #     locations.append(locations[-1]+step)
    # return locations

def read_numbers(lines):
    numbers = []
    for line in lines:
        if not line.startswith("#"):
            numbers.append(int(line))
    return numbers
     
