import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn

# Simulando dados extraídos do arquivo inputs/dados.txt
dados = pd.DataFrame({
    'Temperatura': [30, 22, 28],
    'Vendas': [250, 140, 210]
})

# Treinamento do modelo
modelo = LinearRegression()
modelo.fit(dados[['Temperatura']], dados['Vendas'])

# Simulação de ambiente MLflow na Azure
mlflow.set_tracking_uri("https://mlflow.azure.com")  # Simulação de URI
mlflow.set_experiment("Previsao_Vendas_Sorvete")

with mlflow.start_run():
    mlflow.log_param("modelo", "LinearRegression")
    mlflow.log_param("variavel_independente", "Temperatura")
    mlflow.log_metric("score", modelo.score(dados[['Temperatura']], dados['Vendas']))
    mlflow.sklearn.log_model(modelo, "modelo_sorvete")

    print("Modelo treinado e registrado com sucesso no MLflow (simulado).")
