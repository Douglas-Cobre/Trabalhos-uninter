#Questão 03: Copiadora

#Procedimentos
def escolha_servico():#Registra qual é a operação e seu custo #Exigência de código 2
    while True:#Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        print('Entre com o tipo de serviço desejado')
        print('DIG - Digitalização')
        print('ICO - Impressão colorida')
        print('IPB - Impressão em preto e branco')
        print('FOT - Fotocópia')
        op = input('>>')
        if (op == 'dig'):
            custo = 1.10
            return custo
        elif(op == 'ico'):
            custo = 1
            return custo
        elif(op == 'ipb'):
            custo = 0.40
            return custo
        elif(op == 'fot'):
            custo = 0.20
            return custo
        else:
            print('Opção inválida, entre com o tipo de serviço novamente')
            print()
            
def num_pagina():#Registra o número de páginas #Exigência de código 3
    while True:#Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        try:#Exigência de código 6
            num = int(input('Entra com o número de páginas:'))
            if (num >20000):
                print('Não aceitamos tantas páginas de uma vez')
                print('Entre com o número de páginas novamente')
                print()
            elif(num == 0):
                print('Valor inválido, entre com o número de páginas novamente')
                print()
            else:
                return num
        except ValueError:
            print('Valor inválido, entre com o número de páginas novamente')
            print()
        
def servico_extra():#Adiciona algum custo extra, caso o usuário queira algo à mais #Exigência de código 4
    while True:#Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        print('Deseja adicionar algum serviço?')
        print('1 - Encadernação simples - R$ 15,00')
        print('2 - Encadernação capa dura - R$ 40,00')    
        print('0 - Não desejo mais nada')
        try:
            op = int(input('>>')) 
            if (op == 1):
                extra = 15
                return extra
            elif(op == 2):
                extra = 40
                return extra
            elif(op == 0):
                extra = 0
                return extra
            else:
                print('Opção inválida, escolha novamnete')
                print()
        except ValueError:
            print('Opção inválida, escolha novamnete')
            print()   

def desconto(n):#Caso o número de paginas cumpra alguma condição, essa função calcula um desconto
    if (n >= 20 and n < 200):
        desc = 15
        return desc
    elif(n >= 200 and n < 2000):
        desc = 20
        return desc
    elif(n >= 2000 and n < 20000):
        desc = 25
        return desc           
    
            
#Programa principal             
print('+----------------------------+')
print('| Copíadora do Douglas Cobre |')#Exigência de código 1
print('+----------------------------+')
   
#Essas varíveis serão usadas para calcular o total a pagar e chamarãoas funções     
servico = escolha_servico()
num = num_pagina()
extra = servico_extra()
desc_porcento = desconto(num)

#Cálculos
total = ((servico*num)+extra) #Valor sem desconto
descontos = total*(desc_porcento/100) #Quanto vale o desconto
final = total - descontos #Valor a pagar
print('+-----------------------------------------------------------------------------+')
print(f' Total: R$ {final:.2f} (Serviço: R${servico:.2f} * páginas:{num} + extra: R${extra:.2f} desconto: {desc_porcento}%)')#Exigência de código 5
print('+-----------------------------------------------------------------------------+')


