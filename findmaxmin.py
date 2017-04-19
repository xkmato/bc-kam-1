def find_max_min(arr):
    try:
        arr = sorted(arr)
        return list({arr[0], arr[-1]})
    except TypeError:
        raise TypeError("Expecting an array of integers and floats only")