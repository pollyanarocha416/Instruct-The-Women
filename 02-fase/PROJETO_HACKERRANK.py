#Arredondar pra o proximo numero

import math

#Arredondar pra sima
#m = 0.34
#a = math.ceil(m)
#print(a)

# funcao:

# 4.17 * qtd de letras/ qtd de palavras + 0.5 * qtd de palavras/ qtd de frase 1 - 21.43
# depois disso arredonda para o proximo nmero O maximo e 14
#4.71 * 38 / 11 ~ = 16.27

#0.5 * 11 = 5.5

#16.27 + 5.5 - 21.43 = 0.34


def automated_readability_index(sentence):
    palavras = len(sentence.split())
    #print(palavras)
    sentence = sentence.replace(" ", "")
    letras = len(sentence)
    #print(letras)
    calculo = 4.71 * float(letras) / float(palavras) + 0.5 * float(palavras) - 21.43
    #a= 4.17
    #b = 0.5
    #c = -21.43
    #calculo = a * letras / palavras + b * palavras - c
    valor = math.ceil(calculo)
    if valor >= 14:
        return 14
    else:
        return valor
    

resul = automated_readability_index(
    "The latter consisted simply of six hydrocoptic marzelvanes so fitted to the ambifacient lunar waneshaft that side fumbling was effectively prevented")

print(resul)
