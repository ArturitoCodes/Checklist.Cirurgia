import streamlit as st

# Estrutura: Especialidade → Cirurgia → Abordagem (só itens normais + posicionamento condicional)
checklists = {
    "Obstetrícia/Ginecologia": {
        "Cesariana": {
            "Aberta": {
                "itens": [
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
                "posicionamento": "🧍‍♀️ **Posicionamento do doente:** Decúbito dorsal, braços abertos, pernas em litotomia se necessário."
            }
        }
    },
    "Cirurgia Geral": {
        "Hérnia Hiato": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Cabo fonte de luz",
                    "Cabo CO2",
                    "Porta agulhas LPC",
                    "Punhos de foco",
                    "Separador fígado Nathason (só a parte da mesa cirúrgica; escolhem tamanho depois)",
                    "Cabo ultracisión",
                    "**CONSUMÍVEIS:**",
                    "Trocar 5 (x2)",
                    "Trocar 11 (x2)",
                    "Lâmina 11",
                    "Cobertura de tubo",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Ropi 7,5mg",
                    "Pensos impermeável",
                    "Compressas médias e pequenas",
                    "Nastro (cortar pela metade; dar numa grasper ou clinch)",
                    "Aspirador LPC (SOS)",
                    "Termo",
                    "Ultracisión 36",
                    "Venda crepe",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0",
                    "Premicron con plegets",
                    "Premiparch (plegets soltos)",
                    "Seda 2/0 (cortar tamanho do papel para secar paciente)",
                    "V-loc 3/0 (vermelho)"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Decúbito dorsal, pernas abertas como na colecistectomia, fixadas com venda crepe.\n🏥 Torre do lado direito do doente, quase na cabeça."
            }
        },
        "By-pass Gástrico": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Cabo fonte de luz",
                    "Cabo CO2",
                    "Porta agulhas LPC",
                    "Termo",
                    "Punhos de foco",
                    "Separador fígado Nathason (só a parte da mesa cirúrgica)",
                    "Cabo ultracision",
                    "**CONSUMÍVEIS:**",
                    "Trocar 5 (x2) (SOS)",
                    "Trocar 11 (x2)",
                    "Trocar 12 (x2)",
                    "Lâmina 11",
                    "Cobertura de tubo",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Ropi 7,5mg",
                    "Pensos impermeável",
                    "Compressas médias e pequenas",
                    "Aspirador LPC (SOS)",
                    "Echelon 60",
                    "Cargas verdes (x5) 60+",
                    "Venda crepe (para pernas)",
                    "Meias compressivas",
                    "SV",
                    "Ultracision 36",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0",
                    "V-loc 3/0 (vermelho) (3 ou 4)",
                    "Prolene 1 (agulha recta; se não houver, redonda e põe recta)"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Pernas abertas como na colecistectomia.\n🏥 Torre do lado direito do doente, quase na cabeça."
            }
        },
        "Hérnia Inguinal": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Cabo fonte de luz",
                    "Cabo CO2",
                    "Pinça sem dente comprida",
                    "Punhos de foco",
                    "**CONSUMÍVEIS:**",
                    "Trocar 5",
                    "Trocar hasson",
                    "Balão distensão extra peritoneal",
                    "Lâmina 11",
                    "Cobertura de tubo",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Ropi 7,5mg",
                    "Pensos impermeável",
                    "Compressas médias e pequenas",
                    "Afastador Sean miller (SOS)",
                    "Prótese optilene mesh 15x15",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Torre nos pés do doente; pernas fechadas; pedal no lado esquerdo.\n*Rede: enrolar num canudinho com kelly na ponta; dar na grasper*"
            }
        },
        "Hérnia Incisional/Umbilical": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Cabo fonte de luz",
                    "Cabo CO2",
                    "Porta agulhas LPC",
                    "Punhos de foco",
                    "**CONSUMÍVEIS:**",
                    "Trocar 5 (x2)",
                    "Trocar 12",
                    "Lâmina 11",
                    "Cobertura de tubo",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Ropi 7,5mg",
                    "Pensos impermeável",
                    "Compressas médias e pequenas",
                    "Prótese ventralight (com seringa)",
                    "Endoclose (passa fios)",
                    "Optifix",
                    "Aspirador LPC (SOS)",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0",
                    "Monosof 1 (fio duplo, verde por fora)"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Torre lateral no lado esquerdo do doente."
            }
        },
        "Fistulectomia": {
            "Aberta": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Estilete",
                    "**CONSUMÍVEIS:**",
                    "Cureta 7",
                    "Biotomo 4",
                    "Campo com óculo",
                    "Compressas",
                    "Gaze gorda (em triângulo)",
                    "Bisturi elétrico"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Posição litotomia ou prona conforme acesso."
            }
        },
        "Colecistectomia": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Cabo fonte de luz",
                    "Cabo CO2",
                    "Afastador Sean miller",
                    "Pinça Hemolock roxa",
                    "**CONSUMÍVEIS:**",
                    "Trouxa laparoscopia",
                    "Lâmina 11",
                    "Trocar 5 (2)",
                    "Trocar 11 (2)",
                    "Clips Hemolock roxos",
                    "Compressas médias e pequenas",
                    "Pensos impermeáveis",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Ropi 7,5mg",
                    "Cobertura tubo",
                    "Contentor para anatomia",
                    "Saco de recolha",
                    "Aspirador elephant",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0",
                    "*Monopolar: 35/35; CO2: 12-40*",
                    "*No final: batufo (compressa cortada em 2 com betadine pomada + compressa dobrada em 4 por cima)*"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Pernas abertas com crepe, braços abertos.\n🏥 Torre no lado direito do doente; pedal no meio das pernas do paciente."
            }
        },
        "Apendicectomia": {
            "Laparoscópica": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Cx laparoscopia",
                    "Lente 30",
                    "Punhos foco",
                    "Pinça Hemolock XL",
                    "Sean miller",
                    "**CONSUMÍVEIS:**",
                    "Compressas médias e pequenas",
                    "Trouxa laparoscopia",
                    "Clips Hemolock XL",
                    "Trocar 5",
                    "Trocar 11",
                    "Ropi 7,5",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Pensos impermeáveis",
                    "Batufo com Betadine pomada",
                    "Elephant (SOS)",
                    "Saco recolha",
                    "Contentor anatomia",
                    "**FIOS:**",
                    "Vicryl 2/0 (5/8)",
                    "Ethilon 3/0"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Torre no lado direito do abdómen; algaliar (retirar no final); braço direito aberto, esquerdo ao longo do corpo; pernas fechadas."
            }
        },
        "Hemorroidectomia": {
            "Aberta": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Punhos foco",
                    "**CONSUMÍVEIS:**",
                    "Mesa mayo",
                    "Campo com óculo",
                    "Compressas médias",
                    "Lidocaina 2% + Ropi 7,5mg",
                    "Seringa 20",
                    "Agulha IM",
                    "Bisturi elétrico (35/35)",
                    "Gaze gorda",
                    "Betadine pomada",
                    "Máquina hemorroidas (SOS)",
                    "Tiras adesivo",
                    "Desinfeção com iodopovidona"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Posição litotomia ou jackknife."
            }
        },
        "Esfincterotomia e/ou Fissurectomia": {
            "Aberta": {
                "itens": [
                    "**FERROS:**",
                    "Cx operação",
                    "Punhos de foco",
                    "Estilete anuscopio metálico",
                    "**CONSUMÍVEIS:**",
                    "Mesa mayo",
                    "Campo com óculo grande",
                    "Iodopovidona",
                    "Instilagel",
                    "Betadine pomada",
                    "Ropi 7,5mg + lidocaina 2%",
                    "Seringa 20ml",
                    "Agulha IM",
                    "Compressas médias",
                    "Gaze gorda",
                    "Bisturi elétrico",
                    "Adesivo castanho"
                ],
                "posicionamento": "🧍‍♂️ **Posicionamento:** Posição litotomia."
            }
        }
    }
}

