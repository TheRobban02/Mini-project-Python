

# Simple function that adds all words in lst to a set and returns it
def unique_words(lst):
    set_of_words = set()
    for x in lst:
        set_of_words.add(x)
    return set_of_words


def top_ten(lst):
    dict_of_words = {}

    # Counts all the words in dictionary, it turns all words in to lower case!
    for x in lst:
        if dict_of_words.get(x) is None:
            dict_of_words[x] = 1
        else:
            dict_of_words[x] += 1

    # sorts by highest value and recast to dictionary
    dict_of_words = dict(sorted(dict_of_words.items(),
                                key=lambda x: x[1], reverse=True))

    # Creates a dictionary containing highest value if word is larger than 4
    top_words = {}
    for key, value in dict_of_words.items():
        if len(top_words) == 10:
            break
        if len(key) > 4:
            top_words[key] = value

    # returns top 10 words dictionary, ordered by highest value
    return top_words


lst_holy = open("new_holy.txt", encoding="utf-8").read().lower().split(", ")
lst_eng = open("new_eng.txt", encoding="utf-8").read().lower().split(", ")

print("Number of unique words:", len(unique_words(lst_eng)))
top_words = top_ten(lst_eng)
for key, x in top_words.items():
    print(key, x)

print("\nNumber of unique words:", len(unique_words(lst_holy)))
top_words = top_ten(lst_holy)
for key, x in top_words.items():
    print(key, x)
