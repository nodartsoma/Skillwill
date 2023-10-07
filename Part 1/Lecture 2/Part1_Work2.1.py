
val_lst = []


def min_value(diction):
    for val in diction:
        if type(diction[val]) == int:
            val_lst.append(diction[val])
    return max(val_lst)
