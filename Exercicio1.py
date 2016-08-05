# -*- coding: utf-8 -*-
"""
Created on Fri May  6 04:00:35 2016
Exercício 1 - Introducao a Modelagem Computacional
UFJF

Objetiva plotar o valor do saldo de uma aplicação de renda fixa
ao longo do tempo.
@author: Guilherme Almeida Felix da Silva - 201365504AB
"""

import numpy as np
import matplotlib.pyplot as plt

#Pasta destino onde a imagem sera salva.
#localfile = '/home/guilherme/Documentos/Intro Modelagem Computacional/'


#tamanho do vetor
tam = 120
saldo_inicial = 1000
meses = range(tam)
taxa = 0.01

#==============================================================
#   EXEMPLO 1: a' = 1.01*a
saldo = []
saldo.append(saldo_inicial)

for i in meses[1:]:
    saldo.append((1+taxa)*saldo[i-1])

#==============================================================
#Plotagem

plt.figure(1)
plt.plot(meses[::6], saldo[::6], 'bo', label = 'Saldo')
plt.title('Saldo em conta ao fim de 120 meses')
plt.legend()
plt.ylim(ymin=0)
plt.xlabel('Meses')
plt.ylabel('Reais')
plt.grid()
#plt.savefig(localfile+'Exemplo_1.png',dpi=200)

#==============================================================
#   EXEMPLO 2: Com retirada fixa de R$50: a' = 1.01*a - 50
tam = 120
saldo_inicial = 1000
meses = range(tam)
taxa = 0.01

saldo = []
saldo.append(saldo_inicial)

for i in meses[1:]:
    saldo.append((1+taxa)*saldo[i-1] - 50)

#==============================================================
#Plotagem

plt.figure(2)
plt.plot(meses[:24], saldo[:24], 'g^', label = 'Saldo')
plt.title('Saldo em conta ao fim de 24 meses')
plt.legend()
plt.ylim(ymin=0,ymax=1000)
plt.xlabel('Meses')
plt.ylabel('Reais')
plt.grid()
#plt.savefig(localfile+'Exemplo_2.png',dpi=200)
plt.show()

#==============================================================
#   EXEMPLO 2 Crescimento Populacional. Dados

tam = 8
tempo = range(tam)
Biomassa = [9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3] # Parametros já defidos do exemplo em questao
Var_BioMass = []
for i in range(tam-1):
    Var_BioMass.append(Biomassa[i+1] - Biomassa[i])


#==============================================================
#Plotagem

plt.figure(3)
plt.plot(Biomassa[:-1], Var_BioMass, 'ro')
plt.title('Crescimento Populacional 1: Biomassa')
plt.legend()
plt.ylim(ymin=0,ymax= max(Var_BioMass))
plt.xlabel('Biomassa')
plt.ylabel('$\Delta$ Biomassa')
plt.grid()
#plt.savefig(localfile+'Exemplo_3.png',dpi=200)
plt.show()

#============================================================
#               MODELO p' = (1+k)p

#Lista de valores do parametro k
k = np.arange(0.45, 0.75, 0.05)

#lista de simbolos para ser usado no grafico
simbolos = ['bo','rs','y*','g+','cx','m>']
Modelo_BioM = [Biomassa[0],0,0,0,0,0,0,0]

#==============================================================
#Plotagem

plt.figure(4)
plt.title('Crescimento Populacional 2: Comparacao dos Modelos')
plt.plot(tempo, Biomassa, 'k^', label = 'Dados Experimentais')

for i in range(len(k)):
    for j in tempo[1:]:
        Modelo_BioM[j] = (1 + k[i])*Modelo_BioM[j-1]

    plt.plot(tempo, Modelo_BioM, simbolos[i],label = 'Modelo k = '+str(k[i]))
    plt.legend(loc ='upper left')

plt.ylim(ymin=0,ymax= max(Biomassa))
plt.xlabel('Tempo')
plt.ylabel('Biomassa')
plt.grid()
plt.savefig(localfile+'Exemplo_4.png',dpi=200)
plt.show()

#============================================================
#               Crescimento Populacional controlado

tam = 19
tempo = range(tam)

# Parametros já defidos do exemplo em questao
Biomassa = [9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 257.3, 350.7, 441.0, 513.3, 559.7, 594.8, 629.4, 640.8, 651.1, 655.9, 659.6, 661.8]

k = np.arange(0.00082, 0.00090, 0.00002)

p_lim = 663
#lista de simbolos para ser usado no grafico
simbolos = ['bo','rs','y*','g+','cx','m>']
Modelo_BioM = np.zeros(tam)
Modelo_BioM[0] = Biomassa[0]

plt.figure(5)
plt.title('Crescimento Populacional 2: Comparacao dos Modelos')
plt.plot(tempo, Biomassa, 'k^', label = 'Dados Experimentais')

for i in range(len(k)):
    for j in tempo[1:]:
        Modelo_BioM[j] = k[i]*Modelo_BioM[j-1]*(p_lim - Modelo_BioM[j-1]) + Modelo_BioM[j-1]

    plt.plot(tempo, Modelo_BioM, simbolos[i],label = 'Modelo k = '+str(k[i]))
    plt.legend(loc ='upper left')

plt.ylim(ymin=0,ymax= max(Biomassa))
plt.xlabel('Tempo')
plt.ylabel('Biomassa')
plt.grid()
#plt.savefig(localfile+'Exemplo_5.png',dpi=200)
plt.show()

#============================================================
#               Crescimento Logístico
tam = 100000
tempo = range(tam)
PopulacaoInicial = 0.1
Populacao = np.zeros(tam)
Populacao[0] = PopulacaoInicial

simbolos = ['-o','r-s','y-*','g-o','c-s','m->','p-']

r = [0.85,1.546,2.75,3.25,3.525,3.555,3.75]

for j in range(6):
    for i in tempo[1:]:
        Populacao[i] = (r[j]*(1-Populacao[i-1])*Populacao[i-1])
    
    plt.figure(6+j)
    plt.title('Crescimento Logistico '+str(j))    
    plt.plot(tempo[-100:], Populacao[-100:], simbolos[j] ,label = 'r = '+str(r[j]))
    plt.legend(loc='best')
    plt.ylim(ymin=0)
    plt.xlabel('Tempo')
    plt.ylabel('Populacao')
    plt.grid()
    #plt.savefig(localfile+'Exemplo_6_'+str(j)+'.png',dpi=200)
    plt.show()
    
#============================================================
#               Crescimento Logístico e Cobwebbing

#funcao f(x) = xn+1
def f(x,r):
    return r*x*(1-x)

tam = 100
X = np.linspace(0,1,tam)

Vet = np.zeros(tam)
x0 = 0.8
Vet[0] = x0
Cob = np.zeros((2*tam-1,2))

r = [1.546,2.75,3.25,3.525,3.555,3.75]
simbolos = ['r-','y-','k-','g-','c-','m-','p-']

for j in range(len(r)):
    Xn = np.zeros(tam)
    Xn = f(X,r[j])
    plt.figure(j+7)
    plt.title('Cobwebbing')
    plt.plot(X, X,'g-')
    plt.plot(X, Xn,'-')

    Cob[0,0], Cob[0,1] = x0, 0.0
    for i in range(tam-1):
        Vet[i+1] = f(Vet[i],r[j])
        Cob[2*i+1,0], Cob[2*i+1,1] = Vet[i], Vet[i+1]
        Cob[2*i+2,0], Cob[2*i+2,1]= Vet[i+1], Vet[i+1]
    plt.plot(Cob[:,0], Cob[:,1],simbolos[j], label='r = '+str(r[j]))

    plt.legend(loc='best')    
    #plt.ylim(ymax=1)
    plt.xlabel('Xn')
    plt.ylabel('Xn+1')
    plt.grid()
    #plt.savefig(localfile+'Cobwebbing_'+str(j+1)+'.jpg',dpi=200)
    plt.show()
