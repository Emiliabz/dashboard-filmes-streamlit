import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Simples com Streamlit")

# Dados de exemplo
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

st.subheader("Dados em DataFrame")
st.dataframe(data)

st.subheader("Gráfico com Plotly")
fig = px.line(data, x='x', y='y', title='Linha Simples')
st.plotly_chart(fig)