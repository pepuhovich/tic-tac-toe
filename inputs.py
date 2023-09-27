import sys
from print_field import line_0, line_1, line_2

def get_horizontal_input(player):
    print('Player', player,'please enter coordinates of HORIZONTAL axis:')
    input_number = sys.stdin.readline()
    return int(input_number)

def get_vertical_input():
    print('Now enter coordinates of VERTICAL axis:')
    input_number = sys.stdin.readline()
    return int(input_number)

def check_occupancy(horizontal, vertical):
    if horizontal == 0:
        if line_0[vertical][1] == "_":
            return True
        else:
            return False
    if horizontal == 1:
        if line_1[vertical][1] == "_":
            return True
        else:
            return False
    if horizontal == 2:
        if line_2[vertical][1] == "_":
            return True
        else:
            return False
        