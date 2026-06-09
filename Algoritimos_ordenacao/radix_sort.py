
import random   
import time

"""Lógica: Ordena dígito por dígito, começando pela unidade até a
casa decimal mais alta.
Vantagem: Excelente para números inteiros grandes.
Desvantagem: Complexidade depende do número de dígitos."""


def counting_sort_por_digito(lista, casa):
    tamanho = len(lista)
    resultado = [0] * tamanho
    contagem = [0] * 10

    for valor in lista:
        digito = (valor // casa) % 10
        contagem[digito] = contagem[digito] + 1

    for i in range(1, 10):
        contagem[i] = contagem[i] + contagem[i - 1]

    i = tamanho - 1
    while i >= 0:
        valor = lista[i]
        digito = (valor // casa) % 10
        resultado[contagem[digito] - 1] = valor
        contagem[digito] = contagem[digito] - 1
        i = i - 1

    for i in range(tamanho):
        lista[i] = resultado[i]


def radix_sort(lista):
    if len(lista) == 0:
        return lista

    maior = max(lista)
    casa = 1

    while maior // casa > 0:
        counting_sort_por_digito(lista, casa)
        casa = casa * 10

    return lista

lista_aleatoria = random.sample(range(1, 100000), 100000)


if __name__ == "__main__":
        lista = lista_aleatoria
        print(lista)
        radix_sort(lista)
        
        
        print("\n ordenado:")
        print (lista)
        
print("Ordenando com Radix Sort...")
inicio = time.time()
lista_ordenada = radix_sort(lista_aleatoria)
fim = time.time()

print(f"Ordenação concluída com sucesso!")
print(f"Tempo de execução: {fim - inicio:.4f} segundos")

print(f"A lista está corretamente ordenada? {lista_ordenada == sorted(lista_aleatoria)}")
print ("Sim, principalmente para inteiros grandes com número de dígitos controlado O(n + b).")