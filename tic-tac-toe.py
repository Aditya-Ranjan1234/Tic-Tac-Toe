def print_board():
    for i in range(1, 10, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])

def is_free(pos):
    return board[pos] == ' '

def insert(letter, pos):
    if is_free(pos):
        board[pos] = letter
        print_board()
        if check_win(letter):
            print(f"{letter} wins!")
            exit()
        if check_draw():
            print("Draw!")
            exit()
    else:
        insert(letter, int(input("Invalid move! Enter new position: ")))

def check_win(mark):
    return any(board[a] == board[b] == board[c] == mark for a, b, c in win_combos)

def check_draw():
    return all(board[i] != ' ' for i in board)

def player_move():
    insert(player, int(input("Enter position for 'O': ")))

def comp_move():
    best_score = -float('inf')
    best_move = None
    
    for k in board:
        if is_free(k):
            board[k] = bot  
            score = minimax(False)  
            board[k] = ' '  

            if score > best_score:
                best_score = score
                best_move = k
    
    if best_move:
        insert(bot, best_move)
    else:
        print("Draw!")
        exit()

def minimax(is_max):
    if check_win(bot): return 1
    if check_win(player): return -1
    if check_draw(): return 0

    if is_max:  # Maximizing player (Bot)
        best_score = -float('inf')
        for k in board:
            if is_free(k):
                board[k] = bot
                score = minimax(False)
                board[k] = ' '
                best_score = max(score, best_score)
        return best_score
    else:  # Minimizing player (Opponent)
        best_score = float('inf')
        for k in board:
            if is_free(k):
                board[k] = player
                score = minimax(True)
                board[k] = ' '
                best_score = min(score, best_score)
        return best_score

board = {i: ' ' for i in range(1, 10)}
win_combos = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (7,5,3)]
player, bot = 'O', 'X'

print_board()
while True:
    player_move()
    comp_move()
