def print_board():
    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")
    
    coord_num = 1
    # Prints numbers on the side of the board
    # There is two spaces between every piece
    for row in board:
        print(coord_num, row[0], "",row[1], "",row[2], "",row[3], "",row[4], "",row[5], "",row[6], "", row[7], coord_num)
        coord_num += 1

    # Prints letter on top of the board
    print("  A  B  C  D  E  F  G  H")

# Converts an input to a form python understands
def move_convert(move: str) -> int:
    # Converts input coord letter to number
    # Check if the input is valid
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
    
    # Converts input coord number subtracting 1
    # Check if the input is valid
    try:
        row = int(move[1]) - 1
        if row < 0 or row > 7:
            return "Error", "Error"
    except ValueError:
        print("yep")
        return "Error", "Error"

    return row, col

# Checks whether a move is legal to play.
# Yeah, this needs reworking...
# Since the function is being powercreeped by move_check_and_place, 
# it is only used to check if player has viable moves.
def move_check(color_ally, color_enemy) -> bool:
    # Initialize row and col 
    row = 0
    col = -1
    # col is -1 because it gets +1 as soon as the while loop start
    # Don't ask me why

    while True:
        # Goes through the entire board with stack of code
        col += 1
        if col == 8:
            row += 1
            col = 0
        if row == 8:
            return False

        # If the tile is not empty, continue
        # meaning ignore the rest and restart while loop 
        if board[row][col] != empty: 
            continue
        
        # All the directional while loops works the same way:
        # They check whether the first button is enemy's piece, which
        # sets variable "first" from True to False. Then they continue
        # the loop until they find ally's piece, which in turn returns
        # True, ending the function. If the direction is not valid,
        # try the next direction until all the directions are exhausted.

        # West
        col_west = col
        first = True
        while True:
            # Acts as a pointer
            col_west -= 1
            
            # First color has to be enemy, which sets first to False.
            # It can still be triggered in subsequent loops.
            if board[row][col_west] == color_enemy:
                first = False
            # After the first, start looking for ally piece. If one is
            # found, the move is valid.
            elif board[row][col_west] == color_ally and first == False:
                return True
            else:
                break
        
        # East
        col_east = col
        first = True
        while True:
            col_east += 1
            # Checks whether the tile is inside the board.
            # West is the only one who doesn't need this if clause.
            if col_east > 7:
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
            if row_north < 0:
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
            if row_south > 7:
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
            if row_north < 0 or col_west < 0:
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
            if row_north < 0 or col_east > 7:
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
            if row_south > 7 or col_east > 7:
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
            if row_south > 7 or col_west < 0:
                break

            if board[row_south][col_west] == color_enemy:
                first = False
            elif board[row_south][col_west] == color_ally and first == False:
                return True
            else:
                break

# This function is just powercreeped move_check, as it also places a button
def move_check_and_place(row, col, color_ally, color_enemy):
    # Initialize playable which turns into True when one direction discoveres a valid move.
    # If no valid route is found, return false.
    playable = False
    # If the tile is not empty, return Error
    if board[row][col] != empty:
        return "Error"

    # West
    col_west = col
    first = True
    while True:
        col_west -= 1
        if col_west < 0:
            break

        if board[row][col_west] == color_enemy:
            first = False
        elif board[row][col_west] == color_ally and first == False:
            # This for loop turns all the enemy pieces color to ally's
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
        if col_east > 7:
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
        if row_north < 0:
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
        if row_south > 7:
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
        if row_north < 0 or col_west < 0:
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
        if row_north < 0 or col_east > 7:
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
        if row_south > 7 or col_east > 7:
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
        if row_south > 7 or col_west < 0:
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

# This function takes care of player's inputs.
# Return moves turn to opponent.
# This structure makes no sense, but I'm not going to touch the code for now.
def move_input(color_ally, color_enemy):
    # Checks if player has viable moves
    if move_check(color_ally, color_enemy) == False:
        print(f"{color[color_ally]} is out of moves!")
        return color_enemy    
    elif move_check(color_ally, color_enemy) == True:
        # Loop player's turn until he makes a viable move
        while True:
            # Player's input gets places in "move" variable
            move = input(f"{color[color_ally]}'s turn to move: ")
            row, col = move_convert(move)
            # Checks for invalid input
            if row == "Error" and col == "Error":
                print("Invalid Input!")
                continue
            
            # Check for invalid move
            check = move_check_and_place(row, col, color_ally, color_enemy)
            if check == "Error":
                print("Invalid Move!")
                continue

            break

    return color_enemy

# Check whether the board is full
def board_full():
    for row in board:
        for tile in row:
            if empty in tile:
                return False
    return True

# Counts score when the game ends
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

# Backend
def game():
    turn = black

    # The whole game is inside this while loop
    while True:
        print_board()
        if board_full() == True:
            break
        # Check's if there is moves available
        elif move_check(black, white) == False and move_check(white, black) == False:
            print("Both Black and White is out of moves!")
            break

        # Black's turn
        if turn == black:
            turn = move_input(black, white)
        # White's turn
        elif turn == white:
            turn = move_input(white, black)

    # Get scores and announce the result
    black_score, white_score = score_count()

    print("Black has", black_score, "tiles.")
    print("White has", white_score, "tiles.")

    if black_score > white_score:
        print("Black wins!")
    elif black_score < white_score:
        print("White wins!")
    elif black_score == white_score:
        print("Tie!")

# Frontend
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
