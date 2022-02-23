import BstMap as bst
import HashSet as hset


# Returns a BST class
def create_bst(lst_of_words):
    bst_map = bst.BstMap()
    for x in lst_of_words:
        value = bst_map.get(x)
        if value is not None:
            bst_map.put(x, value + 1)
        else:
            bst_map.put(x, 1)
    return bst_map


# expects a list of tuples and if key or value is to be sorted
def sort_lst_of_tuples(lst, search="value"):
    if search == "value":
        return sorted(lst, key=lambda x: x[1], reverse=True)
    elif search == "key":
        return sorted(lst, key=lambda x: int(x[0]))


# Return a HashSet class
def create_hash_map(lst_of_words):
    new_hset = hset.HashSet()
    new_hset.init()
    for x in lst_of_words:
        new_hset.add(x)
    return new_hset
