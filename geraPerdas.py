import random
from datetime import datetime, timedelta
import csv
from lista_produtos import produtos

# Função para obter as informações do produto com base na categoria, subcategoria e produto
def get_produto_info(categoria, subcategoria, produto):
    for item in produtos:
        if item['categoria'] == categoria and item['subcategoria'] == subcategoria and item['produto'] == produto:
            return item['preco_de_custo'], item['preco'], item

# Função para gerar uma data aleatória dentro do período de 30 dias
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime('%Y-%m-%d')

# Função para gerar um dataset
def generate_dataset(start_date, end_date, num_rows):
    dataset = []
    for _ in range(num_rows):
        data = {}
        data['Data'] = generate_random_date(start_date, end_date)
        data['Tipo'] = random.choice(['Ajuste', 'Avaria'])
        
        # Escolher uma categoria aleatória
        categoria = random.choice([produto['categoria'] for produto in produtos])
        data['Categoria'] = categoria
        
        # Filtrar subcategorias com base na categoria escolhida
        subcategorias = [produto['subcategoria'] for produto in produtos if produto['categoria'] == categoria]
        subcategoria = random.choice(subcategorias)
        data['Subcategoria'] = subcategoria
        
        # Filtrar produtos com base na categoria e subcategoria escolhidas
        produtos_filtrados = [produto['produto'] for produto in produtos if produto['categoria'] == categoria and produto['subcategoria'] == subcategoria]
        produto = random.choice(produtos_filtrados)
        data['Produto'] = produto
        
        # Obter a unidade do produto
        _, _, produto_info = get_produto_info(categoria, subcategoria, produto)
        data['Unidade'] = produto_info.get('unidade', '')
        
        # Obter o preço de custo e de venda do produto
        preco_custo, preco_venda, _ = get_produto_info(categoria, subcategoria, produto)
        data['Preço de Custo'] = preco_custo
        data['Preço de Venda'] = preco_venda
        
        data['Quantidade'] = random.randint(1, 100)
        
        if data['Tipo'] == 'Avaria':
            data['Tipo Avaria'] = random.choice(['Furto', 'Validade expirada', 'Danos no transporte'])
        else:
            data['Tipo Avaria'] = ''
        
        dataset.append(data)
    return dataset

# Solicitar ao usuário o mês e o ano
def get_month_and_year():
    while True:
        month = input("Digite o número do mês (1 a 12): ")
        year = input("Digite o ano (exemplo: 2024): ")
        try:
            month = int(month)
            year = int(year)
            if month < 1 or month > 12:
                print("Por favor, digite um número de mês válido (1 a 12).")
                continue
            return month, year
        except ValueError:
            print("Por favor, digite um número válido.")

# Definir a data de início e fim do período com base na entrada do usuário
def get_start_and_end_date(month, year):
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    return start_date, end_date

# Obter mês e ano do usuário
month, year = get_month_and_year()

# Opções para o usuário
print("Escolha uma das opções abaixo:")
print("1. Gerar aleatoriamente entre 5000 e 50000 linhas.")
print("2. Escolher o número exato de linhas a serem geradas.")

# Solicitar a escolha do usuário
while True:
    option = input("Digite o número da opção desejada: ")
    if option == '1':
        num_rows = random.randint(5000, 50000)
        break
    elif option == '2':
        num_rows = int(input("Digite o número exato de linhas a serem geradas: "))
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")

# Definir a data de início e fim do período com base na entrada do usuário
start_date, end_date = get_start_and_end_date(month, year)

# Gerando o dataset
dataset = generate_dataset(start_date, end_date, num_rows)

# Salvando o dataset em um arquivo CSV
csv_filename = f"perdas{month}_{year}.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Data', 'Tipo', 'Categoria', 'Subcategoria', 'Produto', 'Unidade', 'Quantidade', 'Preço de Custo', 'Preço de Venda', 'Tipo Avaria']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in dataset:
        writer.writerow(data)

print(f"Dataset salvo com sucesso em '{csv_filename}'.")
