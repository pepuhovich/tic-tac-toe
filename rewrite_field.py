from print_field import line_0, line_1, line_2

def rewrite_field(line_number, column_number, round_number):
    if round_number % 2 != 1:
        player = 'X'
    elif round_number % 2 == 1:
        player = 'O'
    
    if line_number == 0:
        if column_number == 0 or 1 or 2:
            line_0[column_number+1][1] = player
    elif line_number == 1:
        if column_number == 0 or 1 or 2:
            line_1[column_number+1][1] = player
    elif line_number == 2:
        if column_number == 0 or 1 or 2:
            line_2[column_number+1][1] = player
    return