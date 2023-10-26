from io import StringIO
import csv
import math

def task3(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    n = 0
    r = []
    for row in reader:
      r.append([int(ri) for ri in row])
      n += 1
    H = 0.0
    for node in r:
      prob = []
      for ri in node:
        prob.append(ri * 1.0 / (n - 1))
      node_H = 0.0
      for p in prob:
         if (p != 0):
          node_H += p * math.log(p, 2)
      H -= node_H
    return H

print(task3("0,1,3,0,0,0,1\n0,0,1,0,0,1,0\n0,0,2,0,0,1,0\n1,0,0,0,1,0,0\n0,0,1,0,0,1,0\n0,1,0,0,0,0,1\n1,0,0,0,1,0,0\n0,1,1,1,0,0,1\n0,0,1,0,0,0,1\n1,0,0,0,1,0,0\n0,0,1,0,0,1,0"))
