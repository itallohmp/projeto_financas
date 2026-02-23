from datetime import datetime
import json

gasto_por_mes = {}

def carregar_dados():
    global gasto_por_mes
    try:
        with open("gastos.json", "r") as arquivo:
            gasto_por_mes = json.load(arquivo)
    except FileNotFoundError:
        gasto_por_mes = {}

def salvar_dados():
    with open("gastos.json", "w") as arquivo:
        json.dump(gasto_por_mes, arquivo, indent=4)

def validar_mes(mes: str) -> bool:
    try:
        datetime.strptime(mes, "%m/%Y")
        return True
    except ValueError:
        return False

def adicionar_gasto(mes, item, valor, categoria):
    if not validar_mes(mes):
        return False
    if mes not in gasto_por_mes:
        gasto_por_mes[mes] = {}
    gasto_por_mes[mes][item] = {"valor": valor, "categoria": categoria}
    salvar_dados()
    return True

def excluir_gasto(mes, item):
    if mes in gasto_por_mes and item in gasto_por_mes[mes]:
        gasto_por_mes[mes].pop(item)
        salvar_dados()
        return True
    return False

def gastos_totais(mes):
    if mes not in gasto_por_mes:
        return None
    return sum(dados["valor"] for dados in gasto_por_mes[mes].values())

def gastos_por_categoria(mes):
    if mes not in gasto_por_mes:
        return None
    categorias = {}
    for item, dados in gasto_por_mes[mes].items():
        cat = dados["categoria"]
        categorias[cat] = categorias.get(cat, 0) + dados["valor"]
    return categorias

def gastos_por_ano(ano: str):
    totais = {}
    for mes, itens in gasto_por_mes.items():
        if mes.endswith(ano):
            total_mes = sum(dados["valor"] for dados in itens.values())
            totais[mes] = total_mes
    return totais

# Funções para terminal 
def mostrar_menu():
    print("\n" + "=" * 60)
    print("💰 CONTROLE DE FINANÇAS PESSOAIS".center(60))
    print("=" * 60)
    print("1️⃣  Adicionar gasto")
    print("2️⃣  Excluir gasto")
    print("3️⃣  Ver gastos totais por mês")
    print("4️⃣  Relatório anual")
    print("0️⃣  Sair")
    print("=" * 60)

def adicionar_gasto_terminal():
    mes = input('Digite o mês (MM/YYYY): ').strip()
    item = input('Digite o nome do gasto: ')
    try:
        valor = float(input('Digite o valor gasto: '))
    except ValueError:
        print('Valor Inválido ❌')
        return
    categoria = input('Digite a categoria do gasto: ')
    if adicionar_gasto(mes, item, valor, categoria):
        print(f"Gasto adicionado em {mes} ✅")
    else:
        print("Erro ao adicionar gasto ❌")

def excluir_gasto_terminal():
    mes = input('Digite o mês (MM/YYYY): ')
    item = input('Digite o item a excluir: ')
    if excluir_gasto(mes, item):
        print(f"Gasto {item} removido de {mes} ✅")
    else:
        print("Item não encontrado ❌")

def gastos_totais_terminal():
    mes = input('Digite o mês (MM/YYYY): ')
    total = gastos_totais(mes)
    if total is None:
        print("Mês não encontrado ❌")
    else:
        print(f"Total de gastos em {mes}: R$ {total:.2f}")

def relatorio_anual_terminal():
    ano = input("Digite o ano (YYYY): ")
    totais = gastos_por_ano(ano)
    if not totais:
        print("Nenhum gasto encontrado ❌")
        return
    print(f"\nRelatório de {ano}:")
    for mes, total in totais.items():
        print(f"{mes}: R$ {total:.2f}")
    print(f"Total anual: R$ {sum(totais.values()):.2f}")

def main():
    carregar_dados()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_gasto_terminal()
        elif opcao == '2':
            excluir_gasto_terminal()
        elif opcao == '3':
            gastos_totais_terminal()
        elif opcao == '4':
            relatorio_anual_terminal()
        elif opcao == '0':
            print("Saindo do sistema... 👋")
            break
        else:
            print("Opção inválida ❌ Tente novamente.")

if __name__ == "__main__":
    main()