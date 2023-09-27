from win_check import winner_checker
from print_field import line_top, line_0, line_1, line_2, print_all_lines
from rewrite_field import rewrite_field
from inputs import get_horizontal_input, get_vertical_input, check_occupancy

while True:
    line_top
    line_0
    line_1
    line_2

    round = 0
    while True:
        
        if round == 0:
            print("⎹‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾⎸\n⎹  MY TIC TAC TOE   ⎸\n⎹ by Peter Puhovich ⎸\n⎹___________________⎸", '\n')
        while round <9:
            round +=1
            print_all_lines()
            
            print('⎹‾‾‾‾‾‾‾‾‾‾‾⎸\n⎹ ROUND: ', round,'⎸', '\n⎹___________⎸', '\n')
            while True:
                try:

                    if round % 2 != 1:
                        horizontal_coordinate = get_horizontal_input('X,')
                    if round % 2 == 1:
                        horizontal_coordinate = get_horizontal_input('O,')
                                
                    if horizontal_coordinate == 0 or horizontal_coordinate == 1 or horizontal_coordinate == 2:
                        while True:
                            try:
                                vertical_coordinate = get_vertical_input()
                                if vertical_coordinate == 0 or vertical_coordinate == 1 or vertical_coordinate == 2:
                                    if check_occupancy(horizontal_coordinate,vertical_coordinate+1):
                                        rewrite_field(horizontal_coordinate,vertical_coordinate,round)
                                        break
                                    else:
                                        print("Field that you selected is already TAKEN. Select another.")
                                        round-=1
                                        break
                                else:
                                    print("You entered too low or too high number!")
                            except ValueError:
                                print("Invalid entry. Enter only INTEGER")
                        break
                    else:
                        print("You entered too low or too high number!")
                except ValueError:
                    print("Invalid entry. Enter only INTEGER")
           
            if winner_checker() == "X" or winner_checker() == "O":
                print_all_lines()
                print('THE WINNER IS PLAYER',winner_checker())
                break
            elif winner_checker() != "X" and winner_checker() != "O" and round == 9:
                print_all_lines()
                print('THE RESULT IS EQUAL')
                break
        break

    while True:
        answer = str(input("Do you want to play again? (y/n)"))
        if answer != 'y' and answer != 'n':
            print("Wrong answer")
            
        elif answer == 'y' or answer == 'n':
            break
                
    if answer == 'y':
        continue
    elif answer == 'n':
        print('THANKS FOR PLAYING, GOODBYE!')
        break
