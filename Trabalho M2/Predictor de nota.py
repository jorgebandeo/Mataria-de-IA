
import os
import pandas as pd

# Função para converter uma nota em formato numérico para o formato de notas americanas (A, B, C, D, F)
def notaAmericana(numero):
    if numero >= 16:
        return 'A'
    elif numero >= 14:
        return 'B'
    elif numero >= 12:
        return 'C'
    elif numero >= 10:
        return 'D'
    else: 
        return 'F'

# Função para encontrar o maior valor em uma coluna de um DataFrame
def maior(df, nome_coluna):
    maior_valor = df[nome_coluna].max()
    return maior_valor

# Função para encontrar o menor valor em uma coluna de um DataFrame
def menor(df, nome_coluna):
    menor_valor = df[nome_coluna].min()
    return menor_valor

# Dicionário de pesos para as colunas do DataFrame
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

# Dicionário de tipos de similaridade para as colunas do DataFrame
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

# Função para calcular a similaridade numérica entre dois valores
def SimilaridadeNumerica(F1, F2, max, min):
    # 1 - | F1 - F2 | / (max - min)
    a = F1 - F2 if F1 > F2  else F2 - F1 # | F1 - F2 |
    return 1 - a / (max - min)

# Função para calcular a similaridade booleana entre dois valores
def SimilaridadeBooleana(F1, F2):
    a = 1 if F1 == F2 else 0
    return  a

# Função para calcular a similaridade lógica entre dois valores
def SimilaridadeLolica(F1, F2, valores):
    elementos = {}
    distribuicao = 0
    # Distribui percentualmente os elementos no dicionário
    for i in range(len(valores)):
        distribuicao += 1 / len(valores)
        elementos[valores[i]] = distribuicao
    # Igual ao método SimilaridadeNumerica, mas utiliza o auxílio do dicionário elementos
    F1 = elementos[F1]
    F2 = elementos[F2]
    a = F1 - F2 if F1 > F2  else F2 - F1
    return 1 - a / 1

# Função para calcular a similaridade entre o DataFrame de arquivo e uma linha de predição
def CalculadorDeSimilaridade(Arquivo, predict):

    colunas = Arquivo.columns.to_list()
    semelhanca = []
    pessom = 0
    for i in colunas:
        pessom += pesos[i]
    linas = []
    for i in range(0, len(Arquivo.values)):
        somas = 0
        coll =[]
        for j in colunas:
            
            if 1 == TS[j]:
                aux = pesos[j] * SimilaridadeNumerica(Arquivo[j][i], predict[j], maior(Arquivo,j), menor(Arquivo,j))
                somas += aux
            elif 2 == TS[j]:
                aux = pesos[j] * SimilaridadeBooleana(Arquivo[j][i], predict[j])
                somas += aux
            else:
                aux = pesos[j] * SimilaridadeLolica(Arquivo[j][i], predict[j], Arquivo[j].unique())
                somas += aux
            
        semelhanca.append(somas / pessom)
    return semelhanca

# Função para permitir a alteração de um valor no DataFrame
def men2(suges, arc):
    colunas = arc.columns.to_list()
    while True:
        os.system('cls')
        print(suges)
        print("Digite o elemento que quer mudar")
        op = input("Qual opção: ")
        for i in colunas:
            if op == i:
                while True:
                    os.system('cls')
                    print(suges)
                    print("Os valores possíveis são:", arc[i].unique())
                    pe1 = input("Valor: ")
                    for j in arc[i].unique():
                        if pe1 == str(j):
                            
                            if type(j) != str:
                                pe1 = int(pe1)
                            suges[i] = pe1
                            return suges

# Função para exibir o menu de opções
def menu1(sug):
    os.system('cls')
    while True:
        print(sug)
        print(" 1 - Modificar valor")
        print(" 2 - Calcular")
        print(" 3 - Sair")
        nome = input("Qual opção: ")
        if nome == "1":
            return 1
        elif nome == "2":
            return 2
        elif nome == "3":
            return 3
        os.system('cls')
        print("Valor não identificado")

# Parte principal do código
if __name__ == "__main__":
    # Leitura dos arquivos CSV e seleção das colunas relevantes
    arquivo = pd.read_csv("Data set/student-mat.csv")
    teste = pd.read_csv("Data set/datasetTestes.csv")
    colunaG3 = arquivo["G3"]
    arquivo = arquivo[["G2", "G1", "failures", "absences", "higher", "school", "schoolsup", "goout", "traveltime", "famrel", "sex"]]
    teste = teste[["G2", "G1", "failures", "absences", "higher", "school", "schoolsup", "goout", "traveltime", "famrel", "sex"]]

    # Conversão das notas para o formato americano
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
        print(sugestao)
        resposta1 = menu1(sugestao)
        os.system('cls')
        if resposta1 == 1:
            sugestao = men2(sugestao, arquivo)
            os.system('cls')
        elif resposta1 == 2:
            copia = arquivo.copy()
            simi = CalculadorDeSimilaridade(copia, sugestao)
            copia["G3"] = colunaG3
            copia["similaridadess"] = simi
            simipor = []
            for i in range(len(simi)):
                simipor.append(str(simi[i] * 100) + "%")
            copia["similaridade"] = simipor

            Or_arc = copia.sort_values(by="similaridadess", ascending=False)
            Or_arc = Or_arc.drop('similaridadess', axis=1)
            print(sugestao, "Resultado de maior similaridade:", Or_arc["G3"][0])
            print(Or_arc[0:5])
            input("PQT")
            os.system('cls')
        else:
            saida = True