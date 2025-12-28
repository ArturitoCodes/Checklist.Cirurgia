import streamlit as st

# As tuas checklists (podes mudar ou adicionar mais depois)
checklists = {
    "Apendicectomia": [
        "Bisturi elétrico",
        "Pinças hemostáticas (curvas e retas)",
        "Tesoura de Mayo",
        "Retratores de Balfour",
        "Campos cirúrgicos estéreis",
        "Luvas estéreis",
        "Seringas 10ml",
        "Fios de sutura (vicryl 2-0 e 3-0)",
        "Drenos aspirativos",
        "Compressas estéreis"
    ],
    "Colecistectomia Laparoscópica": [
        "Trocartes (5mm e 10mm)",
        "Ótica 30º",
        "Pinça de disseção Maryland",
        "Clipadora",
        "Bolsa de extração",
        "Insuflador de CO2",
        "Grampeador linear",
        "Campos laparoscópicos",
        "Luvas estéreis"
    ],
    "Cesariana": [
        "Bisturi elétrico",
        "Pinças Kocher",
        "Retratores de Balfour",
        "Aspirador Yankauer",
        "Campos estéreis obstétricos",
        "Fios de sutura (vicryl 1 e 2-0)",
        "Compressas grandes",
        "Luvas estéreis"
    ],
    "Herniorrafia Inguinal": [
        "Malha de polipropileno",
        "Fio de prolene 2-0",
        "Pinças hemostáticas",
        "Retratores autoestáticos",
        "Bisturi elétrico",
        "Anestesia local (lidocaína)",
        "Luvas estéreis"
    ]
}

st.set_page_config(page_title="Checklist Bloco", page_icon="🏥")

st.title("🏥 Checklist de Materiais - Bloco Operatório")
st.markdown("**Verifica todos os itens antes da cirurgia**")

cirurgia = st.selectbox("Escolhe o tipo de cirurgia", options=list(checklists.keys()))

st.subheader(f"Checklist: {cirurgia}")

itens_em_falta = []
for item in checklists[cirurgia]:
    verificado = st.checkbox(item)
    if not verificado:
        itens_em_falta.append(item)

if st.button("🔍 Verificar Checklist", type="primary"):
    if itens_em_falta:
        st.error("⚠️ **ITENS EM FALTA:**")
        for item in itens_em_falta:
            st.write(f"• {item}")
        st.warning("Confirma estes itens antes de começar a cirurgia.")
    else:
        st.success("✅ **Tudo verificado! Cirurgia pode prosseguir com segurança.**")
        st.balloons()  # animação fixe

st.markdown("---")
st.caption("Criado por ti – Enfermeiro do Bloco Operatório 👨‍⚕️💻")