def print_board():
    coord_num = 1
    print("  A  B  C  D  E  F  G  H")
    
    for row in board:
        print(coord_num, row[0], "",row[1], "",row[2], "",row[3], "",row[4], "",row[5], "",row[6], "", row[7], coord_num)
        coord_num += 1
    
    print("  A  B  C  D  E  F  G  H")

def move_convert(move: str) -> int:
    col = move[0]
    if col == "A":
        col = 0
    elif col == "B":
        col = 1
    elif col == "C":
        col = 2
    elif col == "D":
        col = 3
    elif col == "E":
        col = 4
    elif col == "F":
        col = 5
    elif col == "G":
        col = 6
    elif col == "H":
        col = 7
    else:
        return "Error", "Error"
    
    try:
        row = int(move[1]) - 1
        if row < 0 or row > 7:
            return "Error", "Error"
    except ValueError:
        print("yep")
        return "Error", "Error"
    
    return row, col

def move_check(color_ally, color_enemy) -> bool:
    row = 0
    col = -1

    while True:
        col += 1
        if col == 8:
            row += 1
            col = 0
        if row == 8:
            return False

        if board[row][col] != empty: # Is tile is empty?
            continue

        # West
        col_west = col
        first = True
        while True:
            col_west -= 1

            if board[row][col_west] == color_enemy:
                first = False

            elif board[row][col_west] == color_ally and first == False:
                return True

            else:
                break
        
        # East
        col_east = col
        first = True
        while True:
            col_east += 1
            if col_east > 7: # Checks whether the tile is inside the board
                break

            if board[row][col_east] == color_enemy:
                first = False

            elif board[row][col_east] == color_ally and first == False:
                return True

            else:
                break
        
        # North
        row_north = row
        first = True
        while True:
            row_north -= 1
            if row_north < 0: # Checks whether the tile is inside the board
                break

            if board[row_north][col] == color_enemy:
                first = False

            elif board[row_north][col] == color_ally and first == False:
                return True

            else:
                break
        
        # South
        row_south = row
        first = True
        while True:
            row_south += 1
            if row_south > 7: # Checks whether the tile is inside the board
                break

            if board[row_south][col] == color_enemy:
                first = False

            elif board[row_south][col] == color_ally and first == False:
                return True

            else:
                break
        
        # North-West
        row_north = row
        col_west = col
        first = True
        while True:
            col_west -= 1
            row_north -= 1
            if row_north < 0 or col_west < 0: # Checks whether the tile is inside the board
                break

            if board[row_north][col_west] == color_enemy:
                first = False

            elif board[row_north][col_west] == color_ally and first == False:
                return True

            else:
                break

        # North-East
        row_north = row
        col_east = col
        first = True
        while True:
            col_east += 1
            row_north -= 1
            if row_north < 0 or col_east > 7: # Checks whether the tile is inside the board
                break

            if board[row_north][col_east] == color_enemy:
                first = False

            elif board[row_north][col_east] == color_ally and first == False:
                return True

            else:
                break
        
        # South-East
        row_south = row
        col_east = col
        first = True
        while True:
            col_east += 1
            row_south += 1
            if row_south > 7 or col_east > 7: # Checks whether the tile is inside the board
                break

            if board[row_south][col_east] == color_enemy:
                first = False

            elif board[row_south][col_east] == color_ally and first == False:
                return True

            else:
                break
        
        # South-West
        row_south = row
        col_west = col
        first = True
        while True:
            col_west -= 1
            row_south += 1
            if row_south > 7 or col_west < 0: # Checks whether the tile is inside the board
                break

            if board[row_south][col_west] == color_enemy:
                first = False

            elif board[row_south][col_west] == color_ally and first == False:
                return True

            else:
                break

