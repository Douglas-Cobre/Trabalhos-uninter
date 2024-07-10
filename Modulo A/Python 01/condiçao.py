#Cole os exemplos na página de teste.py para ver o resultado

nome = (input('Digite seu nome: '))
if (nome == 'Douglas'):
    print('Usuário correto')
else:
    idade = int(input('Digite sua idade: '))
    if (idade >= 18 and idade < 100):
        print('Usuário de maior')
    elif(idade >= 100):
        print('Usuário não permitido')
    else:
        print('Usuário de menor')