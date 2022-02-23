import time
import lst_funcs as fnc
import matplotlib.pyplot as plt

lst_eng = open("new_eng.txt", encoding="utf-8").read().lower().split(", ")
time_lst_get, lst_depth, lst_size = [], [], []

# # Creates a hashmap and does 2 iterations to go through list in each
# # list and add element to only one list which creates a list of unique words
lst_of_unique_words = fnc.create_hash_map(lst_eng)
lst_of_unique_words = [element for inner_list in
                       lst_of_unique_words.buckets for element in inner_list]

bst_map = fnc.create_bst([])
key, iterations = 0, 4
for i in range(1, iterations + 1):

    # Limit will increase by a fourth the size of unique lst each iteration
    limit = int(len(lst_of_unique_words) / iterations) * i

    # Adds words to tree, each iteration it will continue
    # where it left in lst_of_unique_words
    for x in range(key, limit):
        bst_map.put(lst_of_unique_words[x], 1)

    # Test speed of get method
    start = time.time()
    for x in range(key, limit):
        bst_map.get(lst_of_unique_words[x])
    time_lst_get.append((time.time() - start) * 1000)
    key = limit

    # Get Size and Depth from BST
    lst_depth.append(bst_map.max_depth())
    lst_size.append(bst_map.size())

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(lst_size, time_lst_get)
ax1.set_xlabel('Amount of words in BST')
ax1.set_ylabel(f'Time in ms to get()\
{round(len(lst_of_unique_words) / iterations)} times')
ax1.set_title('Look-up time VS Tree size')

ax2.plot(lst_size, lst_depth, 'r')
ax2.set_xlabel('Amount of words in BST')
ax2.set_ylabel('Max Depth')
ax2.set_title('Max Depth VS Tree size')
plt.show()
