table = []
for i in range(9):
    table.append([])
    for j in range(3):
        table[i].append('')
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append('')
end = False
winner = False
turn = 0
player = 1
while end == False and turn < 9:
    has_piece = False
    row = int(input("Digite a linha que quer inserir a peça: "))
    column = int(input("Digite a coluna que quer inserir a peça: "))
    if (row > 2 or row < 0) or (column > 2 or column < 0):
        print("Insira coordenadas válidas.")
    else:
        for i in range(len(table)):
            if table[i][0] == row and table[i][1] == column:
                has_piece = True
        if has_piece == True:
            print("Essa posição já está ocupada.")
        else:
            if player == 1:
                table[turn][0] = row
                table[turn][1] = column
                table[turn][2] = 'X'
                matrix[row][column] = 'X'
            else:
                table[turn][0] = row
                table[turn][1] = column
                table[turn][2] = 'O'
                matrix[row][column] = 'O'
            for i in range(3):
                if (matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][2] != '') or (matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[2][i] != ''):
                    winner = True
                    end = True
            if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[2][2] != '') or (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[2][0] != ''):
                winner = True
                end = True
            count = 0
            for i in range(len(table)):
                if table[i][2] != '':
                    count += 1
                if count == 9:
                    end = True
            count = 0
            turn += 1
            if player == 1:
                player = 2
            else:
                player = 1
            print()
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=" ")
        print()
    print()
if winner:
    if player == 1:
        print("Parabéns, o jogador X venceu!!")
    else:
        print("Parabéns, o jogador O venceu!!")
else:
    print("Velha!!! Não houve um vencedor.")