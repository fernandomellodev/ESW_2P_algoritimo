import random
import time



def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


lista_aleatoria = random.sample(range(1, 2001), 2000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        selection_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Selection Sort...")
inicio = time.time()
lista_ordenada = selection_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("ideal para ordenar pequenas listas, mas não é recomendado para grandes listas devido à sua baixa eficiência O^2.")