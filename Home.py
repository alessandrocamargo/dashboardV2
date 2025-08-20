import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portal Lunelli", layout="wide")

st.title("Portal de Dashboards - Lunelli")

# Carregar o Excel
xls = pd.ExcelFile("computadoresLunelliv4.xlsx")

st.markdown("### Total de Máquinas por Unidade")

# Layout em colunas dinâmico (3 cards por linha)
cols = st.columns(3)
i = 0

for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)

    total = df.shape[0]
    win10 = df[df["Operating system"].str.contains("Windows 10", case=False, na=False)].shape[0]
    win11 = df[df["Operating system"].str.contains("Windows 11", case=False, na=False)].shape[0]

    with cols[i]:
        st.markdown(
            f"""
            <div style="
                background-color:#004080;
                color:white;
                text-align:center;
                padding:20px;
                border-radius:15px;
                box-shadow:2px 2px 10px rgba(0,0,0,0.2);
                font-size:18px;
                font-weight:bold;
                margin-bottom:20px;
            ">
                {sheet}<br>
                <span style="font-size:22px;">Total: {total}</span><br>
                <span style="font-size:18px;">Windows 10: {win10}</span><br>
                <span style="font-size:18px;">Windows 11: {win11}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    i += 1
    if i == 3:  # quebra de linha a cada 3 unidades
        i = 0
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(3)  # nova linha
# ---------- CARD GERAL ----------
total_maquinas = 0
for sheet in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    total_maquinas += df.shape[0]


st.markdown("### Total Geral de Máquinas ")
st.markdown(
    f"""
    <div style="
        background-color:#008000;
        color:white;
        text-align:center;
        padding:25px;
        border-radius:15px;
        box-shadow:2px 2px 10px rgba(0,0,0,0.2);
        font-size:20px;
        font-weight:bold;
        margin-bottom:30px;
    ">
        <span style="font-size:28px;">{total_maquinas}</span>
    </div>
    """,
    unsafe_allow_html=True
)