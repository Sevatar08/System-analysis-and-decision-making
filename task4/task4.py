import numpy as np

def entropiya(t):
    if (t != 0):
      return -t * np.log2(t)
    else:
      return 0

def toFixed(t):
    return format(t, '.2f')

def task4():
  min_val = 1
  max_val = 6
  all_var_count = max_val * max_val
  mults_count = all_var_count
  sums_count = max_val * 2 - min_val * 2 + 1
  var = [[0 for j in range(mults_count)] for i in range(sums_count)]
  mult_norm = 1
  sum_norm = 2
  used_cols = set()
  
  for i in range(min_val, max_val + 1):
    for j in range(min_val, max_val + 1):
      cur_mult = i * j
      cur_sum = i + j
      used_cols.add(cur_mult - mult_norm)
      var[cur_sum - sum_norm][cur_mult - mult_norm] += 1
      
  resized_var = []
  
  for i in range(sums_count):
    cur_row = []
    for j in range(mults_count):
      if (j in used_cols):
        cur_row.append(var[i][j])
    resized_var.append(cur_row)
    
  matrix = np.array(resized_var)
  mults_count = len(resized_var[0])
  matrix = matrix * 1.0 / all_var_count
  PA = matrix.sum(axis=1)
  PB = matrix.sum(axis=0) 
  vect_ent = np.vectorize(entropiya)
  matrix = vect_ent(matrix)
  PA = vect_ent(PA)
  PB = vect_ent(PB)
  HA = np.sum(PA)
  HB = np.sum(PB)
  HAB = np.sum(matrix)
  HaB = HAB - HA
  HI = HB - HaB
  return [toFixed(HAB), toFixed(HA), toFixed(HB), toFixed(HaB), toFixed(HI)]

print(task4())
