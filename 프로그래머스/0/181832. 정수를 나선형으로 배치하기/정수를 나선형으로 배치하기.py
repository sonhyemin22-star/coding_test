def solution(n):
    answer = [[0] * n for i in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num, x, y, d = 1, 0, 0, 0
    while num <= n ** 2:
        answer[x][y] = num
        num += 1
        nx, ny = x + directions[d][0], y + directions[d][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= n or answer[nx][ny] != 0:
            d = (d + 1) % 4
            nx, ny = x + directions[d][0], y + directions[d][1]
        x, y = nx, ny
    return answer