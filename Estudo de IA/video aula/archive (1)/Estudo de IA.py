import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
#abre o arquivo de trinamento
df = pd.read_csv("Inteligencia Artificial/Estudo de IA/video aula/archive (1)/wine_dataset.csv")

#troca variaveis logicas em binarias
df["style"] = df["style"].replace("red",0)
df["style"] = df["style"].replace("white",1)

#separação das variaveis de entrada e de saida
saida = df["style"]
entrada = df.drop("style", axis=1)# separa o style do resto

#cria o conjunto de dados e testes
entrada_trino, entrada_teste, saida_treino, saida_teste = train_test_split(entrada, saida, test_size=0.3)

#criação do modelo
modelo = ExtraTreesClassifier()
modelo.fit(entrada_trino, saida_treino)

# testa
resultados = modelo.score(entrada_teste, saida_teste)

print("Acurácia:",resultados )

#previção
previcao = modelo.predict(entrada_teste[0:10])
print(previcao)
print(saida_teste[0:10])