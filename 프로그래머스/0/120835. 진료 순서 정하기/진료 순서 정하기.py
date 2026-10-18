def solution(emergency):
    r_emergency = sorted(emergency, reverse=True)
    answer = []
    for rank in emergency:
        answer.append(r_emergency.index(rank) + 1)
    return answer