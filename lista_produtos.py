produtos = [
    {'produto': 'Acém', 'categoria': 'Carnes', 'subcategoria': 'Bovinos', 'preco': 43.35, 'preco_de_custo': 29.9, 'unidade': 'kg'},
    {'produto': 'Peito de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 22.47, 'preco_de_custo': 15.5, 'unidade': 'kg'},
    {'produto': 'Lombo Suíno', 'categoria': 'Carnes', 'subcategoria': 'Suínos', 'preco': 32.91, 'preco_de_custo': 22.7, 'unidade': 'kg'},
    {'produto': 'Cerveja', 'categoria': 'Bebidas', 'subcategoria': 'Alcoólicas', 'preco': 7.67, 'preco_de_custo': 5.9, 'unidade': 'unidades'}, 
    {'produto': 'Refrigerante', 'categoria': 'Bebidas', 'subcategoria': 'Não Alcoólicas', 'preco': 5.85, 'preco_de_custo': 4.5, 'unidade': 'litros'}, 
    {'produto': 'Detergente', 'categoria': 'Limpeza', 'subcategoria': 'Detergentes', 'preco': 4.8, 'preco_de_custo': 3.2, 'unidade': 'litros'},
    {'produto': 'Desinfetante', 'categoria': 'Limpeza', 'subcategoria': 'Desinfetantes', 'preco': 10.2, 'preco_de_custo': 6.8, 'unidade': 'litros'}, 
    {'produto': 'Sabão em Pó', 'categoria': 'Limpeza', 'subcategoria': 'Sabão em Pó', 'preco': 12.75, 'preco_de_custo': 8.5, 'unidade': 'kg'},
    {'produto': 'Shampoo', 'categoria': 'Higiene', 'subcategoria': 'Shampoos', 'preco': 18.06, 'preco_de_custo': 12.9, 'unidade': 'litros'}, 
    {'produto': 'Sabonete', 'categoria': 'Higiene', 'subcategoria': 'Sabonetes', 'preco': 3.22, 'preco_de_custo': 2.3, 'unidade': 'unidades'},
    {'produto': 'Pão Francês', 'categoria': 'Padaria', 'subcategoria': 'Pães', 'preco': 4.05, 'preco_de_custo': 3.0, 'unidade': 'unidades'}, 
    {'produto': 'Bolo de Chocolate', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 24.3, 'preco_de_custo': 18.0, 'unidade': 'kg'}, 
    {'produto': 'Biscoito', 'categoria': 'Padaria', 'subcategoria': 'Biscoitos', 'preco': 7.83, 'preco_de_custo': 5.8, 'unidade': 'kg'}, 
    {'produto': 'Carne de Sol', 'categoria': 'Carnes', 'subcategoria': 'Bovinos', 'preco': 51.48, 'preco_de_custo': 35.5, 'unidade': 'kg'}, 
    {'produto': 'Sobrecoxa de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 18.56, 'preco_de_custo': 12.8, 'unidade': 'kg'}, 
    {'produto': 'Costela Suína', 'categoria': 'Carnes', 'subcategoria': 'Suínos', 'preco': 27.4, 'preco_de_custo': 18.9, 'unidade': 'kg'}, 
    {'produto': 'Vinho Tinto', 'categoria': 'Bebidas', 'subcategoria': 'Alcoólicas', 'preco': 32.5, 'preco_de_custo': 25.0, 'unidade': 'litros'}, 
    {'produto': 'Suco de Laranja', 'categoria': 'Bebidas', 'subcategoria': 'Não Alcoólicas', 'preco': 8.06, 'preco_de_custo': 6.2, 'unidade': 'litros'}, 
    {'produto': 'Lava-louças', 'categoria': 'Limpeza', 'subcategoria': 'Detergentes', 'preco': 7.2, 'preco_de_custo': 4.8, 'unidade': 'litros'}, 
    {'produto': 'Água Sanitária', 'categoria': 'Limpeza', 'subcategoria': 'Desinfetantes', 'preco': 5.25, 'preco_de_custo': 3.5, 'unidade': 'litros'}, 
    {'produto': 'Amaciante de Roupas', 'categoria': 'Limpeza', 'subcategoria': 'Sabão em Pó', 'preco': 14.55, 'preco_de_custo': 9.7, 'unidade': 'litros'},
    {'produto': 'Condicionador', 'categoria': 'Higiene', 'subcategoria': 'Shampoos', 'preco': 20.3, 'preco_de_custo': 14.5, 'unidade': 'litros'},
    {'produto': 'Gel de Banho', 'categoria': 'Higiene', 'subcategoria': 'Sabonetes', 'preco': 5.88, 'preco_de_custo': 4.2, 'unidade': 'litros'},
    {'produto': 'Pão Integral', 'categoria': 'Padaria', 'subcategoria': 'Pães', 'preco': 6.08, 'preco_de_custo': 4.5, 'unidade': 'unidades'},
    {'produto': 'Torta de Morango', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 29.7, 'preco_de_custo': 22.0, 'unidade': 'kg'}, 
    {'produto': 'Rosquinhas', 'categoria': 'Padaria', 'subcategoria': 'Biscoitos', 'preco': 5.27, 'preco_de_custo': 3.9, 'unidade': 'kg'},
    {'produto': 'Smart TV 50 polegadas', 'categoria': 'Eletroeletrônicos', 'subcategoria': 'Televisores', 'preco': 2639.99, 'preco_de_custo': 2199.99, 'unidade': 'unidades'}, 
    {'produto': 'Notebook', 'categoria': 'Eletroeletrônicos', 'subcategoria': 'Computadores', 'preco': 4199.99, 'preco_de_custo': 3499.99, 'unidade': 'unidades'}, 
    {'produto': 'Smartphone', 'categoria': 'Celulares', 'subcategoria': 'Smartphones', 'preco': 2249.99, 'preco_de_custo': 1799.99, 'unidade': 'unidades'}, 
    {'produto': 'Tablet', 'categoria': 'Celulares', 'subcategoria': 'Tablets', 'preco': 1124.99, 'preco_de_custo': 899.99, 'unidade': 'unidades'},
    {'produto': 'Maçã', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.49, 'preco_de_custo': 4.99, 'unidade': 'kg'}, 
    {'produto': 'Banana', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 3.89, 'preco_de_custo': 2.99, 'unidade': 'kg'},
    {'produto': 'Alface', 'categoria': 'Hortifruti', 'subcategoria': 'Verduras', 'preco': 2.59, 'preco_de_custo': 1.99, 'unidade': 'unidades'},
    {'produto': 'Tomate', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 4.54, 'preco_de_custo': 3.49, 'unidade': 'kg'}, 
    {'produto': 'Coxinha de Frango', 'categoria': 'Padaria', 'subcategoria': 'Salgados', 'preco': 4.73, 'preco_de_custo': 3.5, 'unidade': 'unidades'}, 
    {'produto': 'Bolo de Cenoura', 'categoria': 'Padaria', 'subcategoria': 'Bolos', 'preco': 21.6, 'preco_de_custo': 16.0, 'unidade': 'kg'},
    {'produto': 'Café', 'categoria': 'Padaria', 'subcategoria': 'Bebidas Quentes', 'preco': 6.75, 'preco_de_custo': 5.0, 'unidade': 'kg'},
    {'produto': 'Leite', 'categoria': 'Laticínios', 'subcategoria': 'Leites', 'preco': 3.38, 'preco_de_custo': 2.5, 'unidade': 'litros'}, 
    {'produto': 'Queijo', 'categoria': 'Laticínios', 'subcategoria': 'Queijos', 'preco': 13.49, 'preco_de_custo': 9.99, 'unidade': 'kg'}, 
    {'produto': 'Iogurte', 'categoria': 'Laticínios', 'subcategoria': 'Iogurtes', 'preco': 5.13, 'preco_de_custo': 3.8, 'unidade': 'litros'}, 
    {'produto': 'Sorvete', 'categoria': 'Sobremesas', 'subcategoria': 'Sorvetes', 'preco': 16.8, 'preco_de_custo': 12.0, 'unidade': 'litros'},
    {'produto': 'Chocolate', 'categoria': 'Sobremesas', 'subcategoria': 'Chocolates', 'preco': 10.5, 'preco_de_custo': 7.5, 'unidade': 'kg'},
    {'produto': 'Pipoca', 'categoria': 'Snacks', 'subcategoria': 'Salgadinhos', 'preco': 2.9, 'preco_de_custo': 2.0, 'unidade': 'kg'},
    {'produto': 'Amendoim', 'categoria': 'Snacks', 'subcategoria': 'Frutos Secos', 'preco': 6.52, 'preco_de_custo': 4.5, 'unidade': 'kg'},
    {'produto': 'Água Mineral', 'categoria': 'Bebidas', 'subcategoria': 'Águas', 'preco': 1.95, 'preco_de_custo': 1.5, 'unidade': 'litros'},
    {'produto': 'Vassoura', 'categoria': 'Limpeza', 'subcategoria': 'Utensílios de Limpeza', 'preco': 18.0, 'preco_de_custo': 12.0, 'unidade': 'unidades'}, 
    {'produto': 'Escova de Dentes', 'categoria': 'Higiene', 'subcategoria': 'Escovas de Dentes', 'preco': 5.46, 'preco_de_custo': 3.9, 'unidade': 'unidades'}, 
    {'produto': 'Desodorante', 'categoria': 'Higiene', 'subcategoria': 'Desodorantes', 'preco': 12.32, 'preco_de_custo': 8.8, 'unidade': 'unidades'},
    {'produto': 'Cebola', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 2.98, 'preco_de_custo': 2.29, 'unidade': 'kg'},
    {'produto': 'Batata', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 3.89, 'preco_de_custo': 2.99, 'unidade': 'kg'}, 
    {'produto': 'Cenoura', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 2.33, 'preco_de_custo': 1.79, 'unidade': 'kg'},
    {'produto': 'Pimentão', 'categoria': 'Hortifruti', 'subcategoria': 'Legumes', 'preco': 5.19, 'preco_de_custo': 3.99, 'unidade': 'kg'},
    {'produto': 'Melancia', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.8, 'preco_de_custo': 6.0, 'unidade': 'unidades'}, 
    {'produto': 'Abacaxi', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.85, 'preco_de_custo': 4.5, 'unidade': 'unidades'}, 
    {'produto': 'Uva', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 10.4, 'preco_de_custo': 8.0, 'unidade': 'kg'},
    {'produto': 'Limão', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.55, 'preco_de_custo': 3.5, 'unidade': 'kg'},
    {'produto': 'Mamão', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.15, 'preco_de_custo': 5.5, 'unidade': 'kg'},
    {'produto': 'Laranja', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 2.6, 'preco_de_custo': 2.0, 'unidade': 'kg'}, 
    {'produto': 'Pêssego', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.2, 'preco_de_custo': 4.0, 'unidade': 'kg'},
    {'produto': 'Abacate', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 9.1, 'preco_de_custo': 7.0, 'unidade': 'kg'}, 
    {'produto': 'Kiwi', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.5, 'preco_de_custo': 5.0, 'unidade': 'kg'},
    {'produto': 'Cafeteira Elétrica', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Cafeteiras', 'preco': 99.99, 'preco_de_custo': 79.99, 'unidade': 'unidades'},
    {'produto': 'Ferro de Passar', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Ferro de Passar', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Liquidificador', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Liquidificadores', 'preco': 79.99, 'preco_de_custo': 59.99, 'unidade': 'unidades'},
    {'produto': 'Aspirador de Pó', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Aspiradores', 'preco': 199.99, 'preco_de_custo': 149.99, 'unidade': 'unidades'},
    {'produto': 'Fritadeira Elétrica', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Fritadeiras', 'preco': 129.99, 'preco_de_custo': 99.99, 'unidade': 'unidades'},
    {'produto': 'Panela Elétrica de Arroz', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Panelas Elétricas', 'preco': 89.99, 'preco_de_custo': 69.99, 'unidade': 'unidades'},
    {'produto': 'Ventilador de Mesa', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Ventiladores', 'preco': 69.99, 'preco_de_custo': 49.99, 'unidade': 'unidades'},
    {'produto': 'Micro-ondas', 'categoria': 'Eletrodomésticos', 'subcategoria': 'Micro-ondas', 'preco': 199.99, 'preco_de_custo': 149.99, 'unidade': 'unidades'},
    {'produto': 'Cadeira de Escritório', 'categoria': 'Móveis', 'subcategoria': 'Cadeiras', 'preco': 149.99, 'preco_de_custo': 119.99, 'unidade': 'unidades'},
    {'produto': 'Mesa de Jantar', 'categoria': 'Móveis', 'subcategoria': 'Mesas', 'preco': 299.99, 'preco_de_custo': 249.99, 'unidade': 'unidades'},
    {'produto': 'Sofá de Couro', 'categoria': 'Móveis', 'subcategoria': 'Sofás', 'preco': 599.99, 'preco_de_custo': 499.99, 'unidade': 'unidades'},
    {'produto': 'Guarda-roupa', 'categoria': 'Móveis', 'subcategoria': 'Guarda-roupas', 'preco': 399.99, 'preco_de_custo': 299.99, 'unidade': 'unidades'},
    {'produto': 'Cama de Casal', 'categoria': 'Móveis', 'subcategoria': 'Camas', 'preco': 499.99, 'preco_de_custo': 399.99, 'unidade': 'unidades'},
    {'produto': 'Escrivaninha', 'categoria': 'Móveis', 'subcategoria': 'Mesas', 'preco': 129.99, 'preco_de_custo': 99.99, 'unidade': 'unidades'},
    {'produto': 'Prateleira de Parede', 'categoria': 'Móveis', 'subcategoria': 'Prateleiras', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Tapete', 'categoria': 'Decoração', 'subcategoria': 'Tapetes', 'preco': 79.99, 'preco_de_custo': 59.99, 'unidade': 'metros quadrados'},
    {'produto': 'Quadro Decorativo', 'categoria': 'Decoração', 'subcategoria': 'Quadros', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Vaso de Plantas', 'categoria': 'Decoração', 'subcategoria': 'Vasos', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Lustre', 'categoria': 'Iluminação', 'subcategoria': 'Lustres', 'preco': 149.99, 'preco_de_custo': 119.99, 'unidade': 'unidades'},
    {'produto': 'Abajur', 'categoria': 'Iluminação', 'subcategoria': 'Abajures', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Lâmpada LED', 'categoria': 'Iluminação', 'subcategoria': 'Lâmpadas', 'preco': 9.99, 'preco_de_custo': 7.99, 'unidade': 'unidades'},
    {'produto': 'Spot de Teto', 'categoria': 'Iluminação', 'subcategoria': 'Spots', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Cortina', 'categoria': 'Decoração', 'subcategoria': 'Cortinas', 'preco': 59.99, 'preco_de_custo': 39.99, 'unidade': 'metros'},
    {'produto': 'Tapete de Banheiro', 'categoria': 'Decoração', 'subcategoria': 'Tapetes', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Puff', 'categoria': 'Móveis', 'subcategoria': 'Puffs', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Espelho de Parede', 'categoria': 'Decoração', 'subcategoria': 'Espelhos', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Prato Decorativo', 'categoria': 'Decoração', 'subcategoria': 'Pratos Decorativos', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Cadeira de Praia', 'categoria': 'Lazer', 'subcategoria': 'Cadeiras de Praia', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Bola de Futebol', 'categoria': 'Esportes', 'subcategoria': 'Bolas', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Raquete de Tênis', 'categoria': 'Esportes', 'subcategoria': 'Raquetes', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Prancha de Surf', 'categoria': 'Esportes', 'subcategoria': 'Pranchas', 'preco': 299.99, 'preco_de_custo': 249.99, 'unidade': 'unidades'},
    {'produto': 'Bicicleta', 'categoria': 'Esportes', 'subcategoria': 'Bicicletas', 'preco': 499.99, 'preco_de_custo': 399.99, 'unidade': 'unidades'},
    {'produto': 'Luvas de Boxe', 'categoria': 'Esportes', 'subcategoria': 'Luvas', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Taco de Baseball', 'categoria': 'Esportes', 'subcategoria': 'Tacos', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Cama Elástica', 'categoria': 'Lazer', 'subcategoria': 'Brinquedos', 'preco': 199.99, 'preco_de_custo': 149.99, 'unidade': 'unidades'},
    {'produto': 'Quebra-cabeça', 'categoria': 'Lazer', 'subcategoria': 'Brinquedos', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Piscina Inflável', 'categoria': 'Lazer', 'subcategoria': 'Piscinas', 'preco': 99.99, 'preco_de_custo': 79.99, 'unidade': 'unidades'},
    {'produto': 'Câmera Fotográfica', 'categoria': 'Tecnologia', 'subcategoria': 'Câmeras', 'preco': 299.99, 'preco_de_custo': 249.99, 'unidade': 'unidades'},
    {'produto': 'Smartwatch', 'categoria': 'Tecnologia', 'subcategoria': 'Relógios Inteligentes', 'preco': 149.99, 'preco_de_custo': 119.99, 'unidade': 'unidades'},
    {'produto': 'Fone de Ouvido Bluetooth', 'categoria': 'Tecnologia', 'subcategoria': 'Fones de Ouvido', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Carregador Portátil', 'categoria': 'Tecnologia', 'subcategoria': 'Acessórios', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Teclado sem Fio', 'categoria': 'Tecnologia', 'subcategoria': 'Periféricos', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'unidades'},
    {'produto': 'Roteador Wi-Fi', 'categoria': 'Tecnologia', 'subcategoria': 'Redes', 'preco': 79.99, 'preco_de_custo': 59.99, 'unidade': 'unidades'},
    {'produto': 'Cabo HDMI', 'categoria': 'Tecnologia', 'subcategoria': 'Acessórios', 'preco': 9.99, 'preco_de_custo': 7.99, 'unidade': 'metros'},
    {'produto': 'Smart Speaker', 'categoria': 'Tecnologia', 'subcategoria': 'Caixas de Som', 'preco': 99.99, 'preco_de_custo': 79.99, 'unidade': 'unidades'},
    {'produto': 'Relógio de Parede', 'categoria': 'Decoração', 'subcategoria': 'Relógios', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Manga', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.99, 'preco_de_custo': 4.49, 'unidade': 'kg'},
    {'produto': 'Pera', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.49, 'preco_de_custo': 3.29, 'unidade': 'kg'},
    {'produto': 'Melão', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.99, 'preco_de_custo': 6.49, 'unidade': 'unidades'},
    {'produto': 'Uva Verde', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 9.99, 'preco_de_custo': 7.49, 'unidade': 'kg'},
    {'produto': 'Ameixa', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 8.99, 'preco_de_custo': 6.99, 'unidade': 'kg'},
    {'produto': 'Caju', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.99, 'preco_de_custo': 5.49, 'unidade': 'kg'},
    {'produto': 'Jabuticaba', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 15.99, 'preco_de_custo': 12.99, 'unidade': 'kg'},
    {'produto': 'Jaca', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 8.49, 'preco_de_custo': 6.99, 'unidade': 'kg'},
    {'produto': 'Mamão Papaia', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.99, 'preco_de_custo': 3.79, 'unidade': 'kg'},
    {'produto': 'Carambola', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.49, 'preco_de_custo': 5.99, 'unidade': 'kg'},
    {'produto': 'Caqui', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 10.99, 'preco_de_custo': 8.99, 'unidade': 'kg'},
    {'produto': 'Lichia', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 12.49, 'preco_de_custo': 9.99, 'unidade': 'kg'},
    {'produto': 'Manga Tommy', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.49, 'preco_de_custo': 4.99, 'unidade': 'kg'},
    {'produto': 'Mamão Formosa', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.49, 'preco_de_custo': 3.99, 'unidade': 'kg'},
    {'produto': 'Graviola', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 11.99, 'preco_de_custo': 9.49, 'unidade': 'kg'},
    {'produto': 'Figo', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 14.99, 'preco_de_custo': 11.99, 'unidade': 'kg'},
    {'produto': 'Romã', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 9.99, 'preco_de_custo': 7.99, 'unidade': 'kg'},
    {'produto': 'Maracujá', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 3.99, 'preco_de_custo': 2.99, 'unidade': 'kg'},
    {'produto': 'Pitaya', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 19.99, 'preco_de_custo': 16.99, 'unidade': 'kg'},
    {'produto': 'Tamarindo', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 13.99, 'preco_de_custo': 11.99, 'unidade': 'kg'},
    {'produto': 'Cereja', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 29.99, 'preco_de_custo': 24.99, 'unidade': 'kg'},
    {'produto': 'Pêssego', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.99, 'preco_de_custo': 5.49, 'unidade': 'kg'},
    {'produto': 'Amora', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 17.99, 'preco_de_custo': 14.99, 'unidade': 'kg'},
    {'produto': 'Physalis', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 39.99, 'preco_de_custo': 34.99, 'unidade': 'kg'},
    {'produto': 'Coco', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 7.99, 'preco_de_custo': 6.49, 'unidade': 'unidades'},
    {'produto': 'Kiwi', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 11.99, 'preco_de_custo': 9.99, 'unidade': 'kg'},
    {'produto': 'Tangerina', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 3.49, 'preco_de_custo': 2.49, 'unidade': 'kg'},
    {'produto': 'Limão Siciliano', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 5.49, 'preco_de_custo': 4.49, 'unidade': 'kg'},
    {'produto': 'Limão Taiti', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 2.99, 'preco_de_custo': 1.99, 'unidade': 'kg'},
    {'produto': 'Limão Cravo', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 6.99, 'preco_de_custo': 5.49, 'unidade': 'kg'},
    {'produto': 'Cereja do Rio Grande', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 39.99, 'preco_de_custo': 34.99, 'unidade': 'kg'},
    {'produto': 'Mirtilo', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 22.99, 'preco_de_custo': 19.99, 'unidade': 'kg'},
    {'produto': 'Nectarina', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 9.99, 'preco_de_custo': 7.99, 'unidade': 'kg'},
    {'produto': 'Damasco', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 12.99, 'preco_de_custo': 10.99, 'unidade': 'kg'},
    {'produto': 'Cereja Espanhola', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 44.99, 'preco_de_custo': 39.99, 'unidade': 'kg'},
    {'produto': 'Cereja Chilena', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 49.99, 'preco_de_custo': 44.99, 'unidade': 'kg'},
    {'produto': 'Cereja Argentina', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 34.99, 'preco_de_custo': 29.99, 'unidade': 'kg'},
    {'produto': 'Cereja Americana', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 54.99, 'preco_de_custo': 49.99, 'unidade': 'kg'},
    {'produto': 'Pitanga', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 19.99, 'preco_de_custo': 16.99, 'unidade': 'kg'},
    {'produto': 'Banana Prata', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 3.99, 'preco_de_custo': 2.99, 'unidade': 'kg'},
    {'produto': 'Banana Nanica', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 2.99, 'preco_de_custo': 1.99, 'unidade': 'kg'},
    {'produto': 'Banana da Terra', 'categoria': 'Hortifruti', 'subcategoria': 'Frutas', 'preco': 4.99, 'preco_de_custo': 3.99, 'unidade': 'kg'},
    {'produto': 'Vestido Floral', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 59.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Calça Jeans Skinny', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 49.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Camiseta Básica', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 19.99, 'preco_de_custo': 12.99, 'unidade': 'unidades'},
    {'produto': 'Camisa Social', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 39.99, 'preco_de_custo': 24.99, 'unidade': 'unidades'},
    {'produto': 'Blazer Slim', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 89.99, 'preco_de_custo': 59.99, 'unidade': 'unidades'},
    {'produto': 'Vestido de Festa', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 99.99, 'preco_de_custo': 69.99, 'unidade': 'unidades'},
    {'produto': 'Sapato Social', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 79.99, 'preco_de_custo': 49.99, 'unidade': 'unidades'},
    {'produto': 'Bolsa de Couro', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 69.99, 'preco_de_custo': 44.99, 'unidade': 'unidades'},
    {'produto': 'Saia Midi', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 39.99, 'preco_de_custo': 24.99, 'unidade': 'unidades'},
    {'produto': 'Blusa Estampada', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Terno Slim', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 149.99, 'preco_de_custo': 99.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Longo', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 79.99, 'preco_de_custo': 54.99, 'unidade': 'unidades'},
    {'produto': 'Calça Social', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 59.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Jaqueta de Couro', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 129.99, 'preco_de_custo': 89.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Tubinho', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 49.99, 'preco_de_custo': 34.99, 'unidade': 'unidades'},
    {'produto': 'Camiseta Estampada', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 24.99, 'preco_de_custo': 16.99, 'unidade': 'unidades'},
    {'produto': 'Calça Legging', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 34.99, 'preco_de_custo': 22.99, 'unidade': 'unidades'},
    {'produto': 'Tênis Esportivo', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 69.99, 'preco_de_custo': 44.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Rodado', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 54.99, 'preco_de_custo': 36.99, 'unidade': 'unidades'},
    {'produto': 'Gravata Slim', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Sandália Rasteira', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 39.99, 'preco_de_custo': 26.99, 'unidade': 'unidades'},
    {'produto': 'Camisa Polo', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 34.99, 'preco_de_custo': 22.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Midi', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 64.99, 'preco_de_custo': 42.99, 'unidade': 'unidades'},
    {'produto': 'Moletom com Capuz', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 49.99, 'preco_de_custo': 32.99, 'unidade': 'unidades'},
    {'produto': 'Sapatênis Casual', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 59.99, 'preco_de_custo': 39.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Chemise', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 44.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Regata Básica', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 14.99, 'preco_de_custo': 9.99, 'unidade': 'unidades'},
    {'produto': 'Blazer Casual', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 74.99, 'preco_de_custo': 49.99, 'unidade': 'unidades'},
    {'produto': 'Bermuda Jeans', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Ciganinha', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 39.99, 'preco_de_custo': 26.99, 'unidade': 'unidades'},
    {'produto': 'Suéter de Tricô', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 54.99, 'preco_de_custo': 36.99, 'unidade': 'unidades'},
    {'produto': 'Saia Lápis', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 34.99, 'preco_de_custo': 22.99, 'unidade': 'unidades'},
    {'produto': 'Shorts Jeans', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 24.99, 'preco_de_custo': 16.99, 'unidade': 'unidades'},
    {'produto': 'Cinto de Couro', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 19.99, 'preco_de_custo': 12.99, 'unidade': 'unidades'},
    {'produto': 'Blusa de Tricô', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 34.99, 'preco_de_custo': 22.99, 'unidade': 'unidades'},
    {'produto': 'Calça Cargo', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 44.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Blusê', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 49.99, 'preco_de_custo': 32.99, 'unidade': 'unidades'},
    {'produto': 'Camisa Xadrez', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'unidades'},
    {'produto': 'Cardigan de Lã', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 44.99, 'preco_de_custo': 29.99, 'unidade': 'unidades'},
    {'produto': 'Calça Jogger', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 39.99, 'preco_de_custo': 26.99, 'unidade': 'unidades'},
    {'produto': 'Vestido Bandagem', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 54.99, 'preco_de_custo': 36.99, 'unidade': 'unidades'},
    {'produto': 'Camiseta Manga Longa', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 24.99, 'preco_de_custo': 16.99, 'unidade': 'unidades'},
    {'produto': 'Blusa Ciganinha', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 34.99, 'preco_de_custo': 22.99, 'unidade': 'unidades'},
    {'produto': 'Calça Chino', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Masculino', 'preco': 49.99, 'preco_de_custo': 32.99, 'unidade': 'unidades'},
    {'produto': 'Vestido de Renda', 'categoria': 'Moda e Vestuário', 'subcategoria': 'Feminino', 'preco': 64.99, 'preco_de_custo': 42.99, 'unidade': 'unidades'},
    {'produto': 'Picanha', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 69.99, 'preco_de_custo': 49.99, 'unidade': 'kg'},
    {'produto': 'Costela', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 54.99, 'preco_de_custo': 39.99, 'unidade': 'kg'},
    {'produto': 'Filé Mignon', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 79.99, 'preco_de_custo': 59.99, 'unidade': 'kg'},
    {'produto': 'Alcatra', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 64.99, 'preco_de_custo': 46.99, 'unidade': 'kg'},
    {'produto': 'Coxão Mole', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 59.99, 'preco_de_custo': 42.99, 'unidade': 'kg'},
    {'produto': 'Contrafilé', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 74.99, 'preco_de_custo': 52.99, 'unidade': 'kg'},
    {'produto': 'Maminha', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 62.99, 'preco_de_custo': 44.99, 'unidade': 'kg'},
    {'produto': 'Linguiça Toscana', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 34.99, 'preco_de_custo': 24.99, 'unidade': 'kg'},
    {'produto': 'Pernil', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'kg'},
    {'produto': 'Costelinha de Porco', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 49.99, 'preco_de_custo': 34.99, 'unidade': 'kg'},
    {'produto': 'Lombo', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 44.99, 'preco_de_custo': 31.99, 'unidade': 'kg'},
    {'produto': 'Bisteca Suína', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 29.99, 'preco_de_custo': 21.99, 'unidade': 'kg'},
    {'produto': 'Coxa de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 24.99, 'preco_de_custo': 17.99, 'unidade': 'kg'},
    {'produto': 'Peito de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 22.99, 'preco_de_custo': 15.99, 'unidade': 'kg'},
    {'produto': 'Asa de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 19.99, 'preco_de_custo': 13.99, 'unidade': 'kg'},
    {'produto': 'Sobrecoxa de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 29.99, 'preco_de_custo': 21.99, 'unidade': 'kg'},
    {'produto': 'Coxa de Peru', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'kg'},
    {'produto': 'Peito de Peru', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 49.99, 'preco_de_custo': 39.99, 'unidade': 'kg'},
    {'produto': 'Salsicha de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 14.99, 'preco_de_custo': 9.99, 'unidade': 'kg'},
    {'produto': 'Bife de Alcatra', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 64.99, 'preco_de_custo': 47.99, 'unidade': 'kg'},
    {'produto': 'Linguiça de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 19.99, 'preco_de_custo': 13.99, 'unidade': 'kg'},
    {'produto': 'Paleta de Cordeiro', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 89.99, 'preco_de_custo': 74.99, 'unidade': 'kg'},
    {'produto': 'Carne de Hambúrguer', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 29.99, 'preco_de_custo': 21.99, 'unidade': 'kg'},
    {'produto': 'Linguiça Toscana de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 24.99, 'preco_de_custo': 17.99, 'unidade': 'kg'},
    {'produto': 'Bacon Fatiado', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 34.99, 'preco_de_custo': 24.99, 'unidade': 'kg'},
    {'produto': 'Cupim', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 54.99, 'preco_de_custo': 39.99, 'unidade': 'kg'},
    {'produto': 'Picanha Argentina', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 79.99, 'preco_de_custo': 59.99, 'unidade': 'kg'},
    {'produto': 'Músculo', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 34.99, 'preco_de_custo': 24.99, 'unidade': 'kg'},
    {'produto': 'Contrafilé de Cordeiro', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 69.99, 'preco_de_custo': 54.99, 'unidade': 'kg'},
    {'produto': 'Carré de Cordeiro', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 84.99, 'preco_de_custo': 69.99, 'unidade': 'kg'},
    {'produto': 'Pernil de Cordeiro', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 74.99, 'preco_de_custo': 59.99, 'unidade': 'kg'},
    {'produto': 'Fígado de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 12.99, 'preco_de_custo': 7.99, 'unidade': 'kg'},
    {'produto': 'Rabo', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'kg'},
    {'produto': 'Coxão Duro', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 49.99, 'preco_de_custo': 34.99, 'unidade': 'kg'},
    {'produto': 'Fraldinha', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 44.99, 'preco_de_custo': 31.99, 'unidade': 'kg'},
    {'produto': 'Lagarto', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 59.99, 'preco_de_custo': 44.99, 'unidade': 'kg'},
    {'produto': 'Cordeiro Desossado', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 94.99, 'preco_de_custo': 79.99, 'unidade': 'kg'},
    {'produto': 'Lombo Suíno', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 44.99, 'preco_de_custo': 31.99, 'unidade': 'kg'},
    {'produto': 'Linguiça de Cordeiro', 'categoria': 'Carnes', 'subcategoria': 'Ovinos', 'preco': 29.99, 'preco_de_custo': 19.99, 'unidade': 'kg'},
    {'produto': 'Peito de Pato', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 64.99, 'preco_de_custo': 49.99, 'unidade': 'kg'},
    {'produto': 'Rabo de Porco', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 24.99, 'preco_de_custo': 17.99, 'unidade': 'kg'},
    {'produto': 'Linguiça de Peru', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 19.99, 'preco_de_custo': 13.99, 'unidade': 'kg'},
    {'produto': 'Coração de Frango', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 16.99, 'preco_de_custo': 11.99, 'unidade': 'kg'},
    {'produto': 'Barriga de Porco', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 29.99, 'preco_de_custo': 21.99, 'unidade': 'kg'},
    {'produto': 'Filé de Pato', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 74.99, 'preco_de_custo': 59.99, 'unidade': 'kg'},
    {'produto': 'Pato Inteiro', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 89.99, 'preco_de_custo': 74.99, 'unidade': 'kg'},
    {'produto': 'Peito de Codorna', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 39.99, 'preco_de_custo': 29.99, 'unidade': 'kg'},
    {'produto': 'Codorna Inteira', 'categoria': 'Carnes', 'subcategoria': 'Aves', 'preco': 54.99, 'preco_de_custo': 39.99, 'unidade': 'kg'},
    {'produto': 'Rabo de Boi', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 24.99, 'preco_de_custo': 17.99, 'unidade': 'kg'},
    {'produto': 'Fígado de Boi', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 19.99, 'preco_de_custo': 14.99, 'unidade': 'kg'},
    {'produto': 'Língua de Boi', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 34.99, 'preco_de_custo': 24.99, 'unidade': 'kg'},
    {'produto': 'Mocotó', 'categoria': 'Carnes', 'subcategoria': 'Bovina', 'preco': 29.99, 'preco_de_custo': 21.99, 'unidade': 'kg'},
    {'produto': 'Orelha de Porco', 'categoria': 'Carnes', 'subcategoria': 'Suína', 'preco': 14.99, 'preco_de_custo': 9.99, 'unidade': 'kg'},
]