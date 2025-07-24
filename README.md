# Churn Telecommunication Predict 🤖

Este projeto consiste numa aplicação de Machine Learning para prever a probabilidade de um cliente cancelar um serviço de telecomunicações (churn). O processo abrange desde a Análise Exploratória dos Dados (EDA), passando pelo pré-processamento, treino e avaliação de múltiplos modelos de classificação, até à implementação de uma aplicação web interativa com Streamlit para realizar previsões em tempo real.

# Principais Funcionalidades

**Análise Exploratória de Dados (EDA)**: Investigação aprofundada do dataset Telco Customer Churn para identificar padrões, correlações e insights sobre os fatores que influenciam o cancelamento de clientes.

**Pré-processamento de Dados**: Limpeza, tratamento de valores em falta, normalização de dados categóricos e engenharia de novas features para otimizar o desempenho dos modelos.

**Treino e Avaliação de Modelos**: Foram treinados e comparados quatro modelos de classificação diferentes para identificar o de melhor desempenho:

 - Random Forest

 - Regressão Logística

 - XGBoost

 - Gradient Boosting

**Seleção do Melhor Modelo**: O modelo **Random Forest** foi selecionado como o melhor com base em métricas como Acurácia, Precisão, Recall e AUC-ROC, apresentando o menor overfitting após validação cruzada.

**Aplicação Web Interativa**: Uma interface web desenvolvida com Streamlit que permite:

1. Inserir os dados de um novo cliente através de um formulário interativo.

2. Obter uma previsão de probabilidade de churn (Sim/Não).

3. Manter um histórico de clientes previstos durante a sessão.

4. Limpar e fazer o download do histórico de previsões.

# Ficheiros do Projeto

*EDA.ipynb*: Jupyter Notebook contendo toda a Análise Exploratória de Dados, pré-processamento e visualizações.

*ML.ipynb*: Jupyter Notebook com o processo de treino, avaliação e comparação dos modelos de Machine Learning.

*app.py*: Script Python que executa a aplicação web com Streamlit.

*forest_treinado.pkl*: Ficheiro do modelo Random Forest treinado e salvo (serializado com Pickle).

*Telco_Recent.csv*: Dataset processado e limpo, exportado do notebook EDA.ipynb.

*WA_Fn-UseC_-Telco-Customer-Churn.csv*: O dataset original utilizado no projeto.

*requirements.txt*: Ficheiro com as bibliotecas Python necessárias para executar o projeto.

# Tecnologias e Bibliotecas Utilizadas

**Linguagem**: Python 3

**Análise e Manipulação de Dados**: Pandas, NumPy

**Visualização de Dados**: Matplotlib, Seaborn

**Machine Learning**: Scikit-learn, XGBoost

**Aplicação Web**: Streamlit

**Serialização do Modelo**: Pickle

# Como Utilizar a Aplicação

A aplicação possui uma barra lateral com três modos de operação:

1. **Prever Cliente**:

 - Preencha o formulário com os dados do perfil, serviços de internet, e plano de pagamento do cliente.

 - Clique no botão "Prever".

 - O resultado será exibido, mostrando as probabilidades de o cliente cancelar ("Yes") ou não ("No"), juntamente com uma mensagem de alerta ou sucesso.

2. **Clientes Previstos**:

 - Neste modo, é exibida uma tabela com o histórico de todos os clientes cujas previsões foram feitas na sessão atual.

 - Pode limpar o histórico clicando no botão "Limpar histórico".

 - Pode também fazer o download do histórico para um ficheiro CSV clicando em "Baixar Histórico".

3. **Subir CSV**:

 - Neste último modo, o usuário pode subir um arquivo csv (que esteja limpado e organizado) para realizar a previsão do dataset.

 - Após a previsão, tem a possibilidade de salvar o arquivo com as previsões em formato CSV.

# Link da Aplicação

https://previsao-de-churn-de-clientes.streamlit.app/