def move_check_and_place(row, col, color_ally, color_enemy):
    # Is is legal move?
    playable = False
    # Is tile is empty?
    if board[row][col] != empty:
        return "Error"

    # West
    col_west = col
    first = True
    while True:
        col_west -= 1
        if col_west < 0: # Checks whether the tile is inside the board
            break

        if board[row][col_west] == color_enemy:
            first = False

        elif board[row][col_west] == color_ally and first == False:
            for i in range(col - col_west):
                board[row][col - i] = color_ally

            playable = True
            break

        else:
            break
    
    # East
    col_east = col
    first = True
    while True:
        col_east += 1
        if col_east > 7: # Checks whether the tile is inside the board
            break

        if board[row][col_east] == color_enemy:
            first = False

        elif board[row][col_east] == color_ally and first == False:
            for i in range(col_east - col):
                board[row][col + i] = color_ally

            playable = True
            break

        else:
            break
    
    # North
    row_north = row
    first = True
    while True:
        row_north -= 1
        if row_north < 0: # Checks whether the tile is inside the board
            break

        if board[row_north][col] == color_enemy:
            first = False

        elif board[row_north][col] == color_ally and first == False:
            for i in range(row - row_north):
                board[row - i][col] = color_ally

            playable = True
            break

        else:
            break
    
    # South
    row_south = row
    first = True
    while True:
        row_south += 1
        if row_south > 7: # Checks whether the tile is inside the board
            break

        if board[row_south][col] == color_enemy:
            first = False

        elif board[row_south][col] == color_ally and first == False:
            for i in range(row_south - row):
                board[row + i][col] = color_ally

            playable = True
            break

        else:
            break
    
    # North-West
    row_north = row
    col_west = col
    first = True
    while True:
        col_west -= 1
        row_north -= 1
        if row_north < 0 or col_west < 0: # Checks whether the tile is inside the board
            break

        if board[row_north][col_west] == color_enemy:
            first = False

        elif board[row_north][col_west] == color_ally and first == False:
            for i in range(row - row_north):
                board[row - i][col - i] = color_ally

            playable = True
            break

        else:
            break

    # North-East
    row_north = row
    col_east = col
    first = True
    while True:
        col_east += 1
        row_north -= 1
        if row_north < 0 or col_east > 7: # Checks whether the tile is inside the board
            break

        if board[row_north][col_east] == color_enemy:
            first = False

        elif board[row_north][col_east] == color_ally and first == False:
            for i in range(row - row_north):
                board[row - i][col + i] = color_ally

            playable = True
            break

        else:
            break
    
    # South-East
    row_south = row
    col_east = col
    first = True
    while True:
        col_east += 1
        row_south += 1
        if row_south > 7 or col_east > 7: # Checks whether the tile is inside the board
            break

        if board[row_south][col_east] == color_enemy:
            first = False

        elif board[row_south][col_east] == color_ally and first == False:
            for i in range(row_south - row):
                board[row + i][col + i] = color_ally

            playable = True
            break

        else:
            break
    
    # South-West
    row_south = row
    col_west = col
    first = True
    while True:
        col_west -= 1
        row_south += 1
        if row_south > 7 or col_west < 0: # Checks whether the tile is inside the board
            break

        if board[row_south][col_west] == color_enemy:
            first = False

        elif board[row_south][col_west] == color_ally and first == False:
            for i in range(row_south - row):
                board[row + i][col - i] = color_ally

            playable = True
            break

        else:
            break
    
    if playable == False:
        return "Error"

def move_input(color_ally, color_enemy):
    if move_check(color_ally, color_enemy) == False:
        print(f"{color[color_ally]} is out of moves!")
        return color_enemy

    elif move_check(color_ally, color_enemy) == True:
        while True:
            move = input(f"{color[color_ally]}'s turn to move: ")
            row, col = move_convert(move)
            if row == "Error" and col == "Error":
                print("Invalid Input!")
                continue

            check = move_check_and_place(row, col, color_ally, color_enemy)
            if check == "Error":
                print("Invalid Move!")
                continue

            break

    return color_enemy

def board_full():
    for row in board:
        for tile in row:
            if empty in tile:
                return False
    return True

def score_count():
    black_score = 0
    for row in board:
        for tile in row:
            if black in tile:
                black_score += 1

    white_score = 0
    for row in board:
        for tile in row:
            if white in tile:
                white_score += 1

    return black_score, white_score

def game():
    turn = black
    
    while True:
        print_board()
        if board_full() == True:
            break
        elif move_check(black, white) == False and move_check(white, black) == False: # Check's if there is moves available
            print("Both Black and White is out of moves!")
            break
        
        if turn == black:
            turn = move_input(black, white)
        
        elif turn == white:
            turn = move_input(white, black)


    black_score, white_score = score_count()

    print("Black has", black_score, "tiles.")
    print("White has", white_score, "tiles.")

    if black_score > white_score:
        print("Black wins!")
    elif black_score < white_score:
        print("White wins!")
    elif black_score == white_score:
        print("Tie!")

board = [
["□", "□", "□", "□", "□", "□", "□", "□"],
["□", "□", "□", "□", "□", "□", "□", "□"],
["□", "□", "□", "□", "□", "□", "□", "□"],
["□", "□", "□", "◯", "⬤", "□", "□", "□"],
["□", "□", "□", "⬤", "◯", "□", "□", "□"],
["□", "□", "□", "□", "□", "□", "□", "□"],
["□", "□", "□", "□", "□", "□", "□", "□"],
["□", "□", "□", "□", "□", "□", "□", "□"]]
black = "◯"
white = "⬤"
empty = "□"
color = {black: "Black", white: "White"}

game()
