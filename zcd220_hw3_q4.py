def remove_all(lst, value):
    available_ind = 0
    for i in range(len(lst)):
        if lst[i] != value:
            lst[available_ind] = lst[i]
            available_ind += 1
    del lst[available_ind:]
    return lst

