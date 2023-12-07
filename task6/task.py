import json
import numpy as np

def lor(str, template):
  rev = json.loads(str)
  rev_list = [0 for _ in range(len(template))]
  for i in range(len(rev)):
    if type(rev[i]) is list:
      for el in rev[i]:
        rev_list[template[el]] = i + 1
    else:
      rev_list[template[rev[i]]] = i + 1
  return rev_list

def task(*args):
  experts_count = len(args)
  template = dict()
  rev_count = 0
  for el in json.loads(args[0]):
    if type(el) is list:
      for elem in el:
        template[elem] = rev_count
        rev_count += 1
    else:
      template[el] = rev_count
      rev_count += 1     
  matrix = []
  for rev_str in args:
    matrix.append(lor(rev_str, template))
  x = matrix
  matrix = []
  for i in range(rev_count):
    sum = 0
    for j in range(experts_count):
      sum += x[j][i]
    matrix.append(sum)
  matrix = np.matrix(matrix)
  D = np.var(matrix) * rev_count / (rev_count - 1)
  D_max = experts_count ** 2 *(rev_count ** 3 - rev_count)/12/(rev_count - 1)
  return format(D / D_max, ".2f")



A = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
B = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
C = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

print(task(A, B, C))
