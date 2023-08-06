import math

from Consumer import Consumer
from Partition import Partition

import  matplotlib.pyplot as plt


time = []
point = []
lamdasla = 85
replicas = []
wrkld = []
replicasbin=[]

p0 = Partition("p0", 50.0, 0.0)
p1 = Partition("p1", 25.0, 0.0)
p2 = Partition("p2", 80.0, 0.0)
p3 = Partition("p3", 75.0, 0.0)
p4 = Partition("p4", 80.0, 0.0)
partitions: list[Partition] = [p0, p1, p2, p3, p4]


font = {'family': 'normal',
        'weight': 'bold',
        'size': 8}

def scaledLeastLoaded(partitions: list[Partition], f:float):
    partitions.sort(reverse=True)
    consCount = 1
    while True:
        consumers : list[Consumer] = []
        for i in range(consCount):
            consumer = Consumer(str(i), [],  85.0)
            consumers.append(consumer)

        for j in range(len(partitions)):
            consumers.sort(reverse=True)
            for id in range(consCount):
                if partitions[j].lamda < consumers[id].mu - consumers[id].getLamda():
                    consumers[id].partitions.append(partitions[j])
                    break
            else:
                consCount += 1
                break
        else:
            break
    return consumers

def readWorkload():
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 8}
    plt.rc('font', **font)
    with open('defaultArrivalRatesm.csv', 'r') as f:
        lines = f.readlines()

    for line in lines:
        sample = line.split(',')[1]
        wrkld.append(math.ceil(float(sample)))
        point.append(math.ceil(float(sample)))

    return  wrkld


def computeReplicasLinearBinPackFraction():
    for t in range(600):
        for p in range(5):
            partitions[p].lamda = point[t]/5.0
        bins = scaledLeastLoaded(partitions, 1)
        replicasbin.append(len(bins))

        # elif len(bins) < len(currentBins):
        #     bins = scaledLeastLoaded(partitions, 1)
        #     if len(bins) < len(currentBins):
        #       replicasbin.append(len(bins))
        #       currentBins = bins
        #     else:
        #         replicasbin.append(len(currentBins))
        # else:
        #     replicasbin.append(len(currentBins))

        ##########################################
        #bins = scaledLeastLoaded(items, 1.0)
        #computeLatencies(point[t], bins)
        #replicasbin.append(bins)

    # print scaling actions:
    scalingActions = 0
    for t in range(599):
        if replicasbin[t] != replicasbin[t+1]:
            scalingActions += 1
    print("Scaling Actions is: " + str(scalingActions))


def plotWorkloadWithReplicasBinPack():
    replicasscaled = []
    for r in range(len(replicasbin)):
        replicasscaled.append(replicasbin[r]*85)

    plt.plot(time, wrkld)
    plt.plot(time, replicasscaled)
    plt.show()

def plotWorkload():
    for i in range(len(wrkld)):
        time.append((i+1))
        point.append(wrkld[i])
    plt.plot(time, wrkld)
    plt.xlabel("Time (sec)", **font)
    plt.ylabel("Events/sec",**font)
    plt.show()

if __name__=='__main__':
    readWorkload()
    plotWorkload()
    computeReplicasLinearBinPackFraction()
    plotWorkloadWithReplicasBinPack()

    #
    # for part in partitions:
    #     print(part)
    # print("==============")
    #
    # cons = scaledLeastLoaded(partitions, 1.0)
    # for c in range(len(cons)):
    #     print(cons[c])