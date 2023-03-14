from itertools import product

first_line = input().split()
second_line = input().split()
 
output_str = ""

p = list(product(first_line, second_line))
for value in p:
    output_str = f"{output_str}({value[0]}, {value[1]}) "

print(output_str)