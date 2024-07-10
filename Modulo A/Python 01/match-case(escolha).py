#Match - case é uma versão do Python para o Switch ou Escolha

#O Match pode substituir uma série de IF e ELIF

#Exemplo de Match - Case (Compra de produto)
print('Escolha o código do produto')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha ? '))
qtd = int(input('Quantas unidades ? '))

match(produto):
    case 1:#O mesmo que (produto == 1)
        pagar = qtd*2.3
        print(f'Você comprou {qtd} maça(s). Total a pagar {pagar:.2f}')
    case 2:#O mesmo que (produto == 2)
        pagar = qtd*3.6
        print(f'Você comprou {qtd} laranja(s). Total a pagar {pagar:.2f}')
    case 3:#O mesmo que (produto == 3)
        pagar = qtd*1.85
        print(f'Você comprou {qtd} Banana(s). Total a pagar {pagar:.2f}')
    case _:#O memso que ELSE
        print('Produto inexistente')