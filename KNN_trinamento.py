# Importar as bibliotecas necessárias
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados a partir do arquivo CSV
df = pd.read_csv('novo csv')

# Separar as colunas de entrada dos rótulos de saída
X = df.drop(["writing score"], axis=1)
y = df[["writing score"]]

# Normalizar as colunas usando a técnica Z-score
scaler = StandardScaler()
X_norm = scaler.fit_transform(X)

# Dividir o conjunto de dados em um conjunto de treinamento e um conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.3, random_state=85)

# Criar o classificador KNN com um valor de k igual a 3
knn = KNeighborsClassifier(n_neighbors=7,metric='manhattan')

# Treinar o classificador usando o conjunto de treinamento
knn.fit(X_train, y_train)

# Fazer previsões usando o conjunto de teste
y_pred = knn.predict(X_test)



# Calcular a acurácia
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a acurácia
print("Acurácia do modelo: {:.2f}%".format(accuracy * 100))