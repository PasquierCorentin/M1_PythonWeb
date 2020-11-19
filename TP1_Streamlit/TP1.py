import os
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.title("DATA EXPLORER APP")
    st.subheader("Selection et présentation du DATASET")

    def file_selector(folder_path='./Data'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Selectionner un fichier", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.info("Vous avez sélectionné {}".format(filename))


    #Read Data
    df = pd.read_csv(filename)

    #Show Dataset
    number = st.number_input("Nombre de lignes à afficher", value=5.00)
    number = int(number)
    st.dataframe(df.head(number))


    #Spacing
    st.write("")
    st.write("")
    st.write("")

    #Show Shape
    left_column, right_column = st.beta_columns(2)

    left_column.subheader("Shape du dataset")

    #Centrer horizontallement (Oups..)
    right_column.write("")
    right_column.write("")
    right_column.write("")


    data_dim = left_column.radio("Afficher dimension par",("Lignes & Colonnes","Lignes", "Colonnes"))
    if data_dim == "Lignes & Colonnes":
        right_column.write("Dimensions du Dataset")
        right_column.write(df.shape)
    elif data_dim == 'Lignes':
        right_column.write("Nombre de lignes")
        right_column.write(df.shape[0])
    elif data_dim == 'Colonnes':
        right_column.write("Nombre de colonnes")
        right_column.write(df.shape[1])

    #Layout
    left_column, right_column = st.beta_columns(2)  

    #Show Columns
    left_column.subheader("Colonnes du Dataset")
    left_column.write(df.columns)

    #Show Columns Datatypes
    right_column.subheader("Types des data")
    right_column.write(df.dtypes)
    
    #Show Specific columns
    with st.beta_expander("Affichage de colonnes spécifiques"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Selectionner les colonnes à afficher",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)    

    #Count Values
    with st.beta_expander("Nombre d'occurences des valeurs"):
        st.write("Comptage des différentes occurences de valeurs de la colonne")
        all_columns2 = df.columns.tolist()
        colmuns_ids = list(range(len(all_columns2)))
        selected_column_id = st.selectbox("Selectionner la colonne à compter", colmuns_ids, format_func=lambda x: all_columns2[x])
        #count_df = df[selected_column2]
        st.write(df.iloc[:,selected_column_id].value_counts())
    
    #Show Dataset Stats
    with st.beta_expander("Statistiques du Dataset"):
        st.write(df.describe().T)

    #Spacing
    st.write("")
    st.write("")
    st.write("")
    
    ## PLot and Visualisation

    st.subheader("Data Visualisation")

    #Correlation

    # Seaborn Plot
    with st.beta_expander("CorrelationPlot"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
        
    # Pie Chart
    with st.beta_expander("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate Pie Plot"):
            st.success("Generating A Pie Plot")
            st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

        # Count Plot
    with st.beta_expander("Plot of Value Counts"):
        st.text("Value Counts By Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
        selected_columns_names = st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()


    #Custom Plot
    with st.beta_expander("Custom Plot"):    
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Selectionner le type de graphique",["Area","Bar","Line","box","kde"])
        selected_columns_names = st.multiselect("Selectionner les colonnes à utiliser", all_columns_names)

        if st.button("Generer Graphique"):
            st.success("Création du Graphique de type {} pour les colonnes {}".format(type_of_plot, selected_columns_names))

            if type_of_plot == 'Area':
                cust_data = df[selected_columns_names]
                st.area_chart(cust_data)
            
            elif type_of_plot == 'Bar':
                cust_data = df[selected_columns_names]
                st.bar_chart(cust_data)
            
            elif type_of_plot == 'Line':
                cust_data = df[selected_columns_names]
                st.line_chart(cust_data)
            
            elif type_of_plot:
                cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
                st.write(cust_plot)
                st.pyplot()

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    left_column, mid_column, right_column = st.beta_columns(3)

    if mid_column.button("MERCI"):
        st.balloons()




if __name__ == '__main__':
    main()

