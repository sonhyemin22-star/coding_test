def solution(rank, attendance):
    c = []
    while len(c) < 3:
        for i in range(1, (len(rank) + 1)):
            if attendance[rank.index(i)] == True:
                c.append(rank.index(i))
    return 10000 * c[0] + 100 * c[1] + c[2]