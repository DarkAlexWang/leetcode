# You will be supplied with two data files in CSV format .
# The first file contains statistics about various dinosaurs. The second file
# contains additional data.
# Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) *
# SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the
# names of only the bipedal dinosaurs from fastest to slowest.
# Do not print any other information.
#
import math
import heapq

def printBipedalDinosaursOrderBySpeed(filePathDinoInfo, filePathAddInfo):
    bipedalDinosaurs = {}
    g = 9.8

    with open(filePathAddInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            if line:
                NAME, STRIDE_LENGTH, STANCE = line.split(',')
                if STANCE == "bipedal":
                    bipedalDinosaurs[NAME] = float(STRIDE_LENGTH)

    with open(filePathDinoInfo, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline().strip()
            if line:
                NAME, LEG_LENGTH, DIET = line.split(',')
                if NAME in bipedalDinosaurs:
                    STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[NAME], float(STRIDE_LENGTH)
                    bipedalDinosaurs[NAME] = ((STRIDE_LENGTH/ LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
    heap = [(value, key) for key, value in bipedalDinosaurs.items()]
    fastest = heapq.nlargest(len(heap), heap)
    print(*[name for speed, name in fastest], sep = '\n')

printBipedalDinosaursOrderBySpeed('dataset1.csv', 'dataset2.csv')
