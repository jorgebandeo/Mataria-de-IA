import pandas as pd
import csv

matriz = []
df = pd.read_csv('Trabalho M2\student-mat.csv')

with open('Trabalho M2\student-mat.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for linha in reader:
        matriz.append(linha)
valores_das_colunas = []
for i in matriz[0]:
    valores_das_colunas.append(df[i].unique()) 
for i in range(len(matriz[0])):
    print(matriz[0][i], " ___ ", valores_das_colunas[i])
    


