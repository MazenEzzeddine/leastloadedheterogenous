



class Partition(object):
    def __init__(self, id = "",  lamda=0, lag=0 ):
        self.lamda = lamda
        self.lag = lag
        self.id = id


    def __str__(self):
        return "Partition  %s , lamda: %f  lag : %f"  % (self.id, self.lamda, self.lag)

    def __eq__(self, other):
        return self.lamda == other.lamda

    def __lt__(self, other):
        return self.lamda < other.lamda

    def __gt__(self, other):
        return self.lamda > other.lamda

    def __le__(self, other):
        return self.lamda <= other.lamda

    def __ge__(self, other):
        return self.lamda >= other.lamda

