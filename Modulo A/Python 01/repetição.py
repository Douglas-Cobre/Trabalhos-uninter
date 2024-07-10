#Cole os exemplos na página de teste.py para ver o resultado

#1ºExemplo de WHILE
inicio = int(input('Começo da contagem: '))
fim = int(input('Final da contagem: '))

if (inicio != fim):
    if (inicio < fim):
        while (inicio <= fim):
            print(inicio)
            inicio = inicio + 1
    elif (fim < inicio):
        while(fim <= inicio):
            print(inicio)
            inicio = inicio - 1
else:
    print('Valor inválido')
    
    
#2º Exemplo de WHILE
c = 0
soma = 0
while (c < 5):
    c = c + 1
    nota = int(input(f'Digite a {c}º nota: '))
    soma = nota + soma
media = soma/5
print(f'Média final: {media}')    


#1º Exemplo de FOR
for i in range(6):
    print(i) 
    
    
#2º Exemplo de FOR
for i in range(10 , -1 , -1):
    print(i) 
    
#3º Exemplo de FOR (Varredura de String)
frase = "Olá, Mundo!"
for i in range (0 , len(frase) , 1):
    print(frase[i] , end ="")
    
#Exemplo de repetição (Tabuada)
c = 0
while (c<=10):
    print('---------------')
    print(f'Tabuada do {c}')
    print('---------------')
    for i in range (0 , 11 , 1):
        res = c*i
        print(f'{c}X{i}={res}')
    c += 1 
    
#Exemplo de while e if (Menu)
p = 0

while True:
    print('1 - Coxinha R$5,00')
    print('2 - Patel R$8,00')
    print('3 - Empadão R$15,00')
    print('4 - Refri lata R$5,00')
    print('5 - PAGAR')
    
    op = int(input('Digite o código do pruduto: '))
 
    if(op == 1):
        qtd = int(input('Quantidade:'))
        p = p + 5*qtd
    elif(op == 2):
        qtd =int(input('Quantidade:')) 
        p = p + 8*qtd
    elif (op == 3):
        qtd = int(input('Quantidade:'))
        p = p + 15*qtd
    elif (op == 4):
        qtd = int(input('Quantidade:'))
        p = p + 5*qtd
    elif (op == 5):
        break
    else:
        print('Código inválido')

print(f'Total a pagar: {p}')

