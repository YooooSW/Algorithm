def solution(number):
    num_sum = sum(int(digit) for digit in number)
    
    return num_sum % 9