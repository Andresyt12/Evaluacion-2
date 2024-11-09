import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("Análisis de Datos de Educación en Colombia")


uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    st.subheader("Datos de Educación")
    st.dataframe(df)

    
    st.sidebar.header("Filtros")
    
    # Crear filtros solo si las columnas están presentes
    nivel_educativo = []
    carrera = []
    institucion = []

    if "Nivel educativo" in df.columns:
        nivel_educativo = st.sidebar.multiselect(
            "Nivel educativo", options=df["Nivel educativo"].dropna().unique()
        )

    if "Carrera" in df.columns:
        carrera = st.sidebar.multiselect(
            "Carrera", options=df["Carrera"].dropna().unique()
        )

    if "Institución" in df.columns:
        institucion = st.sidebar.multiselect(
            "Institución", options=df["Institución"].dropna().unique()
        )

    # Aplicar filtros al DataFrame
    df_filtrado = df.copy()

    if nivel_educativo:
        df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
    if carrera:
        df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
    if institucion:
        df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

    # Mostrar datos filtrados o un mensaje si no hay coincidencias
    st.subheader("Datos Filtrados")
    if not df_filtrado.empty:
        st.dataframe(df_filtrado)
    else:
        st.warning("No hay datos que coincidan con los filtros seleccionados.")

    # Estadísticas descriptivas
    if not df_filtrado.empty:
        st.subheader("Estadísticas Descriptivas")
        st.write(df_filtrado.describe())
    else:
        st.warning("No se pueden mostrar estadísticas descriptivas debido a la falta de datos filtrados.")

    # Gráficos solo si hay datos filtrados
    if not df_filtrado.empty:
        if "Nivel educativo" in df_filtrado.columns:
            st.subheader("Conteo de Estudiantes por Nivel Educativo")
            st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

        # Histograma de la columna "Edad" solo si está presente
        if "Edad" in df_filtrado.columns:
            st.subheader("Distribución de la Edad")
            fig, ax = plt.subplots()
            ax.hist(df_filtrado["Edad"].dropna(), bins=10, color='skyblue', edgecolor='black')
            ax.set_xlabel("Edad")
            ax.set_ylabel("Frecuencia")
            st.pyplot(fig)
        else:
            st.warning("La columna 'Edad' no está disponible para graficar.")
    else:
        st.warning("No hay datos para generar gráficos.")
else:
    st.info("Por favor, carga un archivo CSV para continuar.")
