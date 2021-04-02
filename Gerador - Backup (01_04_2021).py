'''
Autor: João Víctor Costa de Oliveira
'''

'''
Programa alterado no dia 01/04/2021 por João Víctor Costa de Oliveira
Problemas encontrados e ratificados: 37
Problemas encontrados e não ratificados: 0
'''

import random
import string
import os

#função intermediária que cria uma nova variável
def gerar_senha_intermediario(senha):
    senha_antiga = senha
    return senha_antiga

#função que compara a senha gerada no ciclo anterior e a gerada no ciclo atual do programa 
def gerar_senha_comparacao(senha, senha_antiga):
    if(senha == senha_antiga):
        return True #se as duas senhas forem iguais, a função retornará um código de verdadeiro, atestando que são realmente iguais
    else:
        return False #se as duas senhas forem iguais, a função retornará um código de falso, atestando que não são iguais

#Função que irá gerar e imprimir a senha:
def gerar_senha(senha):
    numero = int(input ("Quantos caractéries você quer na sua senha?  ")) #checa quantos caractéries o usuário deseja na senha
    osta = input("Você quer letras, numeros ou ambos em sua senha?  ") #checa que tipos de caractéries que o usuário desenha na senha
    if (osta == 'ambos'):
        er = input("Na sua senha poderá estar contida letras maiusculas, minusculas ou ambas?  ")
    if(osta == 'letras'):
        answ = input("Deseja letras maiusculas, minusculas ou ambas?   ")
    print("Sua senha é:")   #um simples print para organizar o programa
    senha_antiga = gerar_senha_intermediario(senha) #chamada da função
    for i in range(numero): #faz com que um caractérie seja impresso enquanto o número de caractéries não tiver sido acatado
        if(osta == 'numeros'):
            senha = (random.SystemRandom().choice(string.digits))
        elif(osta == 'letras' and answ == 'ambas'):
            senha = (random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase))
        elif(osta == 'letras' and answ == 'maiusculas'):
            senha = (random.SystemRandom().choice(string.ascii_uppercase))
        elif(osta == 'letras' and answ == 'minusculas'):
            senha = (random.SystemRandom().choice(string.ascii_lowercase))
        elif(osta == 'ambos' and er == 'ambas'):
            senha = (random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase))
        elif(osta == 'ambos' and er == 'maiusculas'):
            senha = (random.SystemRandom().choice(string.ascii_uppercase + string.digits))
        elif(osta == 'ambos' and er == 'minusculas'):
            senha = (random.SystemRandom().choice(string.digits + string.ascii_lowercase))
        intermed = gerar_senha_comparacao(senha, senha_antiga) #chamada da função com uma variável recebendo o retorno
        if(intermed == False):           #termina a checagem das senhas
            print(senha, end = "")
            
            arquivo.write(senha)
        elif(intermed == True):        #termina a checagem das senhas
            return intermed

#Chamada da função dentro do programa principal:
arquivo = open("senhasGeradas.txt", "a+")
resposta = 'sim' #inicializei com sim para poder entrar no loop
senha = 0   #inicializei com zero para ter o que guardar na função gerar_senha_intermediario
while (resposta == 'sim'): #loop
    arquivo.write("\n")
    iaria = gerar_senha(senha) #chamada da função, com uma variável para receber um possível retorno
    print("") #salta uma linha
    if(iaria == True):
        #Se a função gerar_senha retornar a variável intermed como falsa, o programa imprimirá o código de erro:
        print("PROBLEM 001"); print("TENTE GERAR A SENHA NOVAMENTE, POIS ESSA SE IGUALA A GERADA ANTERIORMENTE PELO PROGRAMA")
        print("");print("") #salta uma linha
    resposta = input("Gostaria de gerar outra senha (sim/nao)? ") #pergunta se o usuário deseja digitar outra senha  
    if(resposta == 'sim'):
        os.system('clear') or None #limpa o console depois que o programa termina de executar
print("") #salta uma linha
