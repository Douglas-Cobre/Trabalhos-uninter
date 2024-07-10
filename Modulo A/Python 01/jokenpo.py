import random #Gera números aleatórios

#Verifica se é um número válido
def valida(pergunta , min , max):
    x = int(input(pergunta))
    while (x < min and x > max):
        x = int(input(pergunta))
    return x

#Verifica o vencedor
def vencedor(p1 , p2):
    global v1 , v2 , empate
    if(p1 == 1):#pedra
        if(p2 == 1):
            empate += 1
        elif(p2 == 2):
            v2 += 1
        elif(v2 == 3):
            v1 += 1
    elif(p1 == 2):#papel
        if(p2 == 1):
            v1 += 1
        elif(p2 == 2):
            empate += 1
        elif(p2 == 3):
            v2 += 1
    elif(p1 == 3):#tesoura
        if (p2 == 1):
            v2 += 1
        elif(p2 == 2):
            v1 += 1
        elif(p2 == 3):
            empate += 1
    resulatados = [v1 , v2 , empate]
    return resulatados
            
#MENU
print('+---------+')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
print( '0 - SAIR')

jogadas = []
resultados = []
v1 = 0
v2 = 0
empate = 0
while True:
    j1 = valida('Escolha sua jogada: ', 0 , 3)
    if not j1:
        break
    j2 = random.randint(1,3)
    jogadas.append([j1 , j2])
    resultados = vencedor(j1 , j2)#Chama a função

for jogada in jogadas:
    for dado in jogada:
        print(dado , end = ' ')#END serve para colocar lado a lado
    print()#Quebra de linha
        
print(f'Vitórias do jogador 1: {resultados[0]}')
print(f'Vitórias do jogador 2: {resultados[1]}')
print(f'Empates: {resultados[2]}')
    
    