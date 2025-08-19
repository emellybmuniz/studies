# Print com uma mensagem de boas-vindas, incluindo meu nome e sobrenome.
nome, sobrenome = 'Emelly Beatriz', 'Pereira'
print(f"\nSeja bem-vindo(a) à loja da {nome} {sobrenome}!")

# 2. Recebendo o valor unitário e a quantidade do produto.
try:
    valor_unit = float(input('Digite o valor unitário do produto: '))
    qnt_produto = int(input('Digite a quantidade do produto: '))
    
    # 3. Implementando lógica de desconto.
    if qnt_produto == 0:
        valor_total = valor_unit
    else:
        valor_total = valor_unit * qnt_produto 
    
    if valor_total >= 10000:
        desconto = 11
        
    elif 6000 <= valor_total < 10000:
        desconto = 7
        
    elif 2500 <= valor_total < 6000:
        desconto = 4
        
    else:
        desconto = 0
        
    # Calculando desconto
    valor_desconto = valor_total * (desconto / 100)
    valor_descontado = valor_total - valor_desconto

    # Calculando e exibindo os valores sem desconto e com desconto (unitário e por quantidade).
    print('\n=== Valores Finais ===') 

    if valor_total >= 2500:
        print(f'Desconto aplicado de {desconto}%')  
        print(f'Valor do produto (com desconto): R$ {valor_descontado:.2f}')
    else:
        print('Nenhum desconto aplicado.')
        
    print(f'Valor do produto sem desconto: R$ {valor_total:.2f}') 

except ValueError:
    print('Entrada Inválida.')
    

