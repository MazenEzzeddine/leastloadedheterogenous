class Bin(object):
    """ Container for items that keeps a running sum """
    def __init__(self, capacity):
        self.items = []
        self.sum = 0
        self.capacity = capacity

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def remainingCapacity(self):
        var = self.capacity - self.sum
        return var


    def __str__(self):
        """ Printable representation """
        return 'Bin(capacity= %d sum=%d, items=%s)' % ( self.capacity, self.sum, str(self.items))

    def __eq__(self, other):
        return sum(self.items) == sum(other.items)

    def __lt__(self, other):
        return sum(self.items) < sum(other.items)

    def __gt__(self, other):
        return sum(self.items) > sum(other.items)



class FairBin(object):
    """ Container for items that keeps a running sum """
    def __init__(self, capacity):
        self.items = []
        self.sum = 0
        self.capacity = capacity

    def append(self, item):
        self.items.append(item)
        self.sum += item

    def remainingCapacity(self):
        var = self.capacity - self.sum
        return var


    def __str__(self):
        """ Printable representation """
        return 'Bin(capacity= %d sum=%d, items=%s)' % ( self.capacity, self.sum, str(self.items))

    def __eq__(self, other):
        return self.capacity - sum(self.items) == other.capacity- sum(other.items)

    def __lt__(self, other):
        return self.capacity - sum(self.items) < other.capacity - sum(other.items)

    def __gt__(self, other):
        return self.capacity - sum(self.items) > other.capacity - sum(other.items)



def firstFitDec2(weight, n, c):
    weight.sort(reverse=True)


    bins = []

    # Place items one by one
    for i in range(n):

        # Find the first bin that can accommodate
        # weight[i]
        j = 0
        while (j < len(bins)):
            if (bins[j].remainingCapacity() >= weight[i]):
                bins[j].append(weight[i])
                break
            j += 1

        # If no bin could accommodate weight[i]
        if (j == len(bins)):
            bins.append(Bin(c))
            bins[j].append(weight[i])
    for b in bins:
        print(b)
    return bins


def firstFitDecHetero(weight, n, c):
    weight.sort(reverse=True)

    bins_capacity = [100, 150]

    # Place items one by one

    bins = firstFitDec2(weight, n, bins_capacity[1])
    for b in bins:
        print(b)

    print("new bins")
    newbins=[]
    for b in bins:
        for c in bins_capacity:
            if b.sum <= c:
                nb = Bin(c)
                nb.items.append(b.items)
                nb.sum = b.sum
                newbins.append(nb)
                break
    fairbins = []
    for b in newbins:
        fairbins.append(FairBin(b.capacity))
        print(b)

    for b in fairbins:
        print(b)

    for i in range(n):
        fairbins.sort(reverse=True)
        fairbins[0].append(weight[i])
    for b in fairbins:
        print(b)









def firstFitDecLeastLoaded(weight, n, c):

  weight.sort(reverse=True)
  bins = []
  i =0
  while(True):
    # Place items one by one
    for bin in bins:
        bin.items = []
        bin.sum=  0
    for i in range(n):

        # Find the first bin that can accommodate
        # weight[i]
        bins = sorted(bins)

        j = 0
        while (j < len(bins)):
            if (bins[j].remainingCapacity() >= weight[i]):
                bins[j].append(weight[i])
                break
            j += 1

        # If no bin could accommodate weight[i]
        if (j == len(bins)):
            bins.append(Bin(c))
            break
    else:
      break
  for b in bins:
    print(b)



def firstFitDec(weight, n, c):
    # Initialize result (Count of bins)
    weight.sort(reverse=True)

    res = 0

    bin_rem = [0] * n

    # Place items one by one
    for i in range(n):


        j = 0
        while (j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j += 1

        # If no bin could accommodate weight[i]
        if (j == res):
            bin_rem[res] = c - weight[i]
            res = res + 1
    return res







# This code is contributed by shinjanpatra


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weight = [2, 5, 4, 7, 1, 3, 8]
    c = 10
    n = len(weight)
    firstFitDec2(weight, n, 10)
    print("====================")
    aList = [70, 40, 30, 20, 30, 20]
    aList2 = [70, 40, 30, 20, 10, 20]

    n= len(aList)
    firstFitDec2(aList, 6, 100)
    print("====================")

    firstFitDecLeastLoaded(aList, 6, 100)
    print("====================")

    # firstFitDecHetero(aList, 6, 100)
    # print("====================")
    #
    # print("-------------------------")
    # firstFitDecHetero(aList, 6, 150)
    print("-------------------------")
    firstFitDecHetero(aList2, 6, 150)

    # # print("===================")
    # # firstFitDecLeastLoaded(aList2, 6, 100)
    # firstFitDec2(aList2, 6, 100)
    # print("====================")



    #print("Number of bins required in First Fit Decreasing : ", str(firstFitDec(weight, n, c)))

