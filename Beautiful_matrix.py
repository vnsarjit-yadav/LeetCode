
row_pos = 0
col_pos = 0

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            row_pos = i + 1   
            col_pos = j + 1


moves = abs(row_pos - 3) + abs(col_pos - 3)

print(moves)
