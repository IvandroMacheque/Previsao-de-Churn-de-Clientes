import streamlit as st
import pandas as pd
import pickle
import numpy as np

# importar o modelo
with open("forest_treinado.pkl", "rb") as f:
    modelo = pickle.load(f)

# side bar
with st.sidebar:
    st.header('Options')
    options = st.selectbox("Modo", ['Prever Cliente', 'Clientes Previstos', 'Subir CSV'])
    st.markdown("### 🔗 Links Úteis")
    st.markdown("[📁 Este Projeto](https://github.com/IvandroMacheque/Previsao-de-Churn-de-Clientes.git)")
    st.markdown("[👨‍💻 Meu GitHub](https://github.com/IvandroMacheque/IvandroMacheque.git)")
    st.markdown("[💼 Meu LinkedIn](https://www.linkedin.com/in/ivandromacheque?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    

# criando historico de clientes previstos
if "historico" not in st.session_state:
    st.session_state.historico = pd.DataFrame()

# opcao de prever clientes
if options == 'Prever Cliente':
    st.title("🤖 Churn Telecomunication Predict")
    st.write("## Insira os Dados do Cliente")
    # perfil
    st.write("### Perfil:")
    col1, col2, col3 = st.columns(3)
    with col1:
        senior = st.selectbox("Cidadão Senior", ['Yes', 'No'])
    with col2:
        partner = st.selectbox("Possui parceiro", ["Yes", "No"])
    with col3:
        dependentes = st.selectbox("Dependentes?", ['Yes', 'No'])

    tenure = st.number_input("Tempo de Contrato(meses)")

    # servicos de internet
    st.write("### Serviços de Internet:")
    internetservice = st.selectbox("Tipo de Serviço de Internet:", ['DSL', 'Fiber optic', 'No internet service'])
    col4, col5, col6 = st.columns(3)
    col7, col8, col9 = st.columns(3)
    if internetservice == 'No internet service':
        onlinesecurity = 'No internet service'
        onlinebackup = 'No internet service'
        deviceprotection = 'No internet service'
        techsupport = 'No internet service'
        streamingmovies = 'No internet service'
        streamingtv = 'No internet service'
    else:
        with col4:
            onlinesecurity = st.selectbox("Online Security", ['Yes', 'No'])
        with col5:
            onlinebackup = st.selectbox("Online Backup", ['Yes', 'No'])
        with col6:
            deviceprotection = st.selectbox("Device Protection", ['Yes', 'No'])
        with col7:
            techsupport = st.selectbox("Tech Support", ['Yes', 'No'])
        with col8:
            streamingtv = st.selectbox("Streaming TV", ['Yes', 'No'])
        with col9:
            streamingmovies = st.selectbox("Streaming Movies", ['Yes', 'No'])

    # Plano e Pagamento
    st.write("### Plano e Pagamento:")
    col10, col11 = st.columns(2)
    col12, col13, col14 = st.columns(3)
    with col10:
        contract = st.selectbox("Contrato", ['Month-to-month', 'One year', 'Two year'])
    with col11:
        paymentmethod = st.selectbox("Método de Pagamento", ['Eletronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    with col12:
        monthlycharges = st.number_input("Cobranças Mensais (R$)")
    with col13:
        totalcharges = st.number_input("Cobranças Totais (R$)")
    with col14:
        paperlessbilling = st.selectbox("Faturamento sem Papel", ['Yes', 'No'])

    # dados inseridos
    data = {
        'SeniorCitizen': senior,
        'Partner': partner,
        'Dependents': dependentes,
        'tenure' : tenure,
        'InternetService': internetservice,
        'OnlineSecurity': onlinesecurity,
        'OnlineBackup': onlinebackup,
        'DeviceProtection': deviceprotection,
        'TechSupport': techsupport,
        'StreamingTV': streamingtv,
        'StreamingMovies': streamingmovies,
        'Contract': contract,
        'PaperlessBilling': paperlessbilling,
        'PaymentMethod': paymentmethod,
        'MonthlyCharges': monthlycharges,
        'TotalCharges': totalcharges,}
    input_data = pd.DataFrame(data, index=[0])
    bins = [0 , 1300, 3999, np.inf]
    labels = ['baixo', 'medio', 'alto']
    input_data['TotalCharges_Category'] = pd.cut(input_data['TotalCharges'], bins=bins, labels=labels)

    # transformacao dos dados
    mod = {
            'No internet service': 0,
            'No': 1,
            'Yes': 2}
    mod2 = {
            'No': 0,
            'Yes': 1}
    input_data['StreamingTV'] = input_data['StreamingTV'].map(mod)
    input_data['StreamingMovies'] = input_data['StreamingMovies'].map(mod)
    input_data['OnlineBackup'] = input_data['OnlineBackup'].map(mod)
    input_data['DeviceProtection'] = input_data['DeviceProtection'].map(mod)
    input_data['TechSupport'] = input_data['TechSupport'].map(mod)
    input_data['OnlineSecurity'] = input_data['OnlineSecurity'].map(mod)
    input_data['Partner'] = input_data['Partner'].map(mod2)
    input_data['Dependents'] = input_data['Dependents'].map(mod2)
    input_data['PaperlessBilling'] = input_data['PaperlessBilling'].map(mod2)
    input_data['SeniorCitizen'] = input_data['SeniorCitizen'].map(mod2)
    input_data['Contract'] = input_data['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    input_data['TotalCharges_Category'] = input_data['TotalCharges_Category'].map({'baixo': 0, 'medio': 1, 'alto': 2})

    colunas_dummies_esperadas = [
        'InternetService_Fiber optic',
        'InternetService_No',
        'PaymentMethod_Credit card (automatic)',
        'PaymentMethod_Electronic check',
        'PaymentMethod_Mailed check'
    ]
    input_data = pd.get_dummies(input_data, columns=['InternetService', 'PaymentMethod'], drop_first=True) 
    for col in colunas_dummies_esperadas:
        if col not in input_data.columns:
            input_data[col] = 0
    
    if internetservice == 'Fiber optic':
        input_data['InternetService_Fiber optic'] = 1
    elif internetservice == 'No internet service':
        input_data['InternetService_No'] = 1
    if paymentmethod == 'Credit card (automatic)':
        input_data['PaymentMethod_Credit card (automatic)'] = 1
    elif paymentmethod == 'Eletronic check':
        input_data['PaymentMethod_Electronic check'] = 1
    elif paymentmethod == 'Mailed check':
        input_data['PaymentMethod_Mailed check'] = 1

    # funcao de previsao apos o clique do botao
    def prever():

        # dataframe do cliente previsto
        df = {
            'SeniorCitizen': senior,
            'Partner': partner,
            'Dependents': dependentes,
            'tenure' : tenure,
            'InternetService': internetservice,
            'OnlineSecurity': onlinesecurity,
            'OnlineBackup': onlinebackup,
            'DeviceProtection': deviceprotection,
            'TechSupport': techsupport,
            'StreamingTV': streamingtv,
            'StreamingMovies': streamingmovies,
            'Contract': contract,
            'PaperlessBilling': paperlessbilling,
            'PaymentMethod': paymentmethod,
            'MonthlyCharges': monthlycharges,
            'TotalCharges': totalcharges,}
        df_final = pd.DataFrame(df, index=[0])


        # realizando a previsao
        previsao = modelo.predict(input_data)
        previsao_proba = modelo.predict_proba(input_data)
        data_previsao = pd.DataFrame(previsao_proba)
        data_previsao.columns = ['No', 'Yes']
        data_previsao.rename(columns={0: 'No',
                                      1: 'Yes'})
        df_final['Churn'] = previsao
        df_final['Churn'] = df_final['Churn'].replace({0: 'No', 1: 'Yes'})

        st.session_state.historico = pd.concat([st.session_state.historico, df_final], ignore_index=True) # concatenando o cliente previsto ao historico

        # exibicao do resultado
        with resultado_container:
            st.subheader("Previsão")
            st.dataframe(data_previsao,
                         column_config={
                             'Yes': st.column_config.ProgressColumn(
                                 'Yes',
                                 format='%f',
                                 width='medium',
                                 min_value=0,
                                 max_value=1
                             ),
                             'No': st.column_config.ProgressColumn(
                                 'No',
                                 format='%f',
                                 width='medium',
                                 min_value=0,
                                 max_value=1
                             )
                         }, hide_index=True)
            if previsao == 1:
                st.error("Este cliente está propenso a sair!⚠")
            else:
                st.success("Este cliente provavelmente premanecerá!✅")
        
        
    # botao de previsao
    resultado_container = st.container()
    st.button("Realizar Previsão", type="primary", on_click=prever)

elif options == 'Clientes Previstos':
    st.title("📜 Predicted Client's")

    st.dataframe(st.session_state.historico) # exibindo o historico

    # linha de botoes
    but1, but2 = st.columns(2)
    # funcao para limpar o historico
    with but1:
        if not st.session_state.historico.empty:
            def limpar():
                st.session_state.historico = pd.DataFrame()
            st.button("Limpar histórico", on_click=limpar)

    # funcao para salvar o historico
    with but2:
        if not st.session_state.historico.empty:
            def convert_for_download(df):
                df = pd.DataFrame()
                return df.to_csv(index=False).encode("utf-8")
            
            file = convert_for_download(st.session_state.historico)
            st.download_button(
                label="Baixar Histórico",
                data=file,
                file_name='Clientes Previstos.csv',
                mime='text/csv'
            )
else:
    st.title("🗂 Prediction from CSV")

    # inicializando os estados dos botoes
    if 'mostrar_botao1' not in st.session_state:
        st.session_state.mostrar_botao1 = True
    if 'mostrar_botao2' not in st.session_state:
        st.session_state.mostrar_botao2 = False
    
    # subindo o arquivo
    uploaded_file = st.file_uploader("Escolha um arquivo CSV")
    # lendo e exibindo o arquivo
    if uploaded_file is not None:
        dados_inseridos = pd.read_csv(uploaded_file)
        dados_inseridos = dados_inseridos.drop(columns='Unnamed: 0')
        st.dataframe(dados_inseridos)

        # realizando a previsao
        def previsao_CSV():
            st.session_state.mostrar_botao1 = False
            st.session_state.mostrar_botao2 = True 
            previsao_CSV = modelo.predict(dados_inseridos)
            dados_inseridos['Churn'] = previsao_CSV
            dados_inseridos['Churn'] = dados_inseridos['Churn'].replace({0: 'No', 1: 'Yes'})
            with previsao_container:
                st.write("### Predicted Data")
                st.dataframe(dados_inseridos)
        previsao_container = st.container()
        # botao de previsao
        if st.session_state.mostrar_botao1:
            st.button("Realizar Previsão", on_click=previsao_CSV)

        # converter arquivo
        def converter(df):
            df = pd.DataFrame()
            return df.to_csv(index=False).encode("utf-8")
        # remover botao de download
        def remover_but():
            st.session_state.mostrar_botao2 = False
            with success_container:
                st.success("✅ Download realizado com sucesso!")
        # botao de download
        success_container = st.container()
        if st.session_state.mostrar_botao2:
            arquivo = converter(dados_inseridos)
            st.download_button(
                label="Download Data",
                data=arquivo,
                file_name='Predicted Data.csv',
                mime='text/csv',
                on_click=remover_but
                )

