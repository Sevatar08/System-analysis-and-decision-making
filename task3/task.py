import csv
import argparse
import math

def probability(matrix):
    prob_matrix = []
    n = len(matrix)
    for row in matrix:
        temp_probs = []
        for value in row:
            temp_probs.append(float(value) / (n - 1))
        prob_matrix.append(temp_probs)
    return prob_matrix

def entropy1(prob_matrix):
    entropies = []
    for row in prob_matrix:
        h = 0.0
        for value in row:
            if value != 0.0:
                h += -1 * value * math.log2(value)
        entropies.append(h)
    return entropies

def task(matrix):
    prob_matrix = probability(matrix)
    entropies = entropy1(prob_matrix)
    entropy = 0.0
    for value in entropies:
        entropy += value
    return entropy


matrix = [
    [0,1,3,0,0,0,1],
    [0,0,1,0,0,1,0],
    [0,0,1,0,0,1,0],
    [1,0,0,0,1,0,0],
    [0,0,3,0,0,1,0],
    [0,1,1,0,0,0,1],
    [0,1,1,1,0,0,1],
    [1,0,0,0,1,0,0],
    [0,0,1,0,0,0,1],
    [0,0,1,0,0,1,0],
    [1,0,0,0,1,0,0],
]

res = task(matrix)
print(res)
