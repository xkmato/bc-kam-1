class BinarySearch(list):
    def __init__(self, a, b):
        super(BinarySearch, self).__init__([x for x in range(b, a*b+b, b)])
        self.length = a

    def search(self, arg):
        first = 0
        last = self.length - 1
        found = False
        count = 0
        if self[0] == arg:
            return dict(count=count, index=0)
        if self[last] == arg:
            return dict(count=count, index=last)

        while first <= last and not found:
            count += 1
            midpoint = int((first + last)/2)
            if self[midpoint] == arg:
                return dict(count=count, index=midpoint)
            else:
                if arg < self[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return dict(count=count, index=-1)