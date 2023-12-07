import json
import numpy as np

def calculate_lor(rev_str: str, template: dict):
    rev = json.loads(rev_str)
    rev_list = [0 for _ in range(len(template))]
    for i in range(len(rev)):
        if isinstance(rev[i], list):
            for el in rev[i]:
                rev_list[template[el]] = i + 1
        else:
            rev_list[template[rev[i]]] = i + 1
    return rev_list

def task(*args) -> str:
    experts_count = len(args)
    template = dict()
    rev_count = 0
    for el in json.loads(args[0]):
        if isinstance(el, list):
            for elem in el:
                template[elem] = rev_count
                rev_count += 1
        else:
            template[el] = rev_count
            rev_count += 1     
    matrix = []
    for rev_str in args:
        matrix.append(calculate_lor(rev_str, template))
    x = np.array(matrix)
    sum_matrix = np.sum(x, axis=0)
    D = np.var(sum_matrix) * rev_count / (rev_count - 1)
    D_max = (experts_count ** 2) * ((rev_count ** 3 - rev_count) / 12) / (rev_count - 1)
    return format(D / D_max, ".2f")

A = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
B = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
C = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

print(task(A, B, C))
