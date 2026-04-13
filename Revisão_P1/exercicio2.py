# Questao 2 - Biblioteca de Livros Digitais

import os

livros = []
def ler_inteiro_positivo(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um numero inteiro positivo!")
                continue
            return valor
        except ValueError:
            print("Digite um numero inteiro valido!")


def adicionar_livro():
    titulo = input("Titulo do livro: ")
    autor = input("Autor: ")

    if not titulo or not autor:
        print("Titulo e autor nao podem estar vazios!")
        return False

    ano = ler_inteiro_positivo("Ano de publicacao: ")
    paginas = ler_inteiro_positivo("Numero de paginas: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas,
    }
    livros.append(livro)
    print("Livro adicionado com sucesso!")
    return True


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado!")
        return

    print("\nLivros cadastrados:")
    for i, livro in enumerate(livros, start=1):
        print(
            f"{i}. {livro['titulo']} | Autor: {livro['autor']} | "
            f"Ano: {livro['ano']} | Paginas: {livro['paginas']}"
        )


def ordenar_livros():
    if not livros:
        print("Nenhum livro para ordenar!")
        return False

    print("Ordenar por:")
    print("1. Ano de publicacao")
    print("2. Numero de paginas")
    criterio = input("Escolha (1-2): ")

    if criterio == "1":
        chave = "ano"
    elif criterio == "2":
        chave = "paginas"
    else:
        print("Opcao invalida!")
        return False

    ordem = input("Ordem crescente ou decrescente? (C/D): ")
    if ordem not in ("C", "D"):
        print("Opcao invalida! Use C para crescente ou D para decrescente.")
        return False

    reverso = ordem == "D"
    livros.sort(key=lambda livro: livro[chave], reverse=reverso)
    print("Livros ordenados com sucesso!")
    return True


def salvar_livros(nome_arquivo="biblioteca.txt"):
    if not livros:
        print("Nenhum livro para salvar!")
        return False

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("TITULO,AUTOR,ANO,PAGINAS\n")
            for livro in livros:
                linha = f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n"
                arquivo.write(linha)
        print(f"Os dados foram salvos no arquivo '{nome_arquivo}'.")
        return True
    except PermissionError:
        print(f"Erro: sem permissao para escrever em '{nome_arquivo}'.")
        return False
    except OSError as erro:
        print(f"Erro de E/S ao salvar arquivo: {erro}")
        return False


def carregar_livros(nome_arquivo="biblioteca.txt"):
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' nao encontrado.")
        return False

    try:
        livros_carregados = []
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                linha = linha.strip()
                if not linha:
                    continue

                partes = [parte.strip() for parte in linha.split(",")]
                if len(partes) != 4:
                    print(f"Linha {numero_linha} ignorada: formato invalido.")
                    continue

                if numero_linha == 1 and [p.upper() for p in partes] == ["TITULO", "AUTOR", "ANO", "PAGINAS"]:
                    continue

                titulo, autor, ano_texto, paginas_texto = partes

                try:
                    ano = int(ano_texto)
                    paginas = int(paginas_texto)
                    if ano <= 0 or paginas <= 0:
                        raise ValueError
                except ValueError:
                    print(f"Linha {numero_linha} ignorada: ano/paginas invalidos.")
                    continue

                livros_carregados.append(
                    {
                        "titulo": titulo,
                        "autor": autor,
                        "ano": ano,
                        "paginas": paginas,
                    }
                )

        livros.clear()
        livros.extend(livros_carregados)
        print("Dados carregados com sucesso!")
        return True
    except PermissionError:
        print(f"Erro: sem permissao para ler '{nome_arquivo}'.")
        return False
    except OSError as erro:
        print(f"Erro de E/S ao carregar arquivo: {erro}")
        return False


def menu_principal():
    print("Bem-vindo a Biblioteca de Livros Digitais!")

    while True:
        print("\nEscolha uma opcao:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar livros")
        print("4. Salvar dados em arquivo")
        print("5. Carregar dados do arquivo")
        print("6. Sair")

        opcao = input("> ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            ordenar_livros()
        elif opcao == "4":
            salvar_livros()
        elif opcao == "5":
            carregar_livros()
        elif opcao == "6":
            salvar = input("Deseja salvar os dados antes de sair? (S/N): ").strip().upper()
            if salvar == "S":
                salvar_livros()
            print("Programa encerrado!")
            break
        else:
            print("Opcao invalida! Escolha entre 1 e 6.")


if __name__ == "__main__":
    menu_principal()
