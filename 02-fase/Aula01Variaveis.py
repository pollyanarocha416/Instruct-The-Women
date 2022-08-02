listas = [4, 5, 6, 1, 5]
print(listas)
listas.append(2)#adicionar
listas.sort()#organizar
print(listas)
len(listas)#contar
print(len(listas))
del listas[0]# excluir
print(listas)

for i in listas:
    if i >= 6:
        print("Aprovado")
    else:
        print("Reprovado")



tuplas = (5, 6, 1, 0)
#print(tuplas)
conjuto= {1, 3, 4, 5, 2}
#print(conjuto)


#fatiamento
disc= 'ficica'
disc = disc[:5]
disc= disc.replace('f', '0', 1)# so a primeira ocorrencia
disc = disc.split('i')# separa eles por virgula
disca = ('aluna')
disca = '-'.join(disca)
print(disca)
# condicional ternaria
id = 19
resul = "Aprovado" if id >=19 else "Reprovado"
print(resul)


#find busca qual posicao o caractere q vc q estar
