import random   
import time


"""Lógica: Transforma a lista em um Max-Heap (árvore binária) e
remove o maior elemento repetidamente.
Vantagem: Não usa memória extra e garante O (nlogn).
Desvantagem: Não é estável e é mais complexo de
implementar."""


def ajustar_heap(lista, tamanho, raiz):
    maior = raiz
    esquerda = 2 * raiz + 1
    direita = 2 * raiz + 2

    if esquerda < tamanho and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < tamanho and lista[direita] > lista[maior]:
        maior = direita

    if maior != raiz:
        lista[raiz], lista[maior] = lista[maior], lista[raiz]
        ajustar_heap(lista, tamanho, maior)


def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        ajustar_heap(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        ajustar_heap(lista, i, 0)

    return lista

lista_aleatoria = random.sample(range(1, 100000), 100000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        heap_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Heap Sort...")
inicio = time.time()
lista_ordenada = heap_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("Sim, ele é excelente para listas muito grandes, especialmente sob cenários com restrição estrita de memória RAM.(O(n log n)).")