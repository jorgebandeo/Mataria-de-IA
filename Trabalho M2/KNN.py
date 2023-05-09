import pandas as pd
def recot(df,a, nome):
    for j in range (len(a)):
        for i in range (df[nome].shape[0]):
            if df[nome][i] == a[j]:
                df[nome][i] = j
    return df 
def nota(notas, df, nome ):
    for i in range((df["gender"].shape[0])):
        var = int(df[nome][i])
        if var <= 100 and var>= 90: 
            df[nome][i] = notas[0]
        elif var < 90 and var>= 85:
            df[nome][i] = notas[1]
        elif var < 85 and var>= 60:
            df[nome][i] = notas[2]
        elif var < 60 and var>= 40:
            df[nome][i] = notas[3]
        elif var < 40 and var>= 0:
            df[nome][i] = notas[4]
    return df


df = pd.read_csv('Trabalho M2/exams.csv')
sexos = df["gender"].unique()
estnia = df["race/ethnicity"].unique()
ple = df["parental level of education"].unique()
lunch = df["lunch"].unique()
tpc = df["test preparation course"].unique()
df = recot(df, sexos,"gender")
df = recot(df, estnia,"race/ethnicity")
df = recot(df, ple,"parental level of education")
df = recot(df, lunch,"lunch" )
df = recot(df, tpc,"test preparation course" )
notas = [3,2,1, 0, 4]

df = nota(notas, df,"math score")
df = nota(notas, df,"reading score")
df = nota(notas, df,"writing score")

df.to_csv("novo csv", index=False)
    
