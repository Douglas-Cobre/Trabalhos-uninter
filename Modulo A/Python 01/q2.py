#Questão 02

#Verifica o sabor
def valida_sabor(pergunta , op1 , op2):
    print('+---------------------+')
    s = input(pergunta)
    while True: #Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        if(s == op1):
            break#Exigência de código 7
        elif(s == op2):
            break
        else:
            print('Opção inválida')#Exigência de código 2
            print()
            s = input(pergunta)
            continue
    return s

#Verifica o tamanho
def valida_tamanho(pergunta , op1 , op2 , op3):
    t = input(pergunta)
    while True: #Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        if(t == op1):
            break
        elif(t == op2):
            break
        elif(t == op3):
            break
        else:
            print('Opção inválida')#Exigência de código 3
            print()
            t = input(pergunta)
            continue
    return t

#Verifica as opções do cliente e calcula o valor a ser pago
def menu_caixa():
    acumulador = 0 #Essa variável irá acumular o valor dos pedidos #Exigência de código 5
    res = 'S'
    while (res == 'S'): #Até que o usuário responda N para encerrar, o programa repetirá o processo
        sabor = valida_sabor('Escolha o sabor(CP/AC): ' , 'CP' , 'AC')
        print(f'Sabor selecionado: {sabor}')
        tamanho = valida_tamanho('Escolha o tamanho (P/M/G): ' , 'P' , 'M' , 'G')
        print(f'Tamanho selecionado: {tamanho}')
        if(sabor == 'CP'):#Exigência de código 4
            if(tamanho == 'P'):
                acumulador += 9.00
            elif(tamanho == 'M'):
                acumulador += 14.00
            elif(tamanho == 'G'):
                acumulador += 18.00
        elif(sabor == 'AC'):
            if(tamanho == 'P'):
                acumulador += 11.00
            elif(tamanho == 'M'):
                acumulador += 16.00
            elif(tamanho == 'G'):
                acumulador += 20.00
        print('+----------------------------------+')
        res = input('Deseja pedir mais alguma coisa?(S/N)')
        if (res == 'N'):#Exigência de código 6
            print(f'Total a pagar: R${acumulador}')
            break
        elif(res =='S'):
            continue
        else:
            while True: #Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
                print('Opção inválida, tente novamente')
                res = input('Deseja pedir mais alguma coisa?(S/N)')
                if (res == 'N'):#Exigência de código 6
                    print(f'Total a pagar: R${acumulador}')
                    break
                elif(res =='S'):
                    continue
            
    
#Menu de boas-vindas
print('Bem-vindo a loja de Gelados do Douglas Cobre')#Exigência de código 1
print('------------------Cardápio------------------')
print('--------------------------------------------')
print('---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---')
print('---|    P    |   R$  9,00   | R$ 11.00  |---')
print('---|    M    |   R$ 14,00   | R$ 16.00  |---')
print('---|    G    |   R$ 18,00   | R$ 20.00  |---')
print('--------------------------------------------')
print('OBS: Use letras maiúsculas')
print()

#Todo o programa ocorrerá por meio das funções. A função menu_caixa chamará as funões de verificação e calculará os valores a pagar.
menu_caixa()