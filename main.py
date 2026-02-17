from datetime import datetime
import json

gasto_por_mes = {}

def main():    
    carregar_dados()
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_gasto()
            
        elif opcao == '2':
            excluir_gasto()
        
        elif opcao == '3':
            gastos_totais()
            
        elif opcao == '0':
            print("Saindo do sistema... 👋")
            break

        else:
            print("Opção inválida ❌ Tente novamente.")  

def mostrar_menu():
    print("\n" + "=" * 60)
    print("💰 CONTROLE DE FINANÇAS PESSOAIS".center(60))
    print("=" * 60)
    print("1️⃣  Adicionar gasto")
    print("2️⃣  Excluir gasto")
    print("3️⃣  Ver gastos totais por mês")
    print("0️⃣  Sair")
    print("=" * 60)
    
def adicionar_gasto():
    mes = input('Digite o mês (MM/YYYY): ').strip()
    
    if not validar_mes(mes):
        print("Formato inválido ❌ Use MM/YYYY (ex: 01/2026)")
        return

    item = input('Digite o nome do gasto: ')
    try:
        valor = float(input('Digite o valor gasto: '))
    except ValueError:
        print('Valor Inválido')
        return
    
    if mes not in gasto_por_mes:
        gasto_por_mes[mes] = {}
        
    gasto_por_mes[mes][item] = gasto_por_mes[mes].get(item, 0) + valor
    salvar_dados()
    print(f"Gasto adicionado em {mes} ✅")

def excluir_gasto():
    print(list(gasto_por_mes.keys()))

    mes = input('Digite o mês de referência (ex: 01/2016): ')
    
    if not validar_mes(mes):
        print("Formato inválido ❌ Use MM/YYYY (ex: 01/2026)")
        return
    
    for chave, valor in gasto_por_mes[mes].items():
        print(f'Item: {chave} valor: {valor}')

    item = input('Qual item deseja excluir: ')
    
    if mes not in gasto_por_mes:
        print("Mês não encontrado ❌")
        return
    
    if item in gasto_por_mes[mes]:
        gasto_por_mes[mes].pop(item)
        salvar_dados()
        print(f'Gasto {item} removido de {mes} ✅')
    else:
        print('item não encontrado nesse mês ❌')
        
def gastos_totais():
    print(list(gasto_por_mes.keys()))
    
    mes = input('Selecione o mês para verificar os valores dos gastos: ')
    
    if mes not in gasto_por_mes:
        print('Mês não encontrado❌')
        return
    
    total = sum(gasto_por_mes[mes].values())
    
    print(f'Total de gastos em {mes}: R$ {total:.2f}')
    
def salvar_dados():
    with open("gastos.json", "w") as arquivo:
        json.dump(gasto_por_mes, arquivo, indent=4)
        
def carregar_dados():
    global gasto_por_mes # DECLARADO PARA MODIFICAR A VARIAVEL EXTERNA
    try:
        with open("gastos.json", "r") as arquivo:
            gasto_por_mes = json.load(arquivo)
    except FileNotFoundError:
        gasto_por_mes = {}

def validar_mes(mes: str) -> bool:
    try:
        datetime.strptime(mes, "%m/%Y")  # Letra Y maiscula para utilizar o ano com 4 digitos
        return True
    except ValueError:
        return False
       
if __name__ == "__main__":
    main()