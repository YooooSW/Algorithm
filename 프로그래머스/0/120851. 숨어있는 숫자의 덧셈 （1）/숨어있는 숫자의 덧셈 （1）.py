def solution(my_string):
    answer = 0
    num = ['1','2','3','4','5','6','7','8','9']
    
    for i in range(len(my_string)):
        if my_string[i] in num:
            answer += int(my_string[i])
        else:
            continue
    return answer