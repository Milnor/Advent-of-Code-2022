#!/usr/bin/env python3

def my_move(round):
    try:
        opponent = round.split(" ")[0]
        outcome = round.split(" ")[1].strip()
        
        if outcome == "X":
            # Lose
            if opponent == "A":
                return 3
            elif opponent == "B":
                return 1
            elif opponent == "C":
                return 2
        elif outcome == "Y":
            # Draw
            if opponent == "A":
                return 1 # rock
            elif opponent == "B":
                return 2 # paper
            elif opponent == "C":
                return 3 # scissors
        elif outcome == "Z":
            # Win
            if opponent == "A":
                return 2
            elif opponent == "B":
                return 3
            elif opponent == "C":
                return 1
    except:
        return 0

def did_i_win(round):
    try:
        opponent = round.split(" ")[0]
        me = round.split(" ")[1].strip()
        #print(f"{opponent} vs {me}")
        # Wins
        if opponent == "A" and me == "Y":
            #print("win!")
            return 6
        elif opponent == "B" and me == "Z":
            return 6
        elif opponent == "C" and me == "X":
            return 6
        # Ties
        elif opponent == "A" and me == "X":
            return 3
        elif opponent == "B" and me == "Y":
            return 3
        elif opponent == "C" and me == "Z":
            return 3
        # Losses
        else:
            return 0
    except:
        # ignore the final blank line
        #print("skipped!")
        return 0

def main():
    with open("./input/02-1.txt", "r") as file:
        all_data = file.readlines()

        # Part 1
        # A or X is Rock, worth 1
        # B or Y is Paper, worth 2
        # C or Z is Scissors, worth 3
        # Scoring:
        # 0 = loss
        # 3 = draw
        # 6 = win
        total_score = 0

        for round in all_data:
            if "X" in round:
                total_score += 1
            elif "Y" in round:
                total_score += 2
            elif "Z" in round:
                total_score += 3
            total_score += did_i_win(round)

        print(f"Total score: {total_score}")

        # Part 2
        # X = lose
        # Y = draw
        # Z = win
        total_score = 0
        for round in all_data:
            if "X" in round:
                # I lose
                total_score += 0
            elif "Y" in round:
                # A draw
                total_score += 3
            elif "Z" in round:
                # I win
                total_score += 6
            total_score += my_move(round)

        print(f"Total score: {total_score}")

if __name__ == "__main__":
    main()
