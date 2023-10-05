import random

# Dicionário de escalas maiores e menores
escalas = {
    'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'Cm': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B♭'],
    #'C Menor Harmônica': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B'],
    #'C Menor Melódica': ['C', 'D', 'E♭', 'F', 'G', 'A', 'B'],
    'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'Dm': ['D', 'E', 'F', 'G', 'A', 'B♭', 'C'],
    #'D Menor Harmônica': ['D', 'E', 'F', 'G', 'A', 'B♭', 'C#'],
    #'D Menor Melódica': ['D', 'E', 'F', 'G', 'A', 'B', 'C#'],
    'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'Em': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    #'E Menor Harmônica': ['E', 'F#', 'G', 'A', 'B', 'C', 'D#'],
    #'E Menor Melódica': ['E', 'F#', 'G', 'A', 'B', 'C#', 'D#'],
    'F': ['F', 'G', 'A', 'B♭', 'C', 'D', 'E'],
    'Fm': ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E♭'],
    #'F Menor Harmônica': ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E'],
    #'F Menor Melódica': ['F', 'G', 'A♭', 'B♭', 'C', 'D', 'E'],
    'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'Gm': ['G', 'A', 'B♭', 'C', 'D', 'E♭', 'F'],
    #'G Menor Harmônica': ['G', 'A', 'B♭', 'C', 'D', 'E♭', 'F#'],
    #'G Menor Melódica': ['G', 'A', 'B♭', 'C', 'D', 'E', 'F#'],
    'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'Am': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    #'A Menor Harmônica': ['A', 'B', 'C', 'D', 'E', 'F', 'G#'],
    #'A Menor Melódica': ['A', 'B', 'C', 'D', 'E', 'F#', 'G#'],
    'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
    'Bm': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    #'B Menor Harmônica': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#'],
    #'B Menor Melódica': ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A#']
    # Adicione mais escalas conforme necessário
    # ...
}

# Função para escolher uma escala
def escolher_escala():
    print("Escolha uma escala ou deixe-me sortear uma para você:")
    print("1. Escolher uma escala")
    print("2. Sortear uma escala aleatoriamente")
    
    opcao = input("Digite 1 ou 2: ")
    
    if opcao == '1':
        print("Escalas disponíveis:")
        for i, escala in enumerate(escalas.keys()):
            print(f"{i+1}. {escala}")
        
        escolha = int(input("Digite o número correspondente à escala desejada: ")) - 1
        
        if 0 <= escolha < len(escalas):
            escala_escolhida = list(escalas.keys())[escolha]
        else:
            print("Opção inválida. Escolhendo uma escala aleatória.")
            escala_escolhida = random.choice(list(escalas.keys()))
    elif opcao == '2':
        escala_escolhida = random.choice(list(escalas.keys()))
    else:
        print("Opção inválida. Escolhendo uma escala aleatória.")
        escala_escolhida = random.choice(list(escalas.keys()))
    
    return escala_escolhida

# Função para gerar uma sequência de notas aleatórias entre 4 e 20
def gerar_sequencia_notas(escala):
    notas = escalas[escala]
    sequencia = [random.choice(notas) for _ in range(random.randint(4, 20))]
    return sequencia

# Função principal
def main():
    escala_escolhida = escolher_escala()
    sequencia_notas = gerar_sequencia_notas(escala_escolhida)
    
    print(f"Escala escolhida: {escala_escolhida}")
    print(f"Sequência de notas geradas: {' '.join(sequencia_notas)}")

if __name__ == "__main__":
    main()
