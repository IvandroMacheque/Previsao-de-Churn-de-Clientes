# Churn Telecommunication Predict 🤖

Este projeto consiste numa aplicação de Machine Learning para prever a probabilidade de um cliente cancelar um serviço de telecomunicações (churn). O processo abrange desde a Análise Exploratória dos Dados (EDA), passando pelo pré-processamento, treino e avaliação de múltiplos modelos de classificação, até à implementação de uma aplicação web interativa com Streamlit para realizar previsões em tempo real.

# Principais Funcionalidades

**Análise Exploratória de Dados (EDA)**: Investigação aprofundada do dataset Telco Customer Churn para identificar padrões, correlações e insights sobre os fatores que influenciam o cancelamento de clientes.

**Pré-processamento de Dados**: Limpeza, tratamento de valores em falta, normalização de dados categóricos e engenharia de novas features para otimizar o desempenho dos modelos.

**Treino, Avaliação e Otimização de Modelos**: Processo iterativo de treino e avaliação de modelos, com foco especial na otimização do Random Forest para corrigir overfitting e alinhar as métricas (Recall e Precisão) com os objetivos de negócio.

**Seleção do Melhor Modelo**: O modelo Random Forest, após um rigoroso processo de ajuste de hiperparâmetros e seleção de features, foi escolhido como o mais robusto e com melhor performance para o problema.

# Metodologia de Modelagem e Otimização
A abordagem de modelagem foi iterativa, focada em resolver um problema de negócio específico: identificar com a maior precisão possível os clientes propensos a cancelar o serviço (churn).

1. **Modelo Base e Overfitting**: O treino inicial com o Random Forest apresentou um bom desempenho nos dados de treino, mas foi identificado um claro sinal de overfitting. O modelo estava demasiado ajustado aos dados de treino, o que comprometia a sua capacidade de generalizar para novos dados.
2. **Teste com Modelos Alternativos**: Para buscar uma alternativa, foi treinado um Ridge Classifier (uma forma de Regressão Logística). No entanto, este apresentou um desempenho geral muito inferior, sendo inadequado para o problema.
3. **Refinamento e Otimização do Random Forest**: Com base nos resultados, o foco voltou a ser o Random Forest, aplicando as seguintes melhorias:
 - **Seleção de Features**: Foi realizada uma análise da correlação e da importância das features. Variáveis que causavam ruído ou tinham baixa relevância para o modelo (Dependents, SeniorCitizen, etc.) foram removidas para simplificar e melhorar a performance.
 - **Ajuste de Hiperparâmetros**: Em vez de apenas ajustes manuais, foi utilizado o RandomizedSearchCV para testar sistematicamente diferentes combinações de parâmetros (*n_estimators*, *max_depth*, *min_samples_split*, etc.).
 - **Foco Estratégico em Recall e Precisão**: A otimização teve como objetivo principal obter um Recall alto, pois para o negócio é mais custoso não identificar um cliente que vai cancelar do que classificar incorretamente um que não vai. Após atingir um bom Recall, o modelo foi ajustado para aumentar também a Precisão, garantindo um equilíbrio essencial.
4. **Modelo Final**: O resultado deste processo foi um modelo Random Forest robusto, com overfitting significativamente reduzido e um excelente balanço entre identificar corretamente os clientes que irão cancelar e manter uma alta precisão geral, como demonstrado pelas métricas finais de avaliação e pela validação cruzada.

**Aplicação Web Interativa**: Uma interface web desenvolvida com Streamlit que permite:

1. Inserir os dados de um novo cliente através de um formulário interativo.

2. Obter uma previsão de probabilidade de churn (Sim/Não).

3. Manter um histórico de clientes previstos durante a sessão.

4. Limpar e fazer o download do histórico de previsões.

# Ficheiros do Projeto

*EDA.ipynb*: Jupyter Notebook contendo toda a Análise Exploratória de Dados, pré-processamento e visualizações.

*ML.ipynb*: Jupyter Notebook com o processo de treino, avaliação e comparação dos modelos de Machine Learning.

*app.py*: Script Python que executa a aplicação web com Streamlit.

*modelo_forest_comprimido.joblib*: Ficheiro do modelo Random Forest final, treinado com os melhores hiperparâmetros e salvo de forma comprimida com joblib.

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