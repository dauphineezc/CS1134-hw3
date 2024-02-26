def find_duplicates(lst):
    duplicates = []
    sorted_lst = sorted(lst)
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] == sorted_lst[i - 1]:
            duplicates.append(sorted_lst[i])
    return duplicates