st.set_page_config(page_title="Checklist Bloco Operatório", page_icon="🏥")

st.title("🏥 Checklist de Materiais - Bloco Operatório")
st.markdown("**Seleciona a especialidade, cirurgia e abordagem para ver a checklist e posicionamento**")

especialidade = st.selectbox("Especialidade", options=list(checklists.keys()))

if especialidade:
    cirurgia = st.selectbox("Cirurgia", options=list(checklists[especialidade].keys()))

    if cirurgia:
        abordagem = st.selectbox("Abordagem Cirúrgica", options=list(checklists[especialidade][cirurgia].keys()))

        if abordagem:
            itens = checklists[especialidade][cirurgia][abordagem]["itens"]
            posicionamento = checklists[especialidade][cirurgia][abordagem]["posicionamento"]

            # Posicionamento condicional: só mostra torre se Laparoscópica ou Artroscópica
            if "Laparoscópica" in abordagem or "Artroscópica" in abordagem or "Endoscópica" in abordagem:
                st.markdown("---")
                st.markdown("### 🧍 Posicionamento do Doente e Torre")
                st.markdown(posicionamento)
                st.markdown("---")

            # Checklist de materiais
            st.subheader(f"Checklist de Materiais: {especialidade} → {cirurgia} ({abordagem})")

            itens_em_falta = []
            for item in itens:
                if item.startswith("**") or item.startswith("*"):
                    st.markdown(item)
                else:
                    verificado = st.checkbox(item, key=item)
                    if not verificado:
                        itens_em_falta.append(item)

            if st.button("🔍 Verificar Checklist", type="primary"):
                if itens_em_falta:
                    st.error("⚠️ **ITENS EM FALTA:**")
                    for item in itens_em_falta:
                        st.write(f"• {item}")
                    st.warning("Por favor, confirma estes itens antes de iniciar a cirurgia.")
                else:
                    st.success("✅ **Tudo verificado! Pode prosseguir com segurança.**")
                    st.balloons()

st.markdown("---")
st.caption("Criado por BO Braga Sul")

# 5 linhas abaixo, apenas AP (centralizado e discreto)
st.markdown("<br>" * 5, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; font-size: 14px;'>AP</p>", unsafe_allow_html=True)
