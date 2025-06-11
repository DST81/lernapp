import streamlit as st
import random
import os
import json

def lade_fragen(pfad='mc_unix_for_poets.json'):
    with open (pfad, 'r',encoding='utf-8') as f:
        return json.load(f)
SPEICHERDATEI = 'spielstand.json'

def speicherstand_laden():
    if os.path.exists(SPEICHERDATEI):
        with open(SPEICHERDATEI, 'r') as f:
            return json.load(f)
    return {}

def speicherstand_speichern():
    with open(SPEICHERDATEI, 'w') as f:
        json.dump({
            "beantwortete_ids": list(st.session_state.beantwortete_ids),
            "falsch_beantwortete_ids": list(st.session_state.falsch_beantwortete_ids),
            "score": st.session_state.score,
            "nur_falsche_wiederholung":st.session_state.nur_falsche_wiederholung
        }, f)

#IDs hinzfügen (Index als ID)
alle_fragen =[{**f,'id':i} for i,f in enumerate(lade_fragen())]
st.title('🎓 Single-Choice Lern-App')

daten=speicherstand_laden()
#Session State initialisieren
if 'beantwortete_ids' not in st.session_state:
    st.session_state.beantwortete_ids=set(daten.get('beantwortete_ids',[]))
if 'falsch_beantwortete_ids' not in  st.session_state:
    st.session_state.falsch_beantwortete_ids=set(daten.get('falsch_beantwortete_ids', []))
if "score" not in st.session_state:
    st.session_state.score = daten.get('score',0)
if 'nur_falsche_wiederholung' not in st.session_state:
    st.session_state.nur_falsche_wiederholung = False
if 'frage' not in st.session_state:
    if st.session_state.nur_falsche_wiederholung:
        falsche = [f for f in alle_fragen if f['id'] in st.session_state.falsch_beantwortete_ids]
        if falsche:
            st.session_state.frage = random.choice(falsche)
        else:
            st.success("✅ Du hast alle falsch beantworteten Fragen wiederholt!")
            st.session_state.nur_falsche_wiederholung = False
            st.stop()
    else:
        unbeantwortete = [f for f in alle_fragen if f['id'] not in st.session_state.beantwortete_ids]
        if not unbeantwortete:
            # Wenn alle Fragen beantwortet wurden:
            if not st.session_state.nur_falsche_wiederholung and len(st.session_state.falsch_beantwortete_ids) == 0:
                # ✅ Nur zurücksetzen, wenn wirklich alles richtig beantwortet
                st.success("🎉 Du hast alle Fragen richtig beantwortet! Spielstand wird zurückgesetzt.")
                st.session_state.beantwortete_ids.clear()
                st.session_state.score = 0
                st.session_state.falsch_beantwortete_ids.clear()
                unbeantwortete = alle_fragen
            elif st.session_state.nur_falsche_wiederholung:
                # 🔁 Wiederholung falscher Fragen abgeschlossen
                st.success("✅ Du hast alle falsch beantworteten Fragen wiederholt!")
                st.session_state.nur_falsche_wiederholung = False
                st.stop()
            else:
                st.warning("Du hast alle Fragen beantwortet, aber noch nicht alle richtig.")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔁 Falsche Fragen wiederholen"):
                        falsche = [f for f in alle_fragen if f['id'] in st.session_state.falsch_beantwortete_ids]
                        if falsche:
                            st.session_state.frage = random.choice(falsche)
                            st.session_state.antwort_bestätigt = False
                            st.session_state.auswahl = None
                            st.session_state.nur_falsche_wiederholung = True
                            st.rerun()
                        else:
                            st.warning("Keine falsch beantworteten Fragen mehr übrig.")
                with col2:
                    if st.button("🔄 Spiel komplett zurücksetzen"):
                        st.session_state.beantwortete_ids.clear()
                        st.session_state.falsch_beantwortete_ids.clear()
                        st.session_state.score = 0
                        if os.path.exists(SPEICHERDATEI):
                            os.remove(SPEICHERDATEI)
                        st.session_state.nur_falsche_wiederholung = False
                        st.rerun()
                st.stop()


    st.session_state.frage=random.choice(unbeantwortete)
if 'antwort_bestätigt' not in st.session_state:
    st.session_state.antwort_bestätigt = False
if 'auswahl' not in st.session_state:
    st.session_state.auswahl=None

# Anzeige
frage = st.session_state.frage
st.subheader(f"Frage {frage['id'] + 1}")
st.write(frage["question"])

if not st.session_state.antwort_bestätigt:
    auswahl = st.radio("Antwortmöglichkeiten:", frage["options"], index=None,key="antwort_radio")
    st.session_state.auswahl = auswahl

    if st.button("Antwort bestätigen"):
        richtig = frage["options"][frage["correct_index"]]
        if st.session_state.auswahl == richtig:
            st.success("✅ Richtig!")
            st.session_state.score += 1
            st.session_state.falsch_beantwortete_ids.discard(frage["id"])
        else:
            st.error(f"❌ Falsch! Richtig wäre: {richtig}")
            st.session_state.falsch_beantwortete_ids.add(frage["id"])
        st.info(frage['explanation'])

        st.session_state.beantwortete_ids.add(frage["id"])
        st.session_state.antwort_bestätigt = True
        speicherstand_speichern()
        st.rerun()

