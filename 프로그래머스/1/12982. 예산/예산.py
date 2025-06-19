def solution(d, budget):
    d.sort()
    count = 0
    for cost in d:
        if budget >= cost:
            budget -= cost
            count += 1
        else:
            break
    return count