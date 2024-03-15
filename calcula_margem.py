produtos = [
    {'produto': 'Acém', 'categoria': 'Carnes', 'subcategoria': 'Bovinos', 'preco': 29.90},
    {'produto': 'Peito de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 15.50},
    {'produto': 'Lombo Suíno', 'categoria': 'Carnes', 'subcategoria': 'Suínos', 'preco': 22.70},
    {'produto': 'Cerveja', 'categoria': 'Bebidas', 'subcategoria': 'Alcoólicas', 'preco': 5.90},
    {'produto': 'Refrigerante', 'categoria': 'Bebidas', 'subcategoria': 'Não Alcoólicas', 'preco': 4.50},
    {'produto': 'Detergente', 'categoria': 'Limpeza', 'subcategoria': 'Detergentes', 'preco': 3.20},
    {'produto': 'Desinfetante', 'categoria': 'Limpeza', 'subcategoria': 'Desinfetantes', 'preco': 6.80},
    {'produto': 'Sabão em Pó', 'categoria': 'Limpeza', 'subcategoria': 'Sabão em Pó', 'preco': 8.50},
    {'produto': 'Shampoo', 'categoria': 'Higiene', 'subcategoria': 'Shampoos', 'preco': 12.90},
    {'produto': 'Sabonete', 'categoria': 'Higiene', 'subcategoria': 'Sabonetes', 'preco': 2.30},
    {'produto': 'Pão Francês', 'categoria': 'Padaria', 'subcategoria': 'Pães', 'preco': 3.00},
    {'produto': 'Bolo de Chocolate', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 18.00},
    {'produto': 'Biscoito', 'categoria': 'Padaria', 'subcategoria': 'Biscoitos', 'preco': 5.80},
    {'produto': 'Carne de Sol', 'categoria': 'Carnes', 'subcategoria': 'Bovinos', 'preco': 35.50},
    {'produto': 'Sobrecoxa de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 12.80},
    {'produto': 'Costela Suína', 'categoria': 'Carnes', 'subcategoria': 'Suínos', 'preco': 18.90},
    {'produto': 'Vinho Tinto', 'categoria': 'Bebidas', 'subcategoria': 'Alcoólicas', 'preco': 25.00},
    {'produto': 'Suco de Laranja', 'categoria': 'Bebidas', 'subcategoria': 'Não Alcoólicas', 'preco': 6.20},
    {'produto': 'Lava-louças', 'categoria': 'Limpeza', 'subcategoria': 'Detergentes', 'preco': 4.80},
    {'produto': 'Água Sanitária', 'categoria': 'Limpeza', 'subcategoria': 'Desinfetantes', 'preco': 3.50},
    {'produto': 'Amaciante de Roupas', 'categoria': 'Limpeza', 'subcategoria': 'Sabão em Pó', 'preco': 9.70},
    {'produto': 'Condicionador', 'categoria': 'Higiene', 'subcategoria': 'Shampoos', 'preco': 14.50},
    {'produto': 'Gel de Banho', 'categoria': 'Higiene', 'subcategoria': 'Sabonetes', 'preco': 4.20},
    {'produto': 'Pão Integral', 'categoria': 'Padaria', 'subcategoria': 'Pães', 'preco': 4.50},
    {'produto': 'Torta de Morango', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 22.00},
    {'produto': 'Rosquinhas', 'categoria': 'Padaria', 'subcategoria': 'Biscoitos', 'preco': 3.90},
    {'produto': 'Smart TV 50 polegadas', 'categoria': 'Eletroeletrônicos', 'subcategoria': 'Televisores', 'preco': 2199.99},
    {'produto': 'Notebook', 'categoria': 'Eletroeletrônicos', 'subcategoria': 'Computadores', 'preco': 3499.99},
    {'produto': 'Smartphone', 'categoria': 'Celulares', 'subcategoria': 'Smartphones', 'preco': 1799.99},
    {'produto': 'Tablet', 'categoria': 'Celulares', 'subcategoria': 'Tablets', 'preco': 899.99},
    {'produto': 'Maçã', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.99},
    {'produto': 'Banana', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 2.99},
    {'produto': 'Alface', 'categoria': 'Hortifruti', 'subcategoria': 'Verduras', 'preco': 1.99},
    {'produto': 'Tomate', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 3.49},
    {'produto': 'Coxinha de Frango', 'categoria': 'Padaria', 'subcategoria': 'Salgados', 'preco': 3.50},
    {'produto': 'Bolo de Cenoura', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 16.00},
    {'produto': 'Café', 'categoria': 'Padaria', 'subcategoria': 'Bebidas Quentes', 'preco': 5.00},
    {'produto': 'Leite', 'categoria': 'Laticínios', 'subcategoria': 'Leites', 'preco': 2.50},
    {'produto': 'Queijo', 'categoria': 'Laticínios', 'subcategoria': 'Queijos', 'preco': 9.99},
    {'produto': 'Iogurte', 'categoria': 'Laticínios', 'subcategoria': 'Iogurtes', 'preco': 3.80},
    {'produto': 'Sorvete', 'categoria': 'Sobremesas', 'subcategoria': 'Sorvetes', 'preco': 12.00},
    {'produto': 'Chocolate', 'categoria': 'Sobremesas', 'subcategoria': 'Chocolates', 'preco': 7.50},
    {'produto': 'Pipoca', 'categoria': 'Snacks', 'subcategoria': 'Salgadinhos', 'preco': 2.00},
    {'produto': 'Amendoim', 'categoria': 'Snacks', 'subcategoria': 'Frutos Secos', 'preco': 4.50},
    {'produto': 'Água Mineral', 'categoria': 'Bebidas', 'subcategoria': 'Águas', 'preco': 1.50},
    {'produto': 'Vassoura', 'categoria': 'Limpeza', 'subcategoria': 'Utensílios de Limpeza', 'preco': 12.00},
    {'produto': 'Escova de Dentes', 'categoria': 'Higiene', 'subcategoria': 'Escovas de Dentes', 'preco': 3.90},
    {'produto': 'Desodorante', 'categoria': 'Higiene', 'subcategoria': 'Desodorantes', 'preco': 8.80},
    {'produto': 'Cebola', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 2.29},
    {'produto': 'Batata', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 2.99},
    {'produto': 'Cenoura', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 1.79},
    {'produto': 'Pimentão', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 3.99},
    {'produto': 'Melancia', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.00},
    {'produto': 'Abacaxi', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.50},
    {'produto': 'Uva', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 8.00},
    {'produto': 'Limão', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 3.50},
    {'produto': 'Mamão', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.50},
    {'produto': 'Laranja', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 2.00},
    {'produto': 'Pêssego', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.00},
    {'produto': 'Abacate', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.00},
    {'produto': 'Kiwi', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.00},
]

# Margem de lucro pretendida por categoria
margem_lucro = {
    'Carnes': 0.45,  # 45%
    'Bebidas': 0.30,  # 30%
    'Limpeza': 0.50,  # 50%
    'Higiene': 0.40,  # 40%
    'Padaria': 0.35,  # 35%
    'Eletroeletrônicos': 0.20,  # 20%
    'Celulares': 0.25,  # 25%
    'Hortifruti': 0.30,  # 30%
    'Laticínios': 0.35,  # 35%
    'Sobremesas': 0.40,  # 40%
    'Snacks': 0.45  # 45%
}

# Calculando e atribuindo os novos preços com base na margem de lucro
for produto in produtos:
    categoria = produto['categoria']
    margem = margem_lucro.get(categoria, 0)  # Se a categoria não estiver definida, a margem será 0%
    preco_custo = produto['preco']
    preco_venda = round(preco_custo * (1 + margem), 2)
    produto['preco_de_custo'] = round(preco_custo, 2)
    produto['preco'] = preco_venda

# Imprimindo os produtos atualizados
for produto in produtos:
    print(produto)
    
    
# Salvando os produtos em um arquivo lista_produtos.py
with open('lista_produtos.py', 'w') as arquivo:
    arquivo.write('produtos = ' + str(produtos))

