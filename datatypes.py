def data_type(arg):
    if arg is None:
        return 'no value'
    if isinstance(arg, str):
        return len(arg)
    if isinstance(arg, bool):
        return arg
    if isinstance(arg, int):
        if arg == 100:
            return 'equal to 100'
        return 'less than 100' if arg < 100 else 'more than 100'
    if isinstance(arg, list):
        if len(arg) >= 3:
            return arg[2]
        return None