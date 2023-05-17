import csv
import os
import numpy as np
import pandas as pd
def notaAmericana(numero):
    if numero >= 16:
        return 'A'
    elif numero>= 14:
        return 'B'
    elif numero >= 12:
        return 'C'
    elif numero >= 10:
        return 'D'
    else: 
        return 'F'
def maior(df, nome_coluna):
    
    maior_valor = df[nome_coluna].max()
    return maior_valor
def menor(df, nome_coluna):
    
    menor_valor = df[nome_coluna].min()
    return menor_valor
pesos = {
    "G2": 0.2537,
    "G1": 0.2224,
    "failures": 0.1395,
    "absences": 0.1178,
    "higher": 0.0822,
    "school": 0.0771,
    "schoolsup": 0.0575,
    "goout": 0.0539,
    "traveltime": 0.0489,
    "famrel": 0.0475,
    "sex": 0.0475
}
TS = {
    "school": 2,
    "sex": 2,
    "failures": 3,
    "absences": 1,
    "higher": 2,
    "schoolsup": 2,
    "goout": 3,
    "traveltime": 3,
    "famrel": 3,
    "G1": 3,
    "G2": 3
}
def SimilaridadeNumerica(F1,F2, max, min):
    # 1 - | F1 - F2 | / (max - min)
    a = F1 - F2 if F1 > F2  else F2 - F1 #| F1 - F2 |
    return 1-a/(max - min)

def SimilaridadeBooleana (F1,F2):
    a = 1 if F1 == F2 else 0
    return 1-(a)

def SimilaridadeLolica(F1, F2, valores):
    elementos= {}
    distribuicao = 0
    # distribui percentualmente os elemento no dicionario
    for i in range(len(valores)):
        distribuicao += 1/len(valores)
        elementos[valores[i]] = distribuicao
    # igaul ao numerico so que usa o auxilio do dicionarios
    
    F1 = elementos[F1]
    F2 = elementos[F2]
    a = F1 - F2 if F1 > F2  else F2 - F1

    return 1-a/(1)

def CalculadorDeSimilaridade(Arquivo,predict):
    colunas = Arquivo.columns.to_list()
    semelhanca = []
    pessom = 0
    for i in colunas:
        pessom += pesos[i]
    for i in range(0,len(Arquivo.values)):
        somas = 0
        for j in colunas:
            if 1 == TS[j]:
                somas += pesos[j]*SimilaridadeNumerica(Arquivo[j][i], predict[j], maior(Arquivo,j), menor(Arquivo,j))
            elif 2 == TS[j]:
                somas += pesos[j]*SimilaridadeBooleana(Arquivo[j][i], predict[j])
            else :
                somas += pesos[j]*SimilaridadeLolica(Arquivo[j][i], predict[j],Arquivo[j].unique())
        semelhanca.append(somas/pessom)

    return semelhanca 
def men2(suges, arc):
    colunas = arc.columns.to_list()
    while True:
        os.system('cls')
        print(suges)
        print("digite o elemento que quer mudar")
        op = input("qual opção: ")
        for i in colunas:
            if op == i:
                while True:
                    os.system('cls')
                    print(suges)
                    print("os valores posiveis são: ", arc[i].unique())
                    pe1 = input("valor: ")
                    for j in arc[i].unique():
                        if pe1 == j:
                            suges[i] = pe1
                            return suges
                    
                    

def menu1(sug):
        os.system('cls')
        while True:
            print(sug)
            print(" 1 - modificar valor")
            print(" 2 - cálcular")
            print(" 3 - sair")
            nome = input("qual opção: ")
            if nome == "1" :
                return 1
            elif nome == "2":
                return 2
            elif nome == "3":
                return 3
            os.system('cls')
            print("valor não identificado")
if __name__ == "__main__":


    arquivo = pd.read_csv("Trabalho M2/Data set/student-mat.csv")
    teste = pd.read_csv("Trabalho M2/Data set/datasetTestes.csv")
    colunaG3 = arquivo["G3"]
    arquivo = arquivo[["G2","G1", "failures","absences","higher","school","schoolsup","goout","traveltime","famrel","sex"]]
    teste  = teste[["G2","G1", "failures","absences","higher","school","schoolsup","goout","traveltime","famrel","sex"]]
    for i in range(len(arquivo.values)):
        arquivo["G2"][i] = notaAmericana(arquivo["G2"][i])
        arquivo["G1"][i] = notaAmericana(arquivo["G1"][i])
        colunaG3[i] = notaAmericana(colunaG3[i])
    for i in range(len(teste.values)):
        teste["G2"][i] = notaAmericana(teste["G2"][i])
        teste["G1"][i] = notaAmericana(teste["G1"][i])
    sugestao = teste.iloc[0]
    saida = False
    while saida == False:
        print(sugestao )
        resposta1 = menu1(sugestao)
        os.system('cls')
        if resposta1 == 1:
            
            sugestao = men2(sugestao, arquivo)
            os.system('cls')
        elif resposta1 == 2 :
            
            simi = CalculadorDeSimilaridade(arquivo, sugestao)
            arquivo["G3"] = colunaG3
            arquivo["similaridadess"] = simi
            simipor = []
            for i in range(len(simi)):
                simipor.append(str(simi[i]*100) + "%")
            arquivo["similaridade"] = simipor

            Or_arc = arquivo.sort_values(by="similaridadess", ascending=False)
            Or_arc = Or_arc.drop('similaridadess', axis=1)
            print (sugestao, "Resultado de maior similaridade:  ", Or_arc["G3"][0])
            print (Or_arc[0:5])
            input("PQT")
            os.system('cls')
        else:
            saida = True
