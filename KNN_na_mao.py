import pandas as pd
import csv
#pesos 
pesos = {
    "school":1,
    "sex":1,
    "age":1,
    "address":1,
    "famsize":1,
    "Pstatus":1,
    "Medu":1,
    "Fedu":1,
    "Mjob":1,
    "Fjob":1,
    "reason":1,
    "guardian":1,
    "traveltime":1,
    "studytime":1,
    "failures":1,
    "schoolsup":1,
    "famsup":1,
    "paid":1,
    "activities":1,
    "nursery":1,
    "higher":1,
    "internet":1,
    "romantic":1,
    "famrel":1,
    "freetime":1,
    "goout":1,
    "Dalc":1,
    "Walc":1,
    "health":1,
    "absences":1,
    "G1":1,
    "G2":1,
    "G3":1
}
TS = {#similaridade 1 numerico 2 binario 3 matrizial
    "school":1,
    "sex":1,
    "age":1,
    "address":1,
    "famsize":1,
    "Pstatus":1,
    "Medu":1,
    "Fedu":1,
    "Mjob":1,
    "Fjob":1,
    "reason":1,
    "guardian":1,
    "traveltime":1,
    "studytime":1,
    "failures":1,
    "schoolsup":1,
    "famsup":1,
    "paid":1,
    "activities":1,
    "nursery":1,
    "higher":1,
    "internet":1,
    "romantic":1,
    "famrel":1,
    "freetime":1,
    "goout":1,
    "Dalc":1,
    "Walc":1,
    "health":1,
    "absences":1,
    "G1":1,
    "G2":1,
    "G3":1
}
# Carregar o conjunto de dados a partir do arquivo CSV
vetor_de_matrizes ={'Mjob' : [['Mjob'     ,'at_home'     , 'health'  , 'other'   , 'services', 'teacher'],
                      ['at_home'  ,1     , 0.2   , 0.5  , 0.2 , 0.2],
                      ['health'   ,None  , 1     , 0.5  , 0.4 , 0.6],
                      ['other'    ,None  , None  , 1    , 0,5 , 0,5],
                      ['services' ,None  , None  , None , 1   , 0.7],
                      ['teacher'  ,None  , None  , None , None, 1  ]],
                      'Fjob': [['Fjob'     ,'at_home'     , 'health'  , 'other'   , 'services', 'teacher'],
                      ['at_home'  ,1     , 0.2   , 0.5  , 0.2 , 0.2],
                      ['health'   ,None  , 1     , 0.5  , 0.4 , 0.6],
                      ['other'    ,None  , None  , 1    , 0,5 , 0,5],
                      ['services' ,None  , None  , None , 1   , 0.7],
                      ['teacher'  ,None  , None  , None , None, 1  ]]
                      } #vetor contem as matrizes de semelhança

# similaridade matematica 
def similaridade(F1,F2):
    a = F1 - F2 if F1 - F2 >=0 else F2 - F1
    return 1-(a/100)
# similaridade matrizial
def similaridadeMatrizial(F1,F2, nome ):
    matriz = vetor_de_matrizes[nome]
    coluna = 0
    linha = 0
    for i in range(len(matriz)):
        if  matriz[0][i] == F1:
            coluna = i
    for i in range(len(matriz)):
        if  matriz[i][0] == F2:
            linha = i
    return matriz[linha][coluna]
# similaridade binaria
def similaridadeBinaria(F1,F2):
    if F1 == F2:
        return 1.0
    else:
        return 0.0


def matriz_de_similaridade(Matriz, entrada, P, tipo_de_similaridade):
    Matriz[0].append("similaridade")#adiciona a coluna de similaridade
    inferior = 0
    for i in range(len(P)-1):#soma dos pessoas de cada coluna
        inferior = inferior + P[Matriz[0][i]]
    
    for i in range(1,len(matriz)):#linhas do dataset
        sup = 0
        for j in range(len(matriz[i])-1):#colunas da linha do dataset
            ax = Matriz[0][i]
            if tipo_de_similaridade[ax] == 1:
                sup += P[ax] * similaridade(int(matriz[i][j]), entrada[j])
            elif tipo_de_similaridade[ax] == 2:
                sup += P[ax] * similaridadeBinaria(matriz[i][j], entrada[j])
            else:
                sup += P[ax] * similaridadeMatrizial(matriz[i][j], entrada[j],Matriz[0][j])
        Matriz[i].append(sup/inferior)
    return Matriz
            
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
if __name__ == "__main__":
    Teste = []
    matriz = []
    # Abre e transforma em matriz o dataset de testes 
    with open('Trabalho M2\datasetTestes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for linha in reader:
            Teste.append(linha)
    # Abre e transforma em matriz o dataset de trinamento
    with open('Trabalho M2\student-mat.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for linha in reader:
            matriz.append(linha)
    # Chama função que a aliza similaridade de uma variavel
    novo = matriz_de_similaridade(matriz,Teste[0],pesos, TS)
    # prinata matris com a similaridade de cada elemento com realação o objeto 
    for i  in novo:
        print(i)
