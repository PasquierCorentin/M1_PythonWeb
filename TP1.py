import os
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
    st.title("DATA EXPLORER App")
    st.subheader("A datascience app using Streamlit")

    def file_selector(folder_path='./Data'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Selectionner un fichier", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.info("Vous avez sélectionné {}".format(filename))

    #Read Data
    df = pd.read_csv(filename)

    #Show Dataset
    if st.checkbox("Afficher le Dataset"):
        number = st.number_input("Nombre de lignes à afficher")
        st.dataframe(df.head(number))

    #Show Columns
    if st.checkbox("Afficher les colonnes"):
        st.write(df.columns)

    #Show Shape
    if st.checkbox("Afficher la 'shape' du dataset"):
        data_dim = st.radio("Afficher dimension par",("Lignes", "Colonnes", "Lignes & Colonnes"))
        if data_dim == 'Lignes':
            st.text("Nombre de lignes")
            st.write(df.shape[0])
        elif data_dim == 'Colonnes':
            st.text("Nombre de colonnes")
            st.write(df.shape[1])
        elif data_dim == "Lignes & Colonnes":
            st.text("Dimension du Dataset")
            st.write(df.shape)

    #Select Columns
    if st.checkbox("Selectionner les colonnes à afficher"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Selectionner",all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    #Show Values
    if st.button("Nombre de valeurs"):
        st.text("Comptage des valeurs par Target/Class")
        st.write(df.iloc[:,-1].value_counts())
    
    #Show Summary

    ## PLot and Visualization


if __name__ == '__main__':
    main()











# st.title('WELCOME to my Data Explorer App !')

# #------------------------------------------------------------------------

# DATE_COLUMN = 'date/time'
# DATA_URL = ('Data/all_seasons.csv')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data



# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Done! (using st.cache)")

# st.subheader('Raw data')
# st.write(data)

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(
#    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)

#st.subheader('Map of all pickups')
#st.map(data)

#hour_to_filter = 17
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader(f'Map of all pickups at {hour_to_filter}:00')
#st.map(filtered_data)