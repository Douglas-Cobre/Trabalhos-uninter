
#Questão 04: Cadastros
#Funções

def cadastrar_livro(id):#Exigência de código 3
    global id_global , indice , lista_livro , livro #As variáveis globais serão usadas ao longo do código
    while True:#Exige uma resposta do usuário
        livro['ID'] = id
        livro['Nome'] = input('Nome do livro: ')
        livro['Autor'] = input('Nome do autor: ')
        livro['Editora'] = input('Nome da editora: ')
        lista_livro.append(livro.copy())#Exigência de código 7
        break
    
def consultar_livro():#Exigência de código 4
    global id_global , lista_livro , livro
    while True:#Até que o usuário dê uma resposta válida, o preograma repetirá a pergunta
        try:
            print('1 - Consultar todos os livros')
            print('2 - Consultar livro por ID')
            print('3 - Consultar livro por autor')
            print('4 - Retornar')
            op = int(input('>>'))
            if(op == 1):#Consultar todos
                for livro in lista_livro:
                    print('+----------+')
                    for keys , values in livro.items():
                        print(f'{keys}: {values}')
                    print('+----------+')
            elif(op == 2):#Consultar por ID
                id_consulta = int(input('Digite o ID: '))
                for livro in lista_livro:
                    for values in livro.values():
                        if (id_consulta == values):#Caso o ID não exista, nada acontecerá
                            print('+----------+')
                            for chaves , valor in livro.items():
                                print(f'{chaves}: {valor}')
                            print('+----------+')     
            elif(op == 3):#Consultar por autor
                autor = input('Digite o nome autor: ')
                for livro in lista_livro:
                    for values in livro.values():
                        if (autor == values):#Caso o AUTOR não exista nada acontecerá
                            print('+----------+')
                            for keys , values in livro.items():
                                print(f'{keys}: {values}')
                            print('+----------+')
            elif(op == 4):#Retornar
                break
            else:
                print('+-----------------------------+')
                print('Opção inválida, tente novamente')
                print('+-----------------------------+')
        except ValueError:
            print('+-----------------------------+')
            print('Opção inválida, tente novamente')
            print('+-----------------------------+')
            
def remover_livro():#Exigência de código 5
    delete = int(input('Digite o ID do livro a ser removido: '))#Caso não tenha um livro com o ID informado, nada acontecerá
    delete -= 1 #O ID do livro é diferente do indice da lista, ao reduzir em 1 os valores ficam iguais
    del lista_livro[delete]
    print('+-------------------------+')
    print('Livro removido com sucesso!')
    print('+-------------------------+')


#Programa principal
#Variáveis
lista_livro = []#Lista
id_global = 1
livro = {}#Dicionário
print('+---------------------------------------+')
print('| Bem vindo a livraria do Douglas Cobre |')#Exigência de código 1
while True:#Exigência de código 6
    try:#Até que seja encerrado essa mensagem irá aparecer
        print('+---------------------------------------+')
        print('+------------MENU PRINCIPAL-------------+')
        print('Escolha a operação desejada')
        print('1 - Cadastrar livro')
        print('2 - Consultar livro')
        print('3 - Remover livro')
        print('4 - Encerrara programa')
        escolha = int(input('>>')) 
        #Chama a função correspondente a opção
        if(escolha == 1):
            cadastrar_livro(id_global)#Exigência de código 2
            id_global += 1
        elif(escolha == 2):
            consultar_livro()
        elif(escolha == 3):
            remover_livro()
        elif(escolha == 4):
            print('+--------------------+')
            print('Encerrando programa...')
            print('+--------------------+')
            break
        else:#Caso algum erro não previsto ocorra, uma mensagem de alerta irá aparecer
            print('+-----------------------------+')
            print('Opção inválida, tente novamente') 
            print('+-----------------------------+')
    except:#Caso algum erro não previsto ocorra, uma mensagem de alerta irá aparecer
        print('+-----------------------------+')
        print('Opção inválida, tente novamente')
        print('+-----------------------------+')



