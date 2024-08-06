white_paper = [[0 for _ in range(100)] for _ in range(100)]
counts = 0

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
index = 1

for _ in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    index += 2
    
    for x_idx in range(x, x+10):
        for y_idx in range(y, y+10):
            white_paper[x_idx][y_idx] = 1
            
for array_row in white_paper:
    counts += array_row.count(1)
    
print(counts)
