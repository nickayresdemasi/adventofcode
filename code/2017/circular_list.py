class CircularList(object):
    def __init__(self, array):
        self.array = array

    def index(self, beg, end):
        '''Allows for indexing of circular list'''

        # check that index is entered correctly
        if beg > end:
            raise ValueError("Invalid indexing")

        # wrap-around if necessary
        if end > len(self.array):
            first_half = self.array[beg:]
            second_half = self.array[:end - len(self.array)]
            sub = first_half + second_half
        else:
            sub = self.array[beg:end]

        return sub

    def replace(self, beg, sub):
        '''Allows for replacement of portion of circular list with other list'''

        for i in range(len(sub)):
            index = beg + i

            # wrap-around if index outside range of array
            if index >= len(self.array):
                index %= len(self.array)

            self.array[index] = sub[i]
