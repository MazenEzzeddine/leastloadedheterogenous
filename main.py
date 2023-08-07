# This is a sample Python script.
import math

from Consumer import Consumer
from Partition import Partition


import matplotlib.pyplot as plt




point = []
wrkld = []
time=[]

font = {'family': 'normal',
        'weight': 'bold',
        'size': 8}


replicasbin=[]

p0 = Partition("p0", 0.0, 0.0)
p1 = Partition("p1", 0.0, 0.0)
p2 = Partition("p2", 0.0, 0.0)
p3 = Partition("p3", 0.0, 0.0)
p4 = Partition("p4", 0.0, 0.0)
partitions: list[Partition] = [p0, p1, p2, p3, p4]


replicas = {100: 0, 300:0}
replicass = {180: [], 300:[]}



def scaledLeastLoadedHomegenous(partitions: list[Partition], f:float):
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


def computeReplicasLinearBinPackFraction():
    for t in range(600):
        for p in range(5):
            partitions[p].lamda = point[t]/5.0
        bins = scaledLeastLoadedHomegenous(partitions, 1)
        replicasbin.append(len(bins))
    scalingActions = 0
    for t in range(599):
        if replicasbin[t] != replicasbin[t+1]:
            scalingActions += 1
    print("Scaling Actions is: " + str(scalingActions))


def computeReplicasLinearBinPackHeterogenousFraction():
    for t in range(600):
        for p in range(5):
            partitions[p].lamda = point[t]/5.0
        bins = scaledLeastLoadedHeterogenous(partitions, 1, [180, 300])

        for bino in [180.0, 300.0]:
            for bin in bins:
                if bin.mu == bino:
                    replicass[bin.mu].append(bin.mu)
                    break
            else :
                replicass[int(bino)].append(0)




def plotWorkloadWithReplicasBinPack():
    replicasscaled = []
    for r in range(len(replicasbin)):
        replicasscaled.append(replicasbin[r]*85)

    plt.plot(time, wrkld)
    plt.plot(time, replicasscaled)
    plt.show()



def plotWorkloadWithReplicasBinPackHeterogenous():
    plt.plot(time, wrkld)
    plt.plot(time, replicass[180])
    plt.plot(time, replicass[300])
    plt.show()

def scaledLeastLoadedHeterogenous ( partitions: list[Partition], f:float, rate : list[int]):
    wsla=5
    partitions.sort(reverse=True)
    lamdaUnpacked:float =0
    lagUnpacked:float =0
    for i in range(len(partitions)) :
        lamdaUnpacked += partitions[i].lamda
        lagUnpacked += partitions[i].lag
    consumers: list[Consumer] = []
    consCount = 1
    while True:
        for i in range(consCount-1):
            consumers[i].partitions = []
        index = chooseConsumerUsingHeuritic(lamdaUnpacked,lagUnpacked, rate)#Consumer(str(i), [],  85.0)
        cons = Consumer(str(consCount-1),[],rate[index])
        consumers.append(cons)
        lamdaUnpacked = 0.0
        for i in range(len(partitions)):
            lamdaUnpacked += partitions[i].lamda
            lagUnpacked += partitions[i].lag
        for j in range(len(partitions)):
            consumers.sort(reverse=True) ### remaining Arrival Capacity from high to low
            for id in range(consCount):
                if partitions[j].lamda < consumers[id].mu - consumers[id].getLamda():
                    consumers[id].partitions.append(partitions[j])
                    lamdaUnpacked -= partitions[j].lamda
                    # -=lag ignore for now
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


def plotWorkload():
    for i in range(len(wrkld)):
        time.append((i+1))
        point.append(wrkld[i])
    plt.plot(time, wrkld)
    plt.xlabel("Time (sec)", **font)
    plt.ylabel("Events/sec",**font)
    plt.show()

def chooseConsumerUsingHeuritic(lamdaunpacked:float, lagunpacked:float, rate:list[float]):
    wsla=5
    rate.sort()
    for i in range(len(rate)):
        if rate[i] >= lamdaunpacked and rate[i]*wsla >= lagunpacked:
            return i
    else:
        return len(rate) - 1



def testscaledLeastLoadedHomegenous():
    p0 = Partition("p0", 50.0, 0.0)
    p1 = Partition("p1", 25.0, 0.0)
    p2 = Partition("p2", 80.0, 0.0)
    p3 = Partition("p3", 75.0, 0.0)
    p4 = Partition("p4", 80.0, 0.0)
    partitions: list[Partition] = [p0, p1, p2, p3, p4]
    for part in partitions:
     print(part)
    print("==============")

    cons = scaledLeastLoadedHomegenous(partitions, 1.0)
    for c in range(len(cons)):
        print(cons[c])

def testscaledLeastLoadedHeterogenous():
    p0 = Partition("p0", 50.0, 0.0)
    p1 = Partition("p1", 25.0, 0.0)
    p2 = Partition("p2", 80.0, 0.0)
    p3 = Partition("p3", 75.0, 0.0)
    p4 = Partition("p4", 80.0, 0.0)
    partitions: list[Partition] = [p0, p1, p2, p3, p4]
    for part in partitions:
     print(part)
    print("==============")

    cons = scaledLeastLoadedHeterogenous(partitions, 1.0,[180, 300])
    for c in range(len(cons)):
        print(cons[c])

if __name__ == '__main__':
    #testscaledLeastLoadedHomegenous()
    #testscaledLeastLoadedHeterogenous()
    readWorkload()
    plotWorkload()
    # computeReplicasLinearBinPackFraction()
    # plotWorkloadWithReplicasBinPack()
    computeReplicasLinearBinPackHeterogenousFraction()
    plotWorkloadWithReplicasBinPackHeterogenous()


