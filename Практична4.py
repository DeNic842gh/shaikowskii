def sort(inlist):
    element = list(set(inlist))
    return element


def sort_int_str(inlist):
    int_sort = sorted([x for x in inlist if isinstance(x, (int, float))])
    str_sort = sorted([x for x in inlist if isinstance(x, str)])
    return int_sort + str_sort


inlist = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

result = sort(inlist)
result = sort_int_str(result)

print(result)
