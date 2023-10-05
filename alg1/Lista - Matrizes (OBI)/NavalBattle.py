rows = int(input())
columns = int(input())
table = []
for i in range(rows):
    table.append([])
    for j in range(columns):
        table[i].append(input())
shots = int(input())
destroyed_ships = 0
for _ in range(shots):
    line = int(input())
    column = int(input())
    if table[line - 1][column - 1] == '#':
        destroyed_ships += 1
print(destroyed_ships)