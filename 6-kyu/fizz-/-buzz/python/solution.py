def solution(number):
    res = [0, 0, 0]
    for i in range(1, number):
        if i % 15 == 0:
            res[2] += 1
        elif i % 5 == 0:
            res[1] += 1
        elif i % 3 == 0:
            res[0] += 1
    return res