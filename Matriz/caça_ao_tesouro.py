import random


TAMANHO = 5


def criar_matriz(tamanho):
    matriz = []
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            linha.append(" ")
        matriz.append(linha)
    return matriz


def imprimir_tabuleiro(mapa):
    print("   0 1 2 3 4")
    for linha in range(TAMANHO):
        conteudo = " ".join(mapa[linha])
        print(f"{linha}  {conteudo}")


def distancia_manhattan(linha1, coluna1, linha2, coluna2):
    return abs(linha1 - linha2) + abs(coluna1 - coluna2)


def obter_dica(distancia):
    if distancia == 1:
        return "Muito perto"
    if distancia in (2, 3):
        return "Perto"
    return "Longe"


mapa = criar_matriz(TAMANHO)
tesouro_linha = random.randint(0, TAMANHO - 1)
tesouro_coluna = random.randint(0, TAMANHO - 1)
mapa[tesouro_linha][tesouro_coluna] = "X"

tentativas = 0
encontrado = False

print("JOGO DA CACA AO TESOURO")
print("O tesouro esta escondido em uma matriz 5x5.")
print("Digite a linha e a coluna de 0 a 4 para tentar encontra-lo.")
print()

while not encontrado:
    try:
        linha = int(input("Digite a linha (0-4): "))
        coluna = int(input("Digite a coluna (0-4): "))
    except ValueError:
        print("Entrada invalida. Digite apenas numeros de 0 a 4.")
        print()
        continue

    if linha < 0 or linha >= TAMANHO or coluna < 0 or coluna >= TAMANHO:
        print("Posicao invalida. Use valores entre 0 e 4.")
        print()
        continue

    tentativas += 1

    if linha == tesouro_linha and coluna == tesouro_coluna:
        encontrado = True
        print()
        print("Parabens! Voce encontrou o tesouro!")
        print(f"Tentativas: {tentativas}")
        print()
        print("Mapa final:")
        imprimir_tabuleiro(mapa)
    else:
        distancia = distancia_manhattan(linha, coluna, tesouro_linha, tesouro_coluna)
        print(obter_dica(distancia))
        print()
