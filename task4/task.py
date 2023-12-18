from math import log2

def get_vals():
    values_sum = []
    values_prod = []
    for i in range(1, 7):
        for j in range(1, 7):
            sum_ij = i + j
            prod_ij = i * j
            values_sum.append(sum_ij)
            values_prod.append(prod_ij)
    values_sum = list(set(values_sum))
    values_prod = list(set(values_prod))
    matrix = [[0 for _ in range(len(values_prod))] for _ in range(len(values_sum))]
    for i in range(1, 7):
        for j in range(1, 7):
            sum_ij = i + j
            prod_ij = i * j
            matrix[values_sum.index(sum_ij)][values_prod.index(prod_ij)] += 1
    return matrix

def prmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] /= 36
    return matrix

def sentropy(matrix, by='row'):
    entropy = 0.0
    if by == 'row':
        for i in range(len(matrix)):
            h = 0.0
            for value in matrix[i]:
                if value != 0.0:
                    h += value
            h = -1 * h * log2(h)
            entropy += h
    elif by == 'column':
        for i in range(len(matrix[0])):
            h = 0.0
            for j in range(len(matrix)):
                if matrix[j][i] != 0.0:
                    h += matrix[j][i]
            h = -1 * h * log2(h)
            entropy += h
    return entropy

def jentropy(matrix):
    entropy = 0.0
    for i in range(len(matrix)):
        h = 0.0
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0.0:
                h += -1 * matrix[i][j] * log2(matrix[i][j])
        entropy += h
    return entropy

def centropy(matrix, prob_matrix):
    prob_matrix_cond = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            prob_matrix_cond[i][j] = matrix[i][j] / sum(matrix[i])
    entropy = 0.0
    for i in range(len(prob_matrix_cond)):
        h_si = 0.0
        for j in range(len(prob_matrix_cond[i])):
            if prob_matrix_cond[i][j] != 0.0:
                h_si += -1 * prob_matrix_cond[i][j] * log2(prob_matrix_cond[i][j])
        h = h_si * sum(prob_matrix[i])
        entropy += h
    return entropy

def task():
    matrix = get_vals()
    prob_matrix = prmatrix(matrix)
    entropy_A = sentropy(prob_matrix, by='row')
    entropy_B = sentropy(prob_matrix, by='column')
    entropy_AB = jentropy(prob_matrix)
    entropy_B_A = centropy(matrix, prob_matrix)
    information_A_B = entropy_B - entropy_B_A
    return entropy_A, entropy_B, entropy_AB, entropy_B_A, information_A_B


task()
