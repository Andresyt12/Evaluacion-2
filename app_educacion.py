# app_educacion.py

from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Análisis de Datos de Educación en Colombia")

# Cargar el archivo CSV
uploaded_file = st.file_uploader('educacion.csv', type=["csv"])

# Verificar si el archivo ha sido cargado
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Mostrar la tabla de datos
    st.dataframe(df)

    # Filtros en la barra lateral
    st.sidebar.header("Filtros")
    nivel_educativo = st.sidebar.multiselect("Nivel educativo", df["Nivel educativo"].unique())
    carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
    institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

    # Filtrar los datos
    df_filtrado = df.copy()
    if nivel_educativo:
        df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
    if carrera:
        df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
    if institucion:
        df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

    # Mostrar los datos filtrados
    st.dataframe(df_filtrado)

    # Estadísticas descriptivas
    st.subheader("Estadísticas Descriptivas")
    st.write(df_filtrado.describe())

    # Conteo de estudiantes por nivel educativo
    st.subheader("Conteo de Estudiantes por Nivel Educativo")
    st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

    # Histograma de la columna "Edad"
    st.subheader("Distribución de la Edad")
    fig, ax = plt.subplots()
    ax.hist(df_filtrado["Edad"], bins=10, color='skyblue', edgecolor='black')
    ax.set_xlabel("Edad")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)
else:
    st.write('educacion.csv')
