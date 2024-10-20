import sys

def eval(red, blue):
    return 3 * blue + 2 * red

def game_over(red, blue):
    return red == 0 or blue == 0

def minmax_alpha_beta(red, blue, version, depth, maximizing_player):
    if depth == 0 or game_over(red, blue):
        return eval(red, blue)

    if maximizing_player:
        max_eval = float('-inf')
        new_red = red - 1
        eval = minmax_alpha_beta(new_red, blue, version, depth - 1, False)
        max_eval = max(max_eval, eval)
        new_blue = blue - 1
        eval = minmax_alpha_beta(red, new_blue, version, depth - 1, False)
        max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        new_red = red - 1
        eval = minmax_alpha_beta(new_red, blue, version, depth - 1, True)
        min_eval = min(min_eval, eval)
        new_blue = blue - 1
        eval = minmax_alpha_beta(red, new_blue, version, depth - 1, True)
        min_eval = min(min_eval, eval)
        return min_eval

def get_computer_move(red, blue, version, depth):
    if version == "misere":
        best_score = float('-inf')
        best_move = None
        new_red = red - 1
        eval = minmax_alpha_beta(new_red, blue, version, depth, False)
        if eval > best_score:
            best_score = eval
            best_move = (1, 0)
        new_blue = blue - 1
        eval = minmax_alpha_beta(red, new_blue, version, depth, False)
        if eval > best_score:
            best_score = eval
            best_move = (0, 1)
        return best_move
    if version == "standard":
        best_score = float('-inf')
        best_move = None
        new_blue = blue - 1
        eval = minmax_alpha_beta(red, new_blue, version, depth, False)
        if eval > best_score:
            best_score = eval
            best_move = (0, 1)
        new_red = red - 1
        eval = minmax_alpha_beta(new_red, blue, version, depth, False)
        if eval > best_score:
            best_score = eval
            best_move = (1, 0)
        return best_move
        
        
        
            
        

def main():
    if len(sys.argv) < 3:
        print("Usage: red_blue_nim.py <num-red> <num-blue> <version> [first-player] [depth]")
        return

    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) >= 4 else "standard"
    first_player = sys.argv[4] if len(sys.argv) >= 5 else "computer"
    depth = int(sys.argv[5]) if len(sys.argv) >= 6 else float('inf')

    if first_player == "computer":
        computer_turn = True
    else:
        computer_turn = False

    while not game_over(num_red, num_blue):
        if computer_turn:
            r, b = get_computer_move(num_red, num_blue, version, depth)
            num_red -= r
            num_blue -= b
            print(f"Computer removes {r} red and {b} blue.")
        else:
            print(f"Red marbles left: {num_red}, Blue marbles left: {num_blue}")
            while True:
                try:
                    marble_type = input("Choose marble type (red or blue): ").lower()
                    if marble_type not in {"red", "blue"}:
                        print("Invalid choice. Choose red or blue.")
                        continue
                    count = 1  # User can only remove one marble
                    if marble_type == "red" and count <= num_red:
                        r = 1
                        b = 0
                        break
                    elif marble_type == "blue" and count <= num_blue:
                        r = 0
                        b = 1
                        break
                    else:
                        print("Invalid move. Try again.")
                except (ValueError, KeyboardInterrupt):
                    print("Invalid input. Please enter red or blue.")

            num_red -= r
            num_blue -= b

        computer_turn = not computer_turn

    final_score = eval(num_red, num_blue)
    if final_score > 0 and computer_turn==True and version == "standard":
        winner = "Computer"
    elif final_score > 0 and computer_turn == False and version == "standard":
        winner = "Human"
    elif final_score > 0 and computer_turn==True and version == "misere":
        winner = "Human"
    elif final_score > 0 and computer_turn==False and version == "misere":
        winner = "Computer"
    else:
        winner = "Tie"

    print(f"The game is over. {winner} wins with a score of {abs(final_score)}.")

if __name__ == "__main__":
    main()
