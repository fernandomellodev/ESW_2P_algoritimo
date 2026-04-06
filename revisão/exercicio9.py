"""# Exercício 9 - Relatório de Vendas com Dicionário
# =============================================
# Anunciado: Corrija o cálculo do total de vendas tratando possíveis erros de conversão.
 
vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}
 
def total_vendas(vendas):
    total = 0
    para valor em vendas.values():
        tentar:
            total += float(valor)
        exceto:
            passar
    retornar total
 
print("Total de vendas:", total_vendas(vendas_dia))"""


# Exercício 9 - Relatório de Vendas com Dicionário
# =============================================
# Anunciado: Corrija o cálculo do total de vendas tratando possíveis erros de conversão.
 
vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}

def total_vendas(vendas):
    total = 0
    for valor in vendas.values():
        try:
            total += float(valor)
        except ValueError:
            print(f"Erro de conversão ao calcular o valor de {valor}. Ignorando...")
            continue
    return total

print("Total de vendas:", total_vendas(vendas_dia))