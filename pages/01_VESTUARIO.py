import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lunelli", page_icon="", layout="wide")

# Botão de retorno estilizado
st.markdown("""
    <style>
        .stButton>button {
            background-color: #ff6600;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #e65c00;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Título do app
st.markdown("""
<div style='text-align: center'>
    <h1>Unidade: VESTUÁRIO</h1>
</div>
""", unsafe_allow_html=True)


# Carregar dados
df = pd.read_excel("computadoresLunelliv4.xlsx", sheet_name="VESTUARIO")

# Limpar dados de sistema operacional
df["Operating system"] = df["Operating system"].astype(str).str.replace("<|>", "", regex=True).str.strip()

# Filtro por sistema operacional
sistemas = sorted(df["Operating system"].dropna().unique())
sistema_escolhido = st.selectbox("🖥️ Selecione o Sistema Operacional", sistemas)

# Filtrar o DataFrame
df_filtrado = df[df["Operating system"] == sistema_escolhido]

# Mostrar total
st.markdown(f"**Total de máquinas com {sistema_escolhido}:** {len(df_filtrado)}")

# # Gráfico de CPUs
# st.subheader("📊 Processadores mais comuns")
# cpu_count = df_filtrado["CPU"].value_counts().reset_index()
# cpu_count.columns = ["CPU", "Quantidade"]

# fig = px.funnel(cpu_count, x="Quantidade", y="CPU", orientation="h", title="Distribuição de CPUs")
# st.plotly_chart(fig, use_container_width=True)

# Lista de máquinas
st.subheader("📋 Máquinas Detalhadas")
st.dataframe(df_filtrado[["Name", "CPU", "Operating system"]].reset_index(drop=True))



