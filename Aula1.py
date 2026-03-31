def soma(a, b): 
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def testeAB():
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: ")) 
 
    if a > b:
        print("certo")
    else:
        while a < b:
            print("deu erro")
            a = float(input("Insira o primeiro valor novamente: "))
            b = float(input("Insira o segundo valor novamente: "))

    return a, b
                
# Desempacotando o retorno da função em duas variáveis
a, b = testeAB()

resultado1 = soma(a, b)
resultado2 = subtracao(a, b)
resultado3 = multiplicacao(a, b)
resultado4 = divisao(a, b)

print(f"Valores: ({a}, {b}) | Resultados: {resultado1:.3f}, {resultado2:.3f}, {resultado3:.3f}, {resultado4:.3f}")