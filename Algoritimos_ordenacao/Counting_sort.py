"""
    Counting Sort (Ordenação por Contagem)
    Estratégia: Não faz comparações. Conta a frequência de cada número e calcula 
    suas posições exatas. Funciona apenas com números inteiros positivos.
    Eficiência: Extremamente rápido, mas usa mais memória. Complexidade: O(n + k).
"""

import random
import time


def counting_sort(lista):
    if not lista:
        return []
    
    lista_copia = lista.copy()
    valor_maximo = max(lista_copia)
    tamanho = len(lista_copia)
    
    resultado = [0] * tamanho
    contagem = [0] * (valor_maximo + 1)
    
    # Conta as ocorrências de cada número
    for i in range(tamanho):
        contagem[lista_copia[i]] += 1
        
    # Acumula as contagens
    for i in range(1, valor_maximo + 1):
        contagem[i] += contagem[i - 1]
        
    # Constrói a lista ordenada
    for i in range(tamanho - 1, -1, -1):
        resultado[contagem[lista_copia[i]] - 1] = lista_copia[i]
        contagem[lista_copia[i]] -= 1
        
    return resultado

lista_aleatoria = random.sample(range(1, 100000), 100000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        counting_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Counting Sort...")
inicio = time.time()
lista_ordenada = counting_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("Sim, o Counting Sort é um dos melhores e mais utilizados algoritmos para listas grandes O(n + k).")
