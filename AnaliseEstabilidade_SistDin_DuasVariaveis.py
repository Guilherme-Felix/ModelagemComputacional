# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:32:41 2016
Modelo dinâmico descrito por um sistema de equacoes
lineares com duas variáveis.
@author: Guilherme
"""
import numpy as np
import matplotlib.pyplot as plt

#localfile = '/home/guilherme/Documentos/Intro Modelagem Computacional/SisDuasVariaveis/'
localfile = '/home/guilherme/Dropbox/UFJF/MAC024 - Intro Modelagem Computacional/Codigos e Trabalhos/Figuras/AnaliseEstabilidade_DuasVariaveis/Resultados2'

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
limite = 1
amostra = 15

aR = np.random.uniform(-limite,limite,amostra)
pR = np.random.uniform(-limite,limite,amostra)
aJ = np.random.uniform(-limite,limite,amostra)
pJ = np.random.uniform(-limite,limite,amostra)

#aR =  [0.31980577436195334, -0.1805950319501628, 0.22967985893424836, 0.040699768170543438, 0.80603860261516158]
#pR =  [0.089718203959241904, -0.50221939976521046, 0.22094328237039362, -0.9846549643320992, -0.92770000838862243]
#aJ =  [0.25358592284432224, -0.97773709509319429, -0.2341137696875204, -0.67742884734070441, 0.66469010522441785]
#pJ =  [-0.90456870482701923, 0.94638949187114574, -0.50903138845354579, 0.29946126012333152, 0.20117193467785266]




for k in range(amostra):
    I = np.identity(2)                #Matriz Identidade
    J = [[aR[k],pR[k]],[pJ[k],aJ[k]]] #Matriz Jacobiana
    A = J - I
    
    detJ = np.linalg.det(J)
    trJ = np.trace(J)
    detA = np.linalg.det(A)
    
    #Vetor para o Romeu
    Romeu = np.zeros(tam)
    Romeu[0] = valor_inicial
    
    #Vetor para o Julieta
    Julieta = np.zeros(tam)
    Julieta[0] = valor_inicial
    
    #Para desenhar as linhas do gráfico
    #retas detJ = +-trJ-1
    X = [-2,0,2]
    Y = [1,-1,1]
    
    #reta det(J) = 1
    X1 = [-2,2]
    Y1 = [1,1]
    
    #parabola det(J) = tr(J)²/4
    X2 = np.linspace(-2,2)
    Y2 = (X2**2)/4
    
    # Evolucao temporal Romeu e o Vetor Julieta
    for i in tempo[1:]:
        Romeu[i] = f(aR[k],Romeu[i-1],pR[k],Julieta[i-1])
        Julieta[i] = g(aJ[k],Romeu[i-1],pJ[k],Julieta[i-1])
#==============================================================================    
    #Figura 1 tr(J) x det(J)
    plt.figure(1+k)   
    plt.title('Grafico det(J) x tr(J) '+str(1+k)) 
    plt.xlabel('tr(J)')
    plt.ylabel('det(J)')
    plt.grid()

    #Plot    
    plt.scatter(trJ,detJ,c='red',label = '('+str(round(trJ,2))+', '+str(round(detJ,2))+')')
    plt.plot(X,Y,'bo-',linewidth=1.0)
    plt.plot(X1,Y1,'bo-',linewidth=1.0)
    plt.plot(X2,Y2,'--',linewidth=0.5)

    #Texto dentro do gráfico
    texto = '$a_R: '+ str(round(aR[k],2)) + '$\n$a_J:' + str(round(aJ[k],2)) + '$\n$p_R: ' + str(round(pR[k],2)) + '$\n$p_J: ' + str(round(pJ[k],2)) + '$'
    Box={'facecolor':'grey', 'alpha':0.2, 'pad':4} 
    plt.text(-2.95, -1.4, texto, fontsize=14, bbox=Box, family='serif')
    
    #Legenda
    plt.legend(loc='best')
    
    plt.savefig(localfile+'det_Versus_tr'+str(1+k)+'.png',dpi=200)    
    plt.show()
#==============================================================================    
    #Figura 2 Evolucao Temporal
    plt.figure(2+k)
    plt.suptitle('Evolucao Temporal'+str(1+k), x=0.5,y=0.985)
    
    texto = '$a_R: '+ str(round(aR[k],2)) + '$, $a_J:' + str(round(aJ[k],2)) + '$, $p_R: ' + str(round(pR[k],2)) + '$, $p_J: ' + str(round(pJ[k],2)) + '$'
    plt.title(texto)
    #Plot    
    plt.plot(tempo,Romeu,'bo-',label='Romeu')
    plt.plot(tempo,Julieta,'go-',label='Julieta')
    
    #Legenda
    plt.legend(loc='best')
    plt.xlabel('Tempo')
    plt.ylabel('Intensidade')
    plt.grid()
    
    plt.savefig(localfile+'EvolucaoTemporal'+str(1+k)+'.png',dpi=200)
    plt.show()

#==============================================================================    
    #Figura 3 Plano Fase
    plt.figure(3+k)
    plt.suptitle('Plano Fase'+str(1+k), x=0.5,y=0.985)
    
    texto = '$a_R: '+ str(round(aR[k],2)) + '$, $a_J:' + str(round(aJ[k],2)) + '$, $p_R: ' + str(round(pR[k],2)) + '$, $p_J: ' + str(round(pJ[k],2)) + '$'
    plt.title(texto)
    #Plot
    plt.plot(Romeu,Julieta,'co-') 
    #Legenda
    plt.xlabel('Romeu')
    plt.ylabel('Julieta')
    plt.grid()

    plt.savefig(localfile+'PlanoFase'+str(1+k)+'.png',dpi=200)
    plt.show()
    
print 'FIM'    
