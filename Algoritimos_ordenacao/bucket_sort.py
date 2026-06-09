"""Bucket Sort para o trabalho de algoritmos de ordenacao.

O algoritmo divide os valores em baldes, ordena cada balde com insertion sort
e depois junta todos os baldes para formar a lista final ordenada.
"""

import random
import time


"""
    Bucket Sort (Ordenação por Baldes)
    Estratégia: Distribui os elementos em vários 'baldes' ou grupos. Cada balde é 
    ordenado individualmente e depois todos são juntados.
    Eficiência: Muito bom quando os dados estão bem distribuídos. Complexidade: O(n + k).
"""

def bucket_sort(lista):
    if not lista:
        return []
        
    lista_copia = lista.copy()
    valor_maximo = max(lista_copia)
    tamanho = len(lista_copia)
    
    # 1. Criando os baldes vazios
    baldes = [[] for _ in range(tamanho)]
    
    # 2. Inserindo os elementos nos baldes apropriados
    for i in range(tamanho):
        indice = int(lista_copia[i] * tamanho / (valor_maximo + 1))
        baldes[indice].append(lista_copia[i])
        
    # 3. Ordenando cada balde internamente e juntando o resultado
    resultado = []
    for balde in baldes:
        balde.sort() # Internamente usa o Timsort do Python
        resultado.extend(balde)
        
    return resultado


lista_aleatoria = random.sample(range(0, 100000), 100000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        bucket_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Bucket Sort...")
inicio = time.time()
lista_ordenada = bucket_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("Sim, o Bucket Sort é excelente para listas grandes, mas com uma condição obrigatória: os dados devem estar distribuídos de forma uniforme. O(n log n).")