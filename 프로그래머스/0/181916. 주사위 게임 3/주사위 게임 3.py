def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_num = [dice.count(i) for i in dice]
    if max(dice_num) == 4:
        return 1111 * a
    elif max(dice_num) == 3:
        return (10 * dice[dice_num.index(3)] + dice[dice_num.index(1)]) ** 2
    elif max(dice_num) == 2:
        if min(dice_num) == 2:
            if a == b:
                return (a + c) * abs(a - c)
            else:
                return (a + b) * abs(a - b)
        elif min(dice_num) == 1:
            return dice[dice_num.index(1)] * dice[::-1][dice_num[::-1].index(1)]
    elif max(dice_num) == 1:
        return min(dice)