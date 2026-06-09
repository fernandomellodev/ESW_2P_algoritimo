import random
import time
def bubble_sort(lista):
    n = len(lista)

    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista

lista_aleatoria = random.sample(range(1, 2001), 2000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        bubble_sort(lista)
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Bubble Sort...")
inicio = time.time()
lista_ordenada = bubble_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("ideal para ordenar pequenas listas, mas não é recomendado para grandes listas devido à sua baixa eficiência (O(n^2)).")