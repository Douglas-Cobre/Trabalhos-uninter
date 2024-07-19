from string import ascii_uppercase #Transforma letras maíusculas em números

#A tabela ascii começa do 65 => A=65
#Quando for converter é preciso fazer uma adaptação
#Não pode usar acentos

letras = list(ascii_uppercase)
msg = input('Digite a msg: ')
msg = msg.upper()
cripto = ''
for l in msg:
    i = ord(l)-65#Vai a correção do número respectivo a letra
    if l in letras:#Verifica se é uma letra
        cripto += letras[(i+3)%26]#Vai trocar pela proxima terceira letra
print(cripto)