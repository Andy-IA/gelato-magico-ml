# 🍦 Gelato Mágico - Previsão de Vendas com Machine Learning

Este projeto simula a criação teórica de um modelo preditivo para prever vendas de sorvete com base na temperatura do dia. Utilizando regressão linear e MLflow, o objetivo é ajudar sorveterias a planejarem melhor sua produção, reduzindo desperdícios e maximizando lucros.

---

## 📊 Objetivo

- Treinar um modelo de Machine Learning para prever vendas com base na temperatura.
- Registrar e gerenciar o modelo usando MLflow (simulado).
- Implementar o modelo para previsões em tempo real em ambiente de nuvem (simulado).
- Criar um pipeline estruturado e reprodutível.

---

## 🧪 Processo

1. **Coleta de dados simulados**  
   As frases foram inseridas no arquivo `inputs/dados.txt`:

"Hoje fez 30°C e vendemos 250 sorvetes. A temperatura foi de 22°C e as vendas foram 140 unidades. Com 28°C, tivemos 210 sorvetes vendidos."


2. **Pré-processamento dos dados**  
Os dados foram convertidos para uma tabela estruturada com colunas `Temperatura` e `Vendas`.

3. **Treinamento do modelo**  
Utilizamos regressão linear com a biblioteca `scikit-learn` para encontrar a relação entre temperatura e vendas.

4. **Registro com MLflow (simulado)**  
O modelo foi registrado com MLflow, incluindo parâmetros e métricas como `score` de desempenho.

5. **Previsão em tempo real (simulada)**  
Criamos um script que recebe a temperatura do dia e retorna a previsão de vendas.

---

## 📸 Prints

> ⚠️ Como este projeto é uma simulação, os prints abaixo representam o que seria visto em um ambiente real.

- 📈 Gráfico de regressão linear mostrando a correlação entre temperatura e vendas.
- 🧪 Interface do MLflow com parâmetros e métricas registrados.
- 🖥️ Terminal exibindo a previsão de vendas para uma temperatura de 32°C.

---

## 💡 Insights

- Existe uma forte correlação positiva entre temperatura e vendas de sorvete.
- Temperaturas acima de 28°C tendem a aumentar significativamente a demanda.
- O modelo pode ser expandido para incluir variáveis como dia da semana, clima (sol/nuvens), feriados e sabores mais vendidos.

---

## 🚀 Possibilidades Futuras

- Criar uma API com Flask ou Streamlit para uso em tempo real.
- Integrar com dados meteorológicos reais via API.
- Automatizar a produção diária com base nas previsões.

---

## 📂 Estrutura do Projeto


- `gelato-magico-ml/` → Pasta principal do projeto.
- `inputs/` → Contém os dados de entrada simulados.
- `src/` → Scripts de treinamento e previsão do modelo.
- `README.md` → Documentação do projeto com prints, insights e explicações.



