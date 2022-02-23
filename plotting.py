import matplotlib.pyplot as plt
import HashSet as hset
import lst_funcs as fnc

lst_eng = open("new_eng.txt", encoding="utf-8").read().lower().split(", ")

# Adds words to set and counts amount of tries and current size each iteration
words = hset.HashSet()
words.init()
lst_attempts, lst_current_size = [], []

# Counts how many times words are added and how the size increases in HashSet
for key, x in enumerate(lst_eng):
    lst_attempts.append(key + 1)
    words.add(x)
    lst_current_size.append(words.get_size())

# Creates a sorted list containing the length of each word and how many of them
lst_of_length = [str(len(x)) for x in lst_eng]
bst_map = fnc.create_bst(lst_of_length)
sorted_lst = fnc.sort_lst_of_tuples(bst_map.as_list(), "key")

# Takes top 20 of sorted list
x_pos = [x[0] for x in sorted_lst[:20:]]
y_pos = [y[1] for y in sorted_lst[:20:]]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(lst_attempts, lst_current_size)
ax1.set_xlabel('Added Words')
ax1.set_ylabel('Unique Words')
ax1.set_title('"Added Words" VS "Unique Words"')
ax2.bar(x_pos, y_pos)
ax2.set_xlabel('Amount of Letters')
ax2.set_ylabel('Length of Words')
ax2.set_title('"Word Count" VS "Word Length"')
plt.show()
