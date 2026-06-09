import random
import time

""""Lógica: Escolhe um pivô e particiona a lista entre menores e
maiores que o pivô.
Vantagem: Extremamente rápido na média e cache-friendly.
Desvantagem: Pior caso quadrático se o pivô for mal
escolhido."""

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = []
    iguais = []
    maiores = []

    for valor in lista:
        if valor < pivo:
            menores.append(valor)
        elif valor == pivo:
            iguais.append(valor)
        else:
            maiores.append(valor)

    return quick_sort(menores) + iguais + quick_sort(maiores)


    
lista_aleatoria = random.sample(range(1, 100000), 100000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        quick_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Quick Sort...")
inicio = time.time()
lista_ordenada = quick_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("Sim, o Quick Sort é um dos melhores e mais utilizados algoritmos para listas grandes O(n^2).")