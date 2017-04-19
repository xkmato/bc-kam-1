def words(arg):
    word_list = arg.replace("\n", " ").replace("\t", " ").split(" ")
    count = {}
    for w in word_list:
        if w:
            if w.isdigit():
                w = int(w)
            if count.get(w, None):
                count[w] += 1
            else:
                count[w] = 1
    return count