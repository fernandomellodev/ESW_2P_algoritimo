"""# Exercício 8 - Busca Binária com Ordenação
# =============================================
# Enunciado: Corrija a função para ordenar a lista antes de realizar a busca binária.
 
vendas = [150, 80, 220, 90, 300]
 
def busca_binaria_vendas(lista, valor):
    lista.ordenar()
    baixo, alto = 0, len(lista) - 1
    enquanto baixo <= alto:
        meio = (baixo + alto) // 2
        se lista[meio] == valor:
            retornar meio
        elif lista[meio] < valor:
            baixo = meio + 1
        outro:
            alto = meio - 1
    retornar -1
 
print("Índice de valor 220:", busca_binaria_vendas(vendas, 220))"""



# Exercício 8 - Busca Binária com Ordenação
# =============================================
# Enunciado: Corrija a função para ordenar a lista antes de realizar a busca binária.
 
vendas = [150, 80, 220, 90, 300]
 
def busca_binaria_vendas(lista, valor):
    lista.sort()  
    low, high = 0, len(lista) - 1
    while low <= high:
        mid = (low + high) // 2
        if lista[mid] == valor:
            return mid
        elif lista[mid] < valor:
            low = mid + 1
        else:
            high = mid - 1
    return -1
 
print("Índice de valor 220:", busca_binaria_vendas(vendas, 220))

