#Cadastro com armazenamento de dados (Manipulação de dados)
def valida_int(perginta , min , max):
    x = int(input('Escolha uma opção: '))
    while (x >= min and x < max):
        x = int(input('Escolha uma opção: '))
        return x

def existeArquivo(nomeArquivo): #Verifica se o arquivo existe
    try:
        a = open(nomeArquivo , 'rt')    
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo): #Cria um arquivo
    try:
        a = open(nomeArquivo , 'wt+')
    except:
        print('Algo inesperado aconteceu')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso')
        
def cadatrarJogo(nomeArquivo , jogo , plataforma): #Cadastrar
    try:
        a = open(nomeArquivo , 'at')
    except:
        print('Erro ao cadastrar jogo')
    else:
        a.write(f'{jogo} ; {plataforma}\n')
    finally:
        a.close
        
def listar(nomeArquivo): #Ver listar/arquivo
    try:
        a = open(nomeArquivo , 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()
    
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado')
else:
    print('Arquivo não encontrado')
    criarArquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastrados')
    print('3 - Sair')    
    op = valida_int('Escolha uma opção: ' , 1 , 4)
    
    if (op == 1):#Novo item
        print('Cadatro carregando...')
        novoJogo = input('Nome do jogo: ')
        plataformaJogo = input('Plataforma: ')
        cadatrarJogo(arquivo , novoJogo , plataformaJogo)
    elif (op == 2):#Listar
        print('Lista carregando...')
        listar(arquivo)
    elif (op == 3):#Sair
        print('Encerrando...')
        break
        
