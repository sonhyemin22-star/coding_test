def solution(lines):
    answer = 0
    line = []
    lines.sort(key=lambda x : x[0])
    for i in range(3):
        for j in range((i + 1), 3):
            if lines[i][1] > lines[j][0]:
                if lines[i][1] >= lines[j][1]:
                    for k in range(lines[j][0], (lines[j][1] + 1)):
                        line.append(k)
                else:
                    for k in range(lines[j][0], (lines[i][1] + 1)):
                        line.append(k)
    line2 = sorted(list(set(line)), reverse=True)
    for index in range(len(line2) - 1):
        if line2[index] - line2[index + 1] == 1:
            answer += 1
    return answer