else:
    frage = st.session_state.frage
    richtig = frage["options"][frage["correct_index"]]
    auswahl = st.session_state.auswahl

    if auswahl == richtig:
        st.markdown(
            f"""
            <div style='background-color:#d4edda;padding:20px;border-radius:10px;border-left:5px solid #28a745;'>
                <h3 style='color:#155724;'>✅ Richtig beantwortet!</h3>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='background-color:#f8d7da;padding:20px;border-radius:10px;border-left:5px solid #dc3545;'>
                <h3 style='color:#721c24;'>❌ Falsch beantwortet</h3>
                <p>Richtige Antwort: <strong>{richtig}</strong></p>
            </div>
            """, unsafe_allow_html=True
        )

    # Erklärung anzeigen
    st.info(frage["explanation"])

    if st.button("Weiter zur nächsten Frage"):
        
        if st.session_state.nur_falsche_wiederholung:
            unbeantwortete = [f for f in alle_fragen if f['id'] in st.session_state.falsch_beantwortete_ids]
        else:
            unbeantwortete = [f for f in alle_fragen if f['id'] not in st.session_state.beantwortete_ids]

        if not unbeantwortete:
            if not st.session_state.nur_falsche_wiederholung and len(st.session_state.falsch_beantwortete_ids) == 0:
                # ✅ Nur zurücksetzen, wenn wirklich alle richtig beantwortet wurden
                st.success("🎉 Du hast alle Fragen korrekt beantwortet! Spielstand wird zurückgesetzt.")
                st.session_state.beantwortete_ids.clear()
                st.session_state.score = 0
                st.session_state.falsch_beantwortete_ids.clear()
                unbeantwortete = alle_fragen
            elif st.session_state.nur_falsche_wiederholung:
                # 🔁 Wiederholung falscher Fragen abgeschlossen
                st.success("✅ Du hast alle falsch beantworteten Fragen wiederholt!")
                st.session_state.nur_falsche_wiederholung = False
                st.stop()
            else:
                # Noch falsche Fragen vorhanden, aber alles einmal durch
                st.warning("Du hast alle Fragen beantwortet, aber noch nicht alle richtig. Wiederhole die falschen oder setze zurück.")
                st.stop()

        st.session_state.frage = random.choice(unbeantwortete)
        st.session_state.antwort_bestätigt = False
        st.session_state.auswahl = None
        st.rerun()
# --- Abschlussmeldung, wenn alle beantwortet ---
if len(st.session_state.beantwortete_ids) == len(alle_fragen):
    st.markdown("---")
    richtig = st.session_state.score
    gesamt = len(alle_fragen)
    falsch = len(st.session_state.falsch_beantwortete_ids)

    st.markdown(
        f"""
        <div style='background-color:#e0f7fa;padding:20px;border-radius:10px;border-left:5px solid #00acc1;'>
            <h2>🎉 Gratulation!</h2>
            <p>Du hast <strong>{richtig} von {gesamt}</strong> Fragen beantwortet.</p>
        </div>
        """, unsafe_allow_html=True
    )

    if falsch > 0:
        if st.button("🔁 Falsch beantwortete Fragen wiederholen"):
            falsche = [f for f in alle_fragen if f['id'] in st.session_state.falsch_beantwortete_ids]
            st.session_state.frage = random.choice(falsche)
            st.session_state.antwort_bestätigt = False
            st.session_state.auswahl = None
            st.rerun()
    else:
        st.success("✅ Du hast alle Fragen korrekt beantwortet. Super gemacht!")


# Statistik
st.markdown("---")
st.info(f"✅ Richtige Antworten: {st.session_state.score}")
st.info(f"📚 Fragen insgesamt: {len(alle_fragen)}")
st.info(f"🔁 Noch offen: {len([f for f in alle_fragen if f['id'] not in st.session_state.beantwortete_ids])}")
st.info(f"❌ Falsch beantwortete Fragen: {len(st.session_state.falsch_beantwortete_ids)}")

if st.button("Nur falsch beantwortete Fragen wiederholen"):
    falsche = [f for f in alle_fragen if f['id'] in st.session_state.falsch_beantwortete_ids]
    if falsche:
        st.session_state.frage = random.choice(falsche)
        st.session_state.antwort_bestätigt = False
        st.session_state.auswahl = None
        st.session_state.nur_falsche_wiederholung = True
        st.rerun()
    else:
        st.warning("Keine falsch beantworteten Fragen vorhanden.")
if st.button("Spielstand zurücksetzen"):
    st.session_state.beantwortete_ids.clear()
    st.session_state.falsch_beantwortete_ids.clear()
    st.session_state.score = 0
    if os.path.exists(SPEICHERDATEI):
        os.remove(SPEICHERDATEI)
    st.session_state.nur_falsche_wiederholung = False
    st.success("Spielstand zurückgesetzt.")
    st.rerun()

