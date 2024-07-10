#Exemplo de função com Passagem de parâmetro
def realce(x):
    print('|----|')
    print(x)
    print('|----|')
    
realce(' Menu ')

#Exemplo de função com modificação de String
def destaque(palavra):
    print('+' , '-'*len(palavra) , '+')
    print(f'| {palavra} |')
    print('+' , '-'*len(palavra) , '+')
    
destaque('Douglas')

#Exemplo de função LAMBDA (função simplificada)
conta = lambda x , y : (x+5)*y
print(conta(5,2)) #Não precisa endentar

#Função FATORIAL
def fatorial(n):
    c = n
    fat = n
    while (c>1):
        c = c-1
        fat = fat*c
    print(f'O fatorial de {x} é {fat}') #Fora do while para evitar looping
        
x = int(input('Digite um número: '))
if(x > 0):
    fatorial(x) #Chama a função
else:
    print('Valor inválido')