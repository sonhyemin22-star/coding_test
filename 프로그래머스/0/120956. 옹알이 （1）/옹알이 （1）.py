def solution(babbling):
    answer = 0
    baby = ['aya', 'ye', 'woo', 'ma']
    for lan in baby:
        for i, bab in enumerate(babbling):
            if lan in bab and bab.count(lan) == 1:
                babbling[i] = bab.replace(lan, ' ')
    for j in range(len(babbling)):
        babbling[j] = babbling[j].replace(' ', '')
    for k in range(len(babbling)):
        if len(babbling[k]) == 0:
            answer += 1
    return answer