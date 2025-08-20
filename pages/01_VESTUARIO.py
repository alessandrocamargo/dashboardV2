import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Dashboard da Unidade")

# Carregar Excel
df = pd.read_excel("computadoresLunelliv4.xlsx", sheet_name="VESTUARIO")

# Título do app
st.markdown("""
<div style='text-align: center'>
    <h1>Unidade: VESTUARIO</h1>
</div>
""", unsafe_allow_html=True)

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
st.dataframe(df_filtrado[["Name", "CPU", "Operating system", "Usuario", "Setor"]].reset_index(drop=True))


# ---------------------- EXPORTAR ----------------------
st.markdown("### Exportar dados filtrados")

# Excel
output = BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    df_filtrado.to_excel(writer, index=False, sheet_name="Filtrado")

st.download_button(
    label="📥 Exportar Excel",
    data=output.getvalue(),
    file_name="vestuario.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)