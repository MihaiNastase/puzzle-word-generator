import os
from webbrowser import get
import pandas as pd
import random
import numpy as np
import itertools

#words_dict = pd.read_csv("words.csv", index_col=False, header=0).aahs
#words_dict.drop_duplicates(inplace=True)

#
# target_words = words_dict.sample(4).to_list()

def generate_puzzle_data(target_words):
    # Creating 4x4 game grid and indexing
    grid = []
    word_hints = {}
    indexes = [[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,1),(1,2),(1,3)],[(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,1),(3,2),(3,3)]]
    
    for index_row in indexes:
        random.shuffle(index_row)
        
    for i, word in enumerate(target_words):
        hint_ind = 0
        for j, letter in enumerate(word):
            grid.append([letter, indexes[j][i]])
            hint_ind += indexes[j][i][1] 
        word_hints[word] = hint_ind + 4
    
    #draw the board
    board = np.zeros([4,4], dtype=str)
    for letter_pos in grid:
        board[letter_pos[1][0]][letter_pos[1][1]] = letter_pos[0]
        
    return grid, word_hints, board


# removes duplicate words
def get_unique_combo(words_dict, max_attempts):
    loop_counter = 0
    while True:
        target_words = words_dict.sample(4).to_list()
    
        rows = np.zeros([4,4],str)
        words_collector = []
        counter = 0

        #split words into letters per board row
        for i, word in enumerate(target_words):
            for j, letter in enumerate(word):
                rows[j][i] = letter

        #get all permutations
        permutations = list(itertools.product(*rows))

        # check if those 4 words can create any other words with their letters
        for combination in permutations:
            test_word = "".join(combination)
            counter += words_dict[words_dict == test_word].count()
            if words_dict[words_dict == test_word].count():
                words_collector.append(combination)

        #print(counter)

        #exit loop
        if len(set(words_collector)) <= 7:
            print("Fails: ", loop_counter)
            #print(words_collector)
            return target_words
        else:
            loop_counter += 1
            if loop_counter > max_attempts:
                print("Failed to find, try again :p")
                return -1

def main():
    # Getting random words
    words_dict = pd.read_csv("words.csv", index_col=False, header=0).aahs
    words_dict.dropna(inplace=True)
    words_dict.drop_duplicates(inplace=True)

    while True:
        print("Input options:\n 1 for words with hints\n 2 for unique words (no hints)\n 0 to exit ...")
        user_input = input("Select option: ")
        if user_input == '0':
            break
        elif user_input == '1':
            try:
                total_puzzles = int(input("Input number of desired puzzles: "))
                puzzle_data = pd.DataFrame(columns=["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4","D1","D2","D3","D4","word1","word2","word3","word4","hint1","hint2","hint3","hint4"])
                for i in range(total_puzzles):
                    target_words = words_dict.sample(4).to_list()
                    grid, word_hints, board= generate_puzzle_data(target_words=target_words)
                    word_order = list(map(lambda x:x[1][1], filter(lambda x:x[1][0]==0, grid)))
                    new_sort = ["","","",""]
                    for i,e in enumerate(word_order):
                        new_sort[e]=target_words[i]
                    puzzle_data.loc[len(puzzle_data)] = list(map(lambda x:x[0].upper(), sorted(grid, key=lambda x:x[1]))) + new_sort + [word_hints[word] for word in new_sort]
                puzzle_data.to_csv("puzzles.csv", index=False)
                if(total_puzzles==1):
                    print(grid)
                    print(board)
                    print(word_hints)
                    input("Press Enter to continue...")
                os.system('cls')
            except:
                os.system('cls')
        elif user_input == '2':
            print(get_unique_combo(words_dict=words_dict, max_attempts=500))
            input("Press Enter to continue...")
            os.system('cls')
        else:
            os.system('cls')


    #input("Press Enter to continue...")

if __name__ == "__main__":
    main()