from game_field import line_top, line_0, line_1, line_2

def print_one_line(line):
    for item in line:
        print(item[0], end='')
        print(item[1], end='')
        print(item[2], end='')
    print()
    return ''

def print_all_lines():
    print_one_line(line_top)
    print_one_line(line_0)
    print_one_line(line_1)
    print_one_line(line_2)
    print()
    return ''