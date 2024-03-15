import csv
import random
from faker import Faker
from datetime import datetime, timedelta
from rich import print
from rich.prompt import Prompt
from lista_produtos import produtos  # Importa a lista de produtos

# Inicialização da Faker
fake = Faker('pt_BR')

# Definindo constantes
MIN_NUM_VENDAS = 10000
MAX_NUM_VENDAS = 30000
MIN_CPF_PERCENTAGE = 5
MAX_CPF_PERCENTAGE = 25
NUM_CAIXAS = 20
NUM_OPERADORAS = 20
MOTIVOS_CANCELAMENTO = ["Pagamento não autorizado", "Fraude", "Estoque indisponível", "Erro no preço",
                        "Desistência do cliente", "Problemas técnicos", "Problemas de entrega", "Desconto recusado"]
TIPOS_PAGAMENTO = ["Cartão_Débito", "Cartão_Crédito", "Pix", "Dinheiro"]

# Lista de nomes de operadoras femininas
operadoras = ['Clara', 'Alice', 'Mariana', 'Ana', 'Beatriz', 'Carla', 'Daniela', 'Fernanda', 'Gabriela', 'Helena',
              'Isabela', 'Juliana', 'Laura', 'Márcia', 'Natália', 'Olivia', 'Patrícia', 'Renata', 'Sabrina', 'Tatiana']

# Definindo horário de funcionamento
HORARIO_ABERTURA = datetime.strptime("08:00:00", "%H:%M:%S").time()
HORARIO_FECHAMENTO = datetime.strptime("22:00:00", "%H:%M:%S").time()

# Gerar uma base de CPFs aleatória correspondendo a 5 a 25% do total de vendas
def generate_base_cpfs(num_vendas, seed=None):
    if seed is not None:
        random.seed(seed)  # Define a semente para a geração de CPFs
    else:
        random.seed()  # Semente aleatória
    total_cpfs = num_vendas * random.randint(MIN_CPF_PERCENTAGE, MAX_CPF_PERCENTAGE) // 100
    cpfs = []
    for _ in range(total_cpfs):
        cpf = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
        cpfs.append(cpf)
    return cpfs

# Função para escolher um CPF da base fixa
def choose_cpf():
    return random.choice(BASE_CPFS)

# Função para gerar uma data aleatória dentro de um mês/ano específico e dentro do horário de funcionamento
def random_date(year, month):
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1
    
    data = fake.date_time_between(datetime(year, month, 1), datetime(next_year, next_month, 1))
    while not (HORARIO_ABERTURA <= data.time() <= HORARIO_FECHAMENTO):
        data = fake.date_time_between(datetime(year, month, 1), datetime(next_year, next_month, 1))
    return data

# Função para gerar o dataset de vendas
def generate_sales_dataset(year, month, num_vendas, seed=None):
    filename = f"vendas_{month}_{year}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['CPF', 'Data', 'Hora', 'PDV', 'Operadora', 'Categoria', 'Subcategoria', 'Produto',
                         'Preço de Custo', 'Preço', 'Quantidade', 'Valor Total', 'Cancelamentos', 'Tipo de Pagamento'])

        # Gerar base de CPFs com semente aleatória
        global BASE_CPFS
        BASE_CPFS = generate_base_cpfs(num_vendas, seed)

        # Determinar o número de cancelamentos aleatoriamente
        num_cancelamentos = int(num_vendas * random.uniform(0.005, 0.20))

        # Dicionário para rastrear as compras feitas por cada CPF no mesmo dia
        compras_por_cpf = {}

        # Gerar vendas
        for _ in range(num_vendas):
            cpf = choose_cpf()
            data = random_date(year, month)
            hora = data.strftime("%H:%M:%S")
            pdv = random.randint(1, NUM_CAIXAS)
            
            # Verificar se há compras anteriores para o mesmo CPF no mesmo dia
            if cpf in compras_por_cpf:
                compras_anteriores = compras_por_cpf[cpf]
                ultima_compra = compras_anteriores[-1]
                # Verificar se a última compra foi feita no mesmo dia e se o intervalo é menor ou igual a 60 segundos
                hora_ultima_compra = ultima_compra['Hora']
                if ultima_compra['Data'] == data.date() and (datetime.combine(datetime.min, data.time()) - datetime.combine(datetime.min, datetime.strptime(hora_ultima_compra, "%H:%M:%S").time())).total_seconds() <= 60:
                    # Se sim, utilizar o mesmo PDV e operadora da última compra
                    pdv = ultima_compra['PDV']
                    operadora = ultima_compra['Operadora']
                else:
                    operadora = random.choice(operadoras)  # nome de operadora feminina
            else:
                operadora = random.choice(operadoras)  # nome de operadora feminina
            
            produto_info = random.choice(produtos)
            categoria = produto_info['categoria']
            subcategoria = produto_info['subcategoria']
            produto = produto_info['produto']
            preco_custo = produto_info.get('preco_de_custo', None)  # Adicionando o preço de custo
            preco = produto_info['preco']
            quantidade = random.randint(1, 10)
            valor_total = round(preco * quantidade, 2)

            # Geração aleatória de cancelamentos
            cancelamento = random.randrange(num_vendas) < num_cancelamentos
            motivo_cancelamento = random.choice(MOTIVOS_CANCELAMENTO) if cancelamento else ""
            
            # Escolha aleatória do tipo de pagamento
            tipo_pagamento = random.choice(TIPOS_PAGAMENTO)

            # Salvar a compra atual no dicionário de compras por CPF
            if cpf not in compras_por_cpf:
                compras_por_cpf[cpf] = []
            compras_por_cpf[cpf].append({'Data': data.date(), 'Hora': hora, 'PDV': pdv, 'Operadora': operadora})

            writer.writerow([cpf, data.date(), hora, pdv, operadora, categoria, subcategoria,
                             produto, preco_custo, preco, quantidade, valor_total, motivo_cancelamento, tipo_pagamento])

    print(f"Dataset gerado e salvo em '{filename}' com {num_vendas} registros")

def main():
    print("[bold cyan]Bem-vindo ao gerador de vendas![/bold cyan]")
    year = Prompt.ask("Por favor, informe o ano:", default="2024")
    month = Prompt.ask("Por favor, informe o mês (1-12):", default="2")
    num_vendas = Prompt.ask("Por favor, informe a quantidade de registros desejada (deixe em branco para aleatório):", default="")
    seed = Prompt.ask("Por favor, informe a semente para a geração de CPFs (deixe em branco para aleatória):", default="")

    year = int(year)
    month = int(month)

    if num_vendas:
        num_vendas = int(num_vendas)
    else:
        num_vendas = random.randint(MIN_NUM_VENDAS, MAX_NUM_VENDAS)

    if seed:
        seed = int(seed)

    generate_sales_dataset(year, month, num_vendas, seed)

if __name__ == "__main__":
    main()
