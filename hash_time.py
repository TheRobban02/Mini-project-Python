import time
import lst_funcs as fnc
import matplotlib.pyplot as plt
import HashSet as hs

lst_eng = open("new_eng.txt", encoding="utf-8").read().lower().split(", ")

# Creates a hashmap and does 2 iterations to go through list in each
# list and add element to only one list which creates a list of unique words
lst_of_unique_words = fnc.create_hash_map(lst_eng)
lst_of_unique_words = [element for inner_list in
                       lst_of_unique_words.buckets for element in inner_list]

hsh_test = hs.HashSet()
hsh_test.init()

time_lst, size_lst, max_buckets_lst, bucket_size_lst = [], [], [], []
key = 0

amount_of_tests = 10
for i in range(0, amount_of_tests):

    # Limit will increase by a tenth the size of unique lst each iteration
    limit = int(len(lst_of_unique_words) / amount_of_tests - 1) * i

    start = time.time()
    for x in range(key, limit):
        hsh_test.add(lst_of_unique_words[x])
    time_lst.append((time.time() - start) * 1000)
    size_lst.append(hsh_test.get_size())
    bucket_size_lst.append(hsh_test.max_bucket_size())
    max_buckets_lst.append(len(hsh_test.buckets))
    key = limit

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(size_lst, time_lst)
ax1.set_xlabel('Amount of words to add')
ax1.set_ylabel('Time in ms to add()')
ax1.set_title('Amount of words to add vs Size')
ax2.plot(max_buckets_lst, bucket_size_lst)
ax2.set_xlabel('Set Sizes')
ax2.set_ylabel('Max Bucket Size')
ax2.set_title('Max bucket size VS Set size')
plt.show()
