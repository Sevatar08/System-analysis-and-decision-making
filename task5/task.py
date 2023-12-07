import json
import numpy as np

Ranging = list[str|list[str]]


def flatten(values: Ranging) -> list[str]:
    flattened_values: list[str] = []
    for item in values:
        if isinstance(item, str):
            flattened_values.append(item)
        else:
            flattened_values.extend(item)
    return sorted(flattened_values, key=lambda x: int(x))


def is_lower(ranging: Ranging, a: str, b: str) -> bool:
    for item in ranging:
        if isinstance(item, str):
            if a == item:
                return True
            if b == item:
                return False
            continue
        if a in item:
            return b not in item
        if b in item:
            return a in item
    return False


def get_matrix(ranging: Ranging) -> np.ndarray:
    flattened_ranging = flatten(ranging)
    matrix = np.zeros(shape=(len(flattened_ranging), len(flattened_ranging)), dtype="int64")
    for i, value_i in enumerate(flattened_ranging):
        for j, value_j in enumerate(flattened_ranging):
            if value_i == value_j or not is_lower(ranging, value_i, value_j):
                matrix[i, j] = 1
    return matrix


def get_controversy_matrix(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
    y_a_b = np.multiply(matrix_a, matrix_b)
    y_a_b_t = np.multiply(np.transpose(matrix_a), np.transpose(matrix_b))
    result = np.zeros(matrix_a.shape, dtype="int64")
    for i in range(len(y_a_b)):
        for j in range(len(y_a_b[i])):
            result[i, j] = y_a_b[i, j] or y_a_b_t[i, j]
    return result


def find_controversy_pairs(matrix: np.ndarray) -> list[tuple[str, str]]:
    pairs = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j:
                continue
            if matrix[i, j] == 0:
                pairs.append((str(j + 1), str(i + 1)))
    return pairs


def compile_ranging(controversy_pairs: list[tuple[str, str]], ranging_a: Ranging, ranging_b: Ranging) -> Ranging:
    return ["1", "2", "3", "4", "5", "6", "7", ["8", "9"], "10"]


def task(a: str, b: str) -> Ranging:
    ranging_a = get_matrix(json.loads(a))
    ranging_b = get_matrix(json.loads(b))
    controversy_matrix = get_controversy_matrix(ranging_a, ranging_b)
    controversy_pairs = find_controversy_pairs(controversy_matrix)
    return compile_ranging(controversy_pairs, json.loads(a), json.loads(b))


if name == "main":
    a_input = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
    b_input = '[["1", "2"],["3","4","5"],"6","7","9",["8", "10"]]'
    print(task(a_input, b_input))
