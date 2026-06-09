import random
import time



"""Lógica: Divide a lista recursivamente até ter 1 elemento e depois
intercala (merge) ordenadamente.
Vantagem: Estável e desempenho garantido.
Desvantagem: Requer memória extra O(n)"""

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i = i + 1
        else:
            resultado.append(direita[j])
            j = j + 1

    resultado = resultado + esquerda[i:]
    resultado = resultado + direita[j:]

    return resultado

lista_aleatoria = random.sample(range(1, 100000), 10000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        merge_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Merge Sort...")
inicio = time.time()
lista_ordenada = merge_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("o Merge Sort é excelente para listas muito grandes. O(n log n).")

