def criar_tabuleiro(tamanho=8):
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(".")
        tabuleiro.append(linha)
    return tabuleiro


def imprimir_tabuleiro(tabuleiro, linha_escolhida=None, coluna_escolhida=None):
    nrows = len(tabuleiro)
    if nrows > 0:
        ncols = len(tabuleiro[0])
    else:
        ncols = 0

    cabecalho_colunas = []
    for c in range(ncols):
        if c == coluna_escolhida:
            cabecalho_colunas.append(f"[{c}]")
        else:
            cabecalho_colunas.append(f" {c} ")
    print("    " + " ".join(cabecalho_colunas))

    print("  +" + ("---+" * ncols))

    for r in range(nrows):
        rotulo = f">{r}" if r == linha_escolhida else f" {r}"
        celulas = []
        for c in range(ncols):
            celulas.append(tabuleiro[r][c])
        print(rotulo + " | " + " | ".join(celulas) + " |")
        print("  +" + ("---+" * ncols))


def posicao_valida(linha, coluna, tamanho=8):
    return 0 <= linha < tamanho and 0 <= coluna < tamanho


def marcar_movimentos_cavalo(tabuleiro, linha_cavalo, coluna_cavalo):
    movimentos = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1)
    ]

    tamanho = len(tabuleiro)
    for movimento in movimentos:
        nova_linha = linha_cavalo + movimento[0]
        nova_coluna = coluna_cavalo + movimento[1]

        if posicao_valida(nova_linha, nova_coluna, tamanho):
            tabuleiro[nova_linha][nova_coluna] = "*"

    tabuleiro[linha_cavalo][coluna_cavalo] = "C"


print("EXERCICIO 2 - MOVIMENTOS DO CAVALO")
print("Tabuleiro 8x8")
print("Digite a posicao inicial do cavalo (linha e coluna de 0 a 7).")
print()

tabuleiro = criar_tabuleiro(8)

entrada_valida = False
while entrada_valida == False:
    try:
        linha = int(input("Digite a linha (0-7): "))
        coluna = int(input("Digite a coluna (0-7): "))

        if posicao_valida(linha, coluna, 8):
            entrada_valida = True
        else:
            print("Posicao invalida. Use valores entre 0 e 7.")
            print()
    except ValueError:
        print("Entrada invalida. Digite apenas numeros de 0 a 7.")
        print()

marcar_movimentos_cavalo(tabuleiro, linha, coluna)

print()
print("Tabuleiro final:")
imprimir_tabuleiro(tabuleiro, linha_escolhida=linha, coluna_escolhida=coluna)
