#Listas e tuplas são semelhantes a vetores
#Tuplas
mochila = ('caderno' , 'lápis' , 'borracha')
print(mochila[0]) # tuplas tem as mesmas carcterísticas de vetores, porém são IMUTÁVEIS

#Listas
mochila = ['caderno' , 'lápis' , 'borracha'] 
print(mochila[1])#Semelhante a tuplas, porém são MUTÁVEIS
mochila.insert(3 , 'livro') # inseri um novo elemento
mochila.append('caneta') #inseri no final
print(mochila)  
#Listas podem mostrar/destacar elementos dentro de elementos
mochila = ['machado ' , 'camisa ']
for item in mochila:
    for letra in item:
        print(letra)
#Podem existir listas dentro de listas
preços = [['coxinha' , 8.00] , ['suco' , 5.00] , ['bolo' , 4.00]]
print(preços[0][0])#index duplo para mostrar a palavra, o mesmo método pode ser usado para separar uma letra
