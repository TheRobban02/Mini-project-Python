import lst_funcs as fnc

lst_holy = open("new_holy.txt", encoding="utf-8").read().lower().split(", ")
lst_eng = open("new_eng.txt", encoding="utf-8").read().lower().split(", ")


def top_ten(lst):
    lst = fnc.create_bst(lst)
    lst = fnc.sort_lst_of_tuples(lst.as_list())
    result, count = "", 0
    for x in lst:
        if count == 10:
            break
        elif len(x[0]) > 4:
            count += 1
            result += f"{x[0]} | {x[1]}\n"
    return result


# Print information holy
new_hset = fnc.create_hash_map(lst_holy)
print(f"Number of unique words: {new_hset.get_size()}")
print("Top 10 occuring words new_holy.txt")
print(top_ten(lst_holy))
print(f"Max bucket size: {new_hset.max_bucket_size()}")
print()

# Overwrite data
new_hset = fnc.create_hash_map(lst_eng)

# Print information eng
print(f"Number of Unique words: {new_hset.get_size()}")
print("Top 10 occuring words new_eng.txt")
print(top_ten(lst_eng))
print(f"Max bucket size: {new_hset.max_bucket_size()}")
print()
