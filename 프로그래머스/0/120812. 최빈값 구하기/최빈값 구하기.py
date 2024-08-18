def solution(array):
    array.sort()
    
    max_cnt = 1
    current_cnt = 1
    most = array[0]
    
    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            current_cnt += 1
        else:
            current_cnt = 1
            
        if current_cnt > max_cnt:
            max_cnt = current_cnt
            most = array[i]
        elif current_cnt == max_cnt:
            most = -1
    
    return most
