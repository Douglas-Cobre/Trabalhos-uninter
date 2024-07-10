#Questão 01: Caixa de atacado

print('+-----------------------------------+')
print('| Bem-vindo à loja do Douglas Cobre |')#Exigência de código 1
print('+-----------------------------------+')

#Exigência de código 2
preco = float(input('| Valor do produto: ')) #Entrada de dados do preço
qtd = int(input('| Quantidade do produto: '))#Entrada de dados da quantidade
valor = preco*qtd
desc = 0

#Exigência de código 3 
#Essa sequência de condições verifica se o valor corresponde à algum tipo de desconto
if(valor < 2500 ):#Exigência de código 7
    desc = 0
elif(valor >= 2500 and valor <6000):
    desc = 4
elif(valor >= 6000 and valor <10000):
    desc = 7
else:
    desc = 11

#Calculo dos descontos e criação da variável de desconto
valor_desconto = valor*(desc/100)
total = valor-valor_desconto

#Exigência de código 4
#Saída dos resultados com valores à pagar
print('+------------------------------+')
print(f'| Valor SEM desconto: {valor:.2f}')
print('+------------------------------+')
print(f'| Valor COM desconto: {total:.2f}')  
print('+------------------------------+')