import streamlit as st

st.set_page_config(page_title="Portal Lunelli", page_icon="", layout="wide")

# ===== Estilo Lunelli =====
st.markdown("""
<style>
:root {
  --lunelli-white: #fff;
  --lunelli-blue: #003366;
  --lunelli-blue-hover: #004b99;
  --lunelli-muted: #667085;
}
.main-title { 
  text-align:center; 
  font-size:40px; 
  font-weight:800; 
  color:var(--lunelli-white); 
  margin: 4px 0 6px 0; 
}
.subtitle {
  text-align:center; 
  color:var(--lunelli-white); 
  margin-bottom:28px; 
}
.stButton > button {
  display: block;
  background: var(--lunelli-blue);
  margin: 10px auto;
  width: 250px;
  font-size: 18px;
  font-weight: bold;
  border-radius: 10px;
  transition: .2s;
}
.stButton>button:hover { 
  background: var(--lunelli-blue-hover);
  transform: translateY(-1px); 
}
.block-container {
  padding-top: 1.6rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'> Computadores Lunelli</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Selecione uma unidade</div>", unsafe_allow_html=True)

dashboards = {'VESTUARIO': '01_VESTUARIO.py', 'MASSARANDUBA': '02_MASSARANDUBA.py', 'TEXTIL': '03_TEXTIL.py', 'LUIZALVES': '04_LUIZALVES.py', 'COMERCIAL': '05_COMERCIAL.py', 'BENEFICIAMENTOS': '06_BENEFICIAMENTOS.py', 'NORDESTE': '07_NORDESTE.py', 'AVARE': '08_AVARE.py', 'SHOWROOM': '09_SHOWROOM.py', 'LNDLNB': '10_LNDLNB.py', 'OUT': '11_OUT.py', 'PARAGUAI': '12_PARAGUAI.py', 'ABI': '13_ABI.py', 'FORAPADRAO': '14_FORAPADRAO.py', 'CONFECCAO': '15_CONFECCAO.py', 'AJD': '16_AJD.py'}

cols = st.columns(4)
for i, (aba, arquivo) in enumerate(dashboards.items()):
    if cols[i % 4].button(aba):
        st.switch_page(f"pages/{arquivo}")
