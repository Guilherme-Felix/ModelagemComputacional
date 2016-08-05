# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:32:41 2016

Modelo dinâmico descrito por um sistema de equacoes
lineares com duas variáveis. Neste exemplo anedotico, 
as grandezas envolvidas são o sentimento de amor e odio
entre Romeu e Julieta

Esse codigo produz o Plano Fase e a Evolucao Temporal 
das variaveis

@author: Guilherme Felix - guilherme.felix@engenharia.ufjf.br
"""
import numpy as np
import matplotlib.pyplot as plt

#localfile = '/home/guilherme/Documentos/Intro Modelagem Computacional/'

#============================================================
#               Romeu e Julieta
#funcao f(r,j) = aR*r + pR*j que descreve o comportamento do Romeu
def f(aR,r,pR,j):
    return aR*r + pR*j

#funcao g(r,j) = aJ*r + pJ*j que descreve o comportamento da Julieta
def g(aJ,r,pJ,j):
    return aJ*j + pJ*r

#============================================================
# Definicao de Parametros
tam = 60    #numero de iterações da evolucao temporal
tempo = range(tam) 
valor_inicial = 1

#Conjunto de Parâmetros das funções f(r,j) e g(r,j)
aR = [0.5, 0.5, 1.0, 0.5]
pR = [0.2, 0.7, 0.2, 0.2]

aJ = [0.7, 0.7, 1.0, 0.8]
pJ = [0.5, 0.9, -0.2, 0.5]

#Vetor para o Romeu
Romeu = np.zeros(tam)
Romeu[0] = valor_inicial

#Vetor para o Julieta
Julieta = np.zeros(tam)
Julieta[0] = valor_inicial

#Preenche o Vetor Romeu e o Vetor Julieta
for k in range(len(aR)):
    for i in tempo[1:]:
        Romeu[i] = f(aR[k], Romeu[i-1], pR[k], Julieta[i-1])
        Julieta[i] = g(aJ[k], Romeu[i-1], pJ[k], Julieta[i-1])
    
	#Plot
    plt.figure(1+k)

    plt.title('Caso '+ str(1+k) + ': $a_R$ = ' + str(aR[k]) + ', $a_J$ = ' + str(aJ[k])
    + ', $p_R$ = ' + str(pR[k]) + ', $p_J$ = ' + str(pJ[k])) 

    plt.plot(tempo,Romeu,'bo-',label='Romeu')
    plt.plot(tempo,Julieta,'go-',label='Julieta')
    
    plt.legend(loc='best')
    plt.xlabel('Tempo')
    plt.ylabel('Intensidade')
    plt.grid()
    #plt.savefig(localfile+'SistemaDuasVariaveis_Caso'+str(1+k)+'.png',dpi=200)
    plt.show()
    
    plt.figure(2+k)
    plt.title('Plano fase Caso ' + str(1+k))
    plt.plot(Romeu,Julieta,'ro-') 
    
    plt.xlabel('Romeu')
    plt.ylabel('Julieta')
    plt.grid()
    #plt.savefig(localfile+'PlanoFase_Caso'+str(1+k)+'.png',dpi=200)
    plt.show()


