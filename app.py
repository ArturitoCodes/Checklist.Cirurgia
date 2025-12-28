import streamlit as st

# Estrutura: Especialidade → Cirurgia → Abordagem → Tipo (Urgência/Programada)
checklists = {
    "Obstetrícia/Ginecologia": {
        "Cesariana": {
            "Aberta": {
                "Programada": [
                    "Betadine",
                    "Bisturi elétrico",
                    "Placa adulto",
                    "Aspirador",
                    "Canula Yankauer",
                    "Lâmina 24",
                    "Trouxa de cesariana",
                    "Fios de sutura (vicryl 1, vicryl 0, monocryl 3-0)",
                    "Compressas grandes",
                    "Compressas médias",
                    "Luvas estéreis",
                    "Lidogel",
                    "Algália 16 Látex",
                    "Saco de Urina 2L",
                    "Seringa de 10cc de Água Bi",
                    "Penso impermeável 25cm"
                ],
                "Urgência": [
                    "Kit de emergência obstétrica",
                    "Oxitocina pronta",
                    "Adrenalina 1:1000"
                ]  # itens extras para urgência
            }
        },
        "Histerectomia": {
            "Aberta": {
                "Programada": [
                    "Itens base histerectomia aberta programada"
                ],
                "Urgência": [
                    "Itens extra urgência histerectomia"
                ]
            },
            "Laparoscópica": {
                "Programada": [
                    "Trocartes, ótica, clipadora..."
                ],
                "Urgência": []
            }
        }
    },
    "Cirurgia Geral": {
        "Apendicectomia": {
            "Aberta": {
                "Programada": [
                    "Bisturi elétrico",
                    "Pinças hemostáticas",
                    "Tesoura de Mayo",
                    "Retratores de Balfour",
                    "Campos estéreis",
                    "Luvas estéreis",
                    "Fios de sutura (vicryl 2-0 e 3-0)",
                    "Drenos aspirativos",
                    "Compressas estéreis"
                ],
                "Urgência": [
                    "Antibiótico IV pronto",
                    "Soro aquecido"
                ]
            },
            "Laparoscópica": {
                "Programada": [
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
                "Urgência": [
                    "Kit de conversão para aberta (por segurança)"
                ]
            }
        },
        "Colecistectomia": {
            "Laparoscópica": {
                "Programada": [
                    "Trocartes, ótica, clipadora..."
                ],
                "Urgência": [
                    "Antibiótico profilático IV"
                ]
            }
        }
    },
    "ORL": {
        "Adenoidectomia": {
            "Endoscópica": {
                "Programada": [
                    "Itens base adenoides programada"
                ],
                "Urgência": [
                    "Bipolar com canula de aspiração para acopolar",
                    "Adrenalina tópica",
                    "Kit de hemorragia"
                ]
            }
        }
    },
    "Ortopedia": {
        "Artroscopia de Joelho": {
            "Artroscópica": {
                "Programada": [
                    "Ótica 30º 4mm",
                    "Shaver e bomba de irrigação",
                    "Pinças de basket",
                    "Canulas arthroscópicas",
                    "Solução de irrigação (soro 3L)",
                    "Torniquete pneumático",
                    "Campos estéreis",
                    "Luvas estéreis"
                ],
                "Urgência": [
                    "Antibiótico IV",
                    "Analgesia intra-articular pronta"
                ]
            }
        }
    }
    # Adiciona mais especialidades, cirurgias, abordagens conforme precisares
}

st.set_page_config(page_title="Checklist Bloco Operatório", page_icon="🏥")

st.title("🏥 Checklist de Materiais - Bloco Operatório")
st.markdown("**Seleciona passo a passo para gerar a checklist correta**")

# 1. Especialidade
especialidade = st.selectbox("Especialidade", options=list(checklists.keys()))

if especialidade:
    # 2. Cirurgia
    cirurgia = st.selectbox("Cirurgia", options=list(checklists[especialidade].keys()))

    if cirurgia:
        # 3. Abordagem
        abordagem = st.selectbox("Abordagem Cirúrgica", options=list(checklists[especialidade][cirurgia].keys()))

        if abordagem:
            # 4. Tipo (Urgência ou Programada)
            tipo = st.radio("Tipo de cirurgia", options=["Programada", "Urgência"])

            # Gera lista final
            itens_base = checklists[especialidade][cirurgia][abordagem][tipo]
            itens_urgencia = checklists[especialidade][cirurgia][abordagem]["Urgência"] if tipo == "Urgência" else []
            itens_total = itens_base + itens_urgencia

            st.subheader(f"Checklist: {especialidade} → {cirurgia} ({abordagem}) – {tipo}")

            itens_em_falta = []
            for item in itens_total:
                verificado = st.checkbox(item, key=item)  # key única para evitar erros
                if not verificado:
                    itens_em_falta.append(item)

            if st.button("🔍 Verificar Checklist", type="primary"):
                if itens_em_falta:
                    st.error("⚠️ **ITENS EM FALTA:**")
                    for item in itens_em_falta:
                        st.write(f"• {item}")
                    st.warning("Confirma estes itens antes de iniciar a cirurgia.")
                else:
                    st.success("✅ **Tudo verificado! Pode prosseguir com segurança.**")
                    st.balloons()

st.markdown("---")
st.caption("Criado por Artur Pinheiro 🚀")
