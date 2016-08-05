# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:29:15 2016

Codigo para identificacao via grafico
de ciclos para o modelo de crescimento 
logistico onde f = rx(1-x)

O objetivo aqui e evoluir o modelo no tempo
de maneira que seja possivel detectar a existencia
de um ciclo. Para isso utiliza-se um numero elevado 
de iteracoes, inspecionam-se os 'n' ultimos elementos 
buscando uma repeticao periodica. Se isso acontece, temos
um ciclo.

@author: Guilherme Felix e Diego Micarello
"""

import numpy as np
import matplotlib.pyplot as plt
import collections as col
#localfile = '/home/guilherme/Documentos/Intro Modelagem Computacional/'

#============================================================
#               Crescimento Logístico

#funcao f(x) = xn+1
def f(x,r):
    return r*x*(1-x)

#============================================================
# Definicao de Parametros
tam = 1e3    #numero de iterações da evolucao temporal
ult = 100    #tamanho da do subconjunto das ultimas posicoes que sera inspeciondo
tempo = range(int(tam)) 
PopulacaoInicial = 0.1 
Populacao = np.zeros(tam)
Populacao[0] = PopulacaoInicial

#Valores para o parametro r. 
passoR = 0.005
r = np.arange(0,3.4,passoR)

plt.figure(1)
plt.title('Grafico Bifurcacao') 

#Evolucao temporal do modelo para (0 <= r <= 3.4)
for j in range(len(r)):
    for i in tempo[1:]:
        Populacao[i] = f(Populacao[i-1],r[j])
    y = col.Counter(Populacao[-ult:]).most_common() # Essa funcao conta as ocorrencias em um vetor e rankeia por frequencia

    print 50*'A', '\n', 'Valor de r com ciclo: ', r[j]
    print 'Tamanho do y:', len(y)
    print 'Valores em y: ', y, '\n'
    X_estrela = [elem[0] for elem in y]
    plt.plot([r[j]]*len(X_estrela),X_estrela,'b.')


# Redefinicao de Parametros
tam = 1e5   
ult = 200    
tempo = range(int(tam)) 
PopulacaoInicial = 0.1 
Populacao = np.zeros(tam)
Populacao[0] = PopulacaoInicial

amostra = 1000
r = np.linspace(3.4,4,amostra)

Ciclos = []
#Evolucao temporal do modelo para (3.4 < r <= 4)
for j in range(len(r)):
    for i in tempo[1:]:
        Populacao[i] = f(Populacao[i-1],r[j])
    y = col.Counter(Populacao[-ult:]).most_common()

    if (len(y)>ult/2):
        print 50*'=', '\n', 'Para r = ', r[j], 'não há ciclo.'
        print 'Tamanho do y para r = ', r[j]
        print len(y)

    else:
        print 50*'A', '\n', 'Valor de r com ciclo: ', r[j]
        print 'Tamanho do y:', len(y)
        print 'Valores em y: ', y, '\n'
        Ciclos.append([r[j],y])        
        X_estrela = [elem[0] for elem in y]
        plt.plot([r[j]]*len(X_estrela),X_estrela,'b.')

plt.legend([str(int(tam))+' iteracoes'],loc='upper left')
#plt.legend(loc='best')
plt.ylim(ymin=0)
plt.xlabel('r')
plt.ylabel('x*')
plt.grid()
#plt.savefig(localfile+'Grafico_Bifurcacao_Ciclo(2).png',dpi=200)
plt.show()

