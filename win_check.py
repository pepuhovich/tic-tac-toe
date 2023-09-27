from print_field import line_0, line_1, line_2

def winner_checker():
    #
    #HORIZONTAL WIN
    #

    if (line_0[1][1], line_0[2][1], line_0[3][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[1][1], line_0[2][1], line_0[3][1]) == ("O", "O", "O"):
        return "O"

    if (line_1[1][1],line_1[2][1], line_1[3][1]) == ("X", "X", "X"):
        return "X"
    elif (line_1[1][1], line_1[2][1], line_1[3][1]) == ("O", "O", "O"):
        return "O"

    if (line_2[1][1], line_2[2][1], line_2[3][1]) == ("X", "X", "X"):
        return "X"
    elif (line_2[1][1], line_2[2][1], line_2[3][1]) == ("O", "O", "O"):
        return "O"
    #
    #VERTICAL WIN
    #

    if (line_0[1][1], line_1[1][1], line_2[1][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[1][1], line_1[1][1], line_2[1][1]) == ("O", "O", "O"):
        return "O"

    if (line_0[2][1], line_1[2][1], line_2[2][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[2][1], line_1[2][1], line_2[2][1]) == ("O", "O", "O"):
        return "O"

    if (line_0[3][1], line_1[3][1], line_2[3][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[3][1], line_1[3][1], line_2[3][1]) == ("O", "O", "O"):
        return "O"

    #
    #CROSS WIN
    #

    if (line_0[1][1], line_1[2][1], line_2[3][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[1][1], line_1[2][1], line_2[3][1]) == ("O", "O", "O"):
        return "O"
    if (line_0[3][1], line_1[2][1], line_2[1][1]) == ("X", "X", "X"):
        return "X"
    elif (line_0[3][1], line_1[2][1], line_2[1][1]) == ("O", "O", "O"):
        return "O"