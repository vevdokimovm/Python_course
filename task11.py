class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x) # super().append()
            # list().append(x)
        else:
            raise NonPositiveError()

class NonPositiveError(Exception):
    pass