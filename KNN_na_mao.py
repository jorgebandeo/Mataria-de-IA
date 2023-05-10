import pandas as pd
import csv
# Carregar o conjunto de dados a partir do arquivo CSV
def similaridade(F1,F2):
    a = F1 - F2 if F1 - F2 >=0 else F2 - F1
    return 1-(a/100)
def ditancia(datatrein, novo, pesos):
    vetorD = []
    inf = 0 
    for i in range(len(pesos)): inf = inf + pesos[i]
    for i in range(1,len(datatrein)):
        
        sup = 0
        for j in range(len(datatrein[i])-1):
            sup += pesos[j] * similaridade(int(novo[j]), int(datatrein[i][j]))
        vetorD.append([sup/inf, datatrein[i][-1]])
    vetorD = sorted(vetorD, key=lambda x: x[0])   
    return vetorD
matriz = []
with open('novo csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for linha in reader:
        matriz.append(linha)
novo = ditancia(matriz,[1,1,2,0,1,0,1],[1,1,1,1,1,1,1])
for i  in novo:
    print(i)
