# Exercicio 1 - Sistema de Gestão de Notas de Alunos


import os

alunos = []

def adicionar_aluno():
    
    try:
        nome = input("Insira o nome do aluno: ")
        
        if not nome:
            print(" Nome não pode estar vazio!")
            
            return False
        
        notas = []
        numero_notas = 0
        
        while numero_notas < 2 or numero_notas > 5:
            try:
                numero_notas = int(input("Qual a quantidade de notas? (2-5): "))
                if numero_notas < 2 or numero_notas > 5:
                    print("somente inserir entre 2 e 5 notas!")
                    continue
            except ValueError:
                print("Digite um número válido!")
                continue       
        for i in range(numero_notas):
            while True:
                try:
                    nota = float(input(f"Nota {i+1}: "))
                    if nota < 0 or nota > 10:
                        print("A nota deve ser entre 0 e 10!")
                        continue
                    notas.append(nota)
                    break
                except ValueError:
                    print("Digite um número válido!")
        media = sum(notas) / len(notas)
        aluno = {
            "nome": nome,
            "notas": notas,
            "media": media
        }
        alunos.append(aluno)
        notas_formatadas = ", ".join(f"{nota:.1f}" for nota in notas)
        print(f"Notas: {notas_formatadas}")
        return True
    except Exception as e:
        print(f"Erro ao adicionar aluno: {e}")
        return False

def pega_media(aluno):
    return aluno["media"]


def ordenar_alunos():
    alunos.sort(key=pega_media, reverse=True)


def exibir_alunos():
    if not alunos:
        print("\n Nenhum aluno cadastrado!")
        return

    print("Alunos ordenados por média:")
    for i, aluno in enumerate(alunos, 1):
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")


def salvar_em_arquivo(nome_arquivo="alunos.txt"):
    if not alunos:
        print("\n Nenhum aluno para salvar!")
        return False
    
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write("ALUNO,MEDIA\n")
            for aluno in alunos:
                arquivo.write(f"{aluno['nome']},{aluno['media']:.2f}\n")      
        print(f"Os dados foram salvos no arquivo '{nome_arquivo}'.")
        return True
        
    except PermissionError:
        print(f"Erro: Sem permissão para salvar no arquivo '{nome_arquivo}'.")
        return False
    except OSError as e:
        print(f"Erro ao salvar no arquivo: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False


def menu_principal():
    while True:
        print("SISTEMA DE GESTÃO DE NOTAS")
        print("1. Adicionar aluno")
        print("2. Exibir alunos ordenados")
        print("3. Salvar em arquivo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            adicionar_aluno()
        elif opcao == '2':
            ordenar_alunos()
            exibir_alunos()
        elif opcao == '3':
            ordenar_alunos()
            salvar_em_arquivo()
        elif opcao == '4':
            print("\nPrograma encerrado!")
            break
        else:
            print("Opção inválida! Digite um número entre 1 e 4.")



if __name__ == "__main__":
 
    menu_principal()
