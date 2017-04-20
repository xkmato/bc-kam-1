def find_missing(list_x, list_y):
    in_y = set(list_y) - set(list_x)
    in_x = set(list_x) - set(list_y)
    if in_x or in_y:
        return list(in_x)[0] if in_x else list(in_y)[0]
    return 0
