import random
import time


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1

        lista[j + 1] = chave

    return lista

lista_aleatoria = random.sample(range(1, 2001), 2000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        insertion_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Insertion Sort...")
inicio = time.time()
lista_ordenada = insertion_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("ideal para ordenar pequenas listas, mas não é recomendado para grandes listas devido à sua baixa eficiência (O(n^2)).")