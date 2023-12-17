import csv
import argparse

def read(filepath):
    dict = {}
    with open(filepath, 'r') as table:
        reader = csv.reader(table)
        for row in reader:
            if row[0] not in dict:
                dict[row[0]] = row[1:]
            else:
                dict[row[0]].extend(row[1])
    return dict

def keys(graph):
    all_keys = []
    for key in graph:
        if key not in all_keys:
            all_keys.append(key)
        for elem in graph[key]:
            if elem not in all_keys:
                all_keys.append(elem)
    return all_keys, len(all_keys)

def matrix(graph, ln):
    matrix = [[0 for _ in range(ln)] for _ in range(ln)]
    for k in graph:
        for v in graph[k]:
            matrix[int(k) - 1][int(v) - 1] = 1
            matrix[int(v) - 1][int(k) - 1] = -1
    return matrix

def csv(matrix, file_name='task_res.csv'):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for row in matrix:
            writer.writerow(row)
        
def task(filename):
    graph = read(filename)
    _, ln = keys(graph)
    matrix = matrix(graph, ln)
    result = [[0 for _ in range(5)] for _ in range(ln)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result[i][0] += 1
                for index, value in enumerate(matrix[j]):
                    if value == 1:
                        result[i][2] += 1
            if matrix[i][j] == -1:
                result[i][1] += 1
                for index, value in enumerate(matrix[j]):
                    if value == -1:
                        result[i][3] += 1
                    if value == 1 and index != i:
                        result[i][4] += 1
    csv(result)
    
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()

args = parser()
task(args.filepath)
