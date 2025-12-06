"""
关系性质判定 & 闭包运算（Python 版）
"""
from copy import deepcopy


# —— 性质判定 ——
def is_reflexive(m):
    n = len(m)
    for i in range(n):
        if m[i][i] != 1:
            return False
    return True


def is_irreflexive(m):
    n = len(m)
    for i in range(n):
        if m[i][i] != 0:
            return False
    return True


def is_symmetric(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True


def is_anti_symmetric(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if i != j and m[i][j] == 1 and m[j][i] == 1:
                return False
    return True


def is_transitive(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                for k in range(n):
                    if m[j][k] == 1 and m[i][k] != 1:
                        return False
    return True


# —— 闭包运算 ——
def reflexive_closure(m):
    c = deepcopy(m)
    for i in range(len(c)):
        c[i][i] = 1
    return c


def symmetric_closure(m):
    c = deepcopy(m)
    n = len(c)
    for i in range(n):
        for j in range(n):
            if c[i][j] == 1:
                c[j][i] = 1
    return c


def transitive_closure(m):
    c = deepcopy(m)
    n = len(c)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = c[i][j] or (c[i][k] and c[k][j])
    return c


def warshall_steps(m):
    """
    返回每一步矩阵（含初始），用于前端动画
    """
    R = deepcopy(m)
    n = len(R)
    steps = [deepcopy(R)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])
        steps.append(deepcopy(R))
    return steps