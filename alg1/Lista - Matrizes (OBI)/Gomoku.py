table = []
winner = 0
for i in range(15):
    table.append([])
    for j in range(15):
        table[i].append(int(input()))
for i in range(len(table)- 4):
    for j in range(len(table[i]) - 4):
        if table[i][j] == table[i][j + 1] == table[i][j + 2] == table[i][j + 3] == table[i][j + 4] != 0:
            winner = table[i][j]
        if table[i][j] == table[i + 1][j] == table[i + 2][j] == table[i + 3][j] == table[i + 4] != 0:
            winner = table[i][j]
for i in range(len(table) - 4):
    for j in range(len(table[i]) - 4):
        if table[i][j] == table[i + 1][j + 1] == table[i + 2][j + 2] == table[i + 3][j + 3] == table[i + 4][j + 4] != 0:
            winner = table[i][j]
        if table[i][j] == table[i + 1][j - 1] == table[i + 2][j - 2] == table[i + 3][j - 3] == table[i + 4][j - 4] != 0:
            winner = table[i][j]
print(winner)