
val_lst = []


def min_value(diction):
    for val in diction:
        if isinstance(diction[val], int):
            val_lst.append(diction[val])
    return max(val_lst)


print(min_value({1: 2, 2: 5, 3: 1, 4: 8}))
