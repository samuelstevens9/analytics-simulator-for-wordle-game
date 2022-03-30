from dictionary import dictionary
from wordle_env import wordle
from solver import brute

# print("tamed")
# game = wordle.Game("tamed")
# solver = brute.BruteForce()
# solved = None
# solved = solver.update_state(game.try_word(solver.guess_word("tamed")))
# # print("Solved", solved, game.wordle_word)
# while solved is None:
#     solved = solver.update_state(game.try_word(solver.guess_word()))
#     print("Solved", solved, game.wordle_word)


# top twenty
first_words = ['heron','agile','tribe','token','sperm','sloth','shaun','prune','ample','trend','slung','month','globe','tucks','sepal','north','forms','cloth','aleck','winch','thorn','piano','hotel','dance','balms','tiber',]
first_words += ['heart', 'abide']
first_words += ['slice', 'tried','crane']
first_words = ['clump']
# first_words = dictionary.five_letter.copy()
best_words = [] # [("word", chance),...]
count_of_words = len(first_words)
count_of_fw = 0
for fw in first_words:
    count_of_fw += 1
    game_count = 2000
    solved_count = 0
    for i in range(game_count):

        game = wordle.Game()
        solver = brute.BruteForce()
        solved = None
        solved = solver.update_state(game.try_word(solver.guess_word(fw)))
        solved = solver.update_state(game.try_word(solver.guess_word("berth")))
        # print("Solved", solved)
        while solved is None:
            solved = solver.update_state(game.try_word(solver.guess_word()))
            # print("Solved", solved, game.wordle_word)
        if solved:
            solved_count += 1

    print(fw, "Solved", solved_count, "of", game_count, round(solved_count/game_count,2), count_of_fw, " of ", count_of_words)
    best_words.append((solved_count, fw))

best_words.sort(reverse=True)
print("top ten, of ", count_of_words)
print(best_words[0:20])

# top ten at 100 games
# [(93, 'ample'), (92, 'heron'), (92, 'agile'), (91, 'tribe'), (91, 'token'), (91, 'sperm'), (91, 'sloth'), (91, 'shaun'), (91, 'prune'), (91, 'prams')]
# top 20 at 200 games
# [(181, 'trend'), (180, 'slung'), (180, 'month'), (180, 'globe'), (179, 'tucks'), (179, 'sepal'), (179, 'north'), (179, 'forms'), (179, 'cloth'), (179, 'aleck'), (178, 'winch'), (178, 'thorn'), (178, 'piano'), (178, 'hotel'), (178, 'dance'), (178, 'balms'), (177, 'tiber'), (177, 'perth'), (177, 'legit')]
# trend
# Solved 7959, 7935 of 10000 0.79, 7980 of 10000 0.8 random first word
# heart: 8214, 8157 of 10000 0.82
# abide: 8112, 8182 of 10000 0.82
# raise: 7989 of 10000 0.8
# treat: 7891 of 10000 0.79