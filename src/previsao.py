import numpy as np
from sklearn.linear_model import LinearRegression

# Simulação de carregamento do modelo treinado
# Em ambiente real, usaríamos mlflow.sklearn.load_model("modelo_sorvete")
modelo_simulado = LinearRegression()
modelo_simulado.coef_ = np.array([10])  # Simulando coeficiente
modelo_simulado.intercept_ = 50         # Simulando intercepto

# Entrada de temperatura para previsão
temperatura_dia = 32
vendas_previstas = modelo_simulado.predict([[temperatura_dia]])

print(f"Previsão de vendas para {temperatura_dia}°C: {vendas_previstas[0]:.0f} sorvetes")
