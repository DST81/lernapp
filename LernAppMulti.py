import streamlit as st
import json
import os
import random

# -------------------- Einstellungen --------------------
st.set_page_config(page_title="LernApp", page_icon="📘", layout="centered")
st.title("📘 Interaktive LernApp")

# -------------------- Fachauswahl --------------------
st.sidebar.image("helfer.png", caption="Hallo, ich bin dein Lernassistent", use_container_width=True)
st.sidebar.title("📚 Fachauswahl")
   
verfügbare_fächer = {
    #"Medizin for Profis":"Medizin_forProfis.json",
    "Medizin Tag 1": "Medizin_Tag1.json",
    "Medizin Tag 2": "Medizin_Tag2.json",
    "Medizin Tag 3": "Medizin_Tag3.json",
    "Medizin Tag 4": "Medizin_Tag4.json",
    "Medizin Tag 5": "Medizin_Tag5.json",
    "Medizin Schwierige Fragen":         "Medizin_AlleTage_schwierigereFragen.json",
    "Med w T1 Einfuehrung":              "medizin_more/med_w_T1_Einfuehrung.json",
    "Med w T1 KI in Medizin":            "medizin_more/med_w_T1_KI_in_Medizin.json",
    "Med w T2 Patientenpfad Einsatz KI": "medizin_more/med_w_T2_Einsatz_KI_Ppfad.json",
    "Med w T2 Patientenpfad":            "medizin_more/med_w_T2_Patientenpfad.json",
    "Med w T3 Architektur, Datenschutz": "medizin_more/med_w_T3_Architektur_Datenschutz.json",
    "Med T3 Prinzipien":                 "medizin_more/med_T3_Prinzipien.json",
    "Med T4 Bildgebende Verfahren":      "medizin_more/med_T4_Bildgebende_Verfahren.json",
    "Med T4 Personalisierte Medizin":    "medizin_more/med_T4_personalisierte_Medizin.json",    
    "Med T5 Interoperabilität":          "medizin_more/med_T5_Interoperabilität.json",  
    "Med m T1 Einfuehrung":              "medizin_more/Med_m_T1_Einfuehrung.json",
    "Med m T1 KI in Medizin":            "medizin_more/med_m_T1_KI_in_Medizin.json",
    "Med m T3 Architektur, Datenschutz": "medizin_more/med_m_T3_Architektur_Datenschutz.json", 
    "Med g T1 Einfuehrung":              "medizin_more/Med_g_T1_Einfuehrung.json",
    "Med g T1 KI in Medizin":            "medizin_more/med_g_T1_KI_in_Medizin.json",
    "Med g T3 Architektur, Datenschutz": "medizin_more/med_g_T3_Architektur_Datenschutz.json", 
    #"Biologie Block 1":"Biologie_Block1.json",
    #"Biologie Block 2":"Biologie_Block2.json",
    #"Biologie Block 3":"Biologie_Block3.json",
    #"Einführung Banken": "mc_bank_Kapitel1.json",
    #"Doppelte Buchführung": "mc_bank_Kapitel2.json",
    #"Modellierung von Banken":"mc_bank_Kapitel3.json",
    #"Hashes, Keys und Signaturen": "mc_bank_Kapitel4.json",
    #"Transaktionen und Architektur": "mc_bank_Kapitel5.json",
    #"Zins, Diskontierung": "mc_bank_Kapitel6.json",
    #"Bankprodukte": "mc_bank_Kapitel7.json",
    #"Simulationen und Risikomessung": "mc_bank_Kapitel10.json",
    #"Deep Learning": "mc_questions_with_explanations.json",
    #"Deep Learning for pros": "mc_DL_next_level.json",
    #"NLP": "mc_NLP.json",
    #"UNIX": "mc_unix_for_poets.json",
    #"Banken": "mc_bank.json"
}

ausgewähltes_fach = st.sidebar.selectbox("Wähle ein Fach:", list(verfügbare_fächer.keys()))

# -------------------- Session State pro Fach --------------------
if "aktuelles_fach" not in st.session_state:
    st.session_state.aktuelles_fach = ausgewähltes_fach
elif st.session_state.aktuelles_fach != ausgewähltes_fach:
    for key in list(st.session_state.keys()):
        if key.startswith(f"{st.session_state.aktuelles_fach}_"):
            del st.session_state[key]
    st.session_state.aktuelles_fach = ausgewähltes_fach
    st.rerun()

key_prefix = f"{ausgewähltes_fach}_"

def ss(key, default):
    return st.session_state.setdefault(key_prefix + key, default)

def ss_set(key, value):
    st.session_state[key_prefix + key] = value

# -------------------- Fragen und Speicherstand --------------------
FRAGEN_DATEI = verfügbare_fächer[ausgewähltes_fach]
SPEICHERDATEI = f"spielstand_{ausgewähltes_fach}.json"

def lade_fragen(pfad):
    with open(pfad, 'r', encoding='utf-8') as f:
        return json.load(f)

alle_fragen = [{**f, 'id': i} for i, f in enumerate(lade_fragen(FRAGEN_DATEI))]

def speicherstand_laden(datei):
    if os.path.exists(datei):
        with open(datei, 'r') as f:
            daten = json.load(f)
            ss_set('beantwortete_ids', daten.get('beantwortete_ids', []))
            ss_set('falsch_beantwortete_ids', daten.get('falsch_beantwortete_ids', []))
            ss_set('score', daten.get('score', 0))
            ss_set('nur_falsche_wiederholung', daten.get('nur_falsche_wiederholung', False))
    else:
        ss_set('beantwortete_ids', [])
        ss_set('falsch_beantwortete_ids', [])
        ss_set('score', 0)
        ss_set('nur_falsche_wiederholung', False)

speicherstand_laden(SPEICHERDATEI)

# -------------------- Frageauswahl --------------------
if ss('nur_falsche_wiederholung', False):
    verfügbare_fragen = [f for f in alle_fragen if f['id'] in ss('falsch_beantwortete_ids', [])]
else:
    verfügbare_fragen = [f for f in alle_fragen if f['id'] not in ss('beantwortete_ids', [])]

if ss('antwort_gegeben', None) is None:
    ss_set('antwort_gegeben', False)

frage = ss('aktuelle_frage', None)
if frage is None or frage['id'] not in [f['id'] for f in verfügbare_fragen]:
    if verfügbare_fragen:
        frage = random.choice(verfügbare_fragen)
        ss_set('aktuelle_frage', frage)
        ss_set('antwort_gegeben', False)
        ss_set(f'antwort_radio-{frage["id"]}', None)
    else:
        frage = None

# -------------------- Frage anzeigen --------------------
if frage:
    st.subheader(frage['question'])
    antwort_key = f"{key_prefix}antwort_radio-{frage['id']}"

    # Shuffle einmalig speichern
    if f"{key_prefix}shuffled_options_{frage['id']}" not in st.session_state:
        options = frage['options'][:]
        random.shuffle(options)
        st.session_state[f"{key_prefix}shuffled_options_{frage['id']}"] = options
    else:
        options = st.session_state[f"{key_prefix}shuffled_options_{frage['id']}"]

    # Korrekte Antwort merken
    richtige_antwort = frage['options'][frage['correct_index']]

    ausgewählt = st.radio("Wähle eine Antwort:", options, key=antwort_key)

    if not ss('antwort_gegeben', False):
        if st.button("Antwort überprüfen"):
            if ausgewählt is None:
                st.warning("Bitte wähle eine Antwort aus.")
                st.stop()

            gegebene_antwort = ausgewählt
            if gegebene_antwort == richtige_antwort:
                ss_set('score', ss('score', 0) + 1)
            else:
                falsch_ids = ss('falsch_beantwortete_ids', [])
                if frage['id'] not in falsch_ids:
                    falsch_ids.append(frage['id'])
                    ss_set('falsch_beantwortete_ids', falsch_ids)

            beantwortet_ids = ss('beantwortete_ids', [])
            if frage['id'] not in beantwortet_ids:
                beantwortet_ids.append(frage['id'])
                ss_set('beantwortete_ids', beantwortet_ids)

            with open(SPEICHERDATEI, 'w') as f:
                json.dump({
                    "beantwortete_ids": ss('beantwortete_ids', []),
                    "falsch_beantwortete_ids": ss('falsch_beantwortete_ids', []),
                    "score": ss('score', 0),
                    "nur_falsche_wiederholung": ss('nur_falsche_wiederholung', False)
                }, f)
            ss_set('antwort_gegeben', True)

    # Antwort wurde bereits gegeben – Rückmeldung anzeigen
    if ss('antwort_gegeben', False):
        gegebene_antwort = st.session_state.get(antwort_key)

        if gegebene_antwort == richtige_antwort:
            st.success("✅ Richtig!")
        else:
            st.error(f"❌ Falsch. Richtig wäre: {richtige_antwort}")
        if 'explanation' in frage:
            st.info(f"ℹ️ Erklärung: {frage['explanation']}")

        if st.button("Nächste Frage anzeigen"):
            # Alte Keys löschen
            for k in ['aktuelle_frage', 'antwort_gegeben', f"shuffled_options_{frage['id']}"]:
                full_key = f"{key_prefix}{k}"
                if full_key in st.session_state:
                    del st.session_state[full_key]
            st.rerun()

else:
    st.info("🎉 Alle Fragen in diesem Fach sind beantwortet!")

    if ss('falsch_beantwortete_ids', []):
        if st.button('🔁 Falsch beantwortete Fragen wiederholen'):
            ss_set('nur_falsche_wiederholung', True)
            for k in ['aktuelle_frage', 'antwort_gegeben']:
                full_key = f"{key_prefix}{k}"
                if full_key in st.session_state:
                    del st.session_state[full_key]
            st.rerun()
    else:
        st.write("Alle Fragen wurden korrekt beantwortet!")

# -------------------- Statistik & Optionen --------------------
st.sidebar.markdown("---")
st.sidebar.metric("Punktzahl", ss('score', 0))
st.sidebar.metric("Beantwortet", len(ss('beantwortete_ids', [])))
st.sidebar.metric("Noch offen", len(alle_fragen) - len(ss('beantwortete_ids', [])))

# Button zum Anzeigen der falsch beantworteten Fragen
if st.sidebar.button("Falsch beantwortete Fragen anzeigen"):
    falsch_ids = ss('falsch_beantwortete_ids', [])
    falsch_fragen = [f for f in alle_fragen if f['id'] in falsch_ids]

    if falsch_fragen:
        st.sidebar.write("Falsch beantwortete Fragen:")
        for frage in falsch_fragen:
            st.markdown(f"**{frage['question']}**")
            st.write(f"- {frage['options'][frage['correct_index']]}")
            if 'explanation' in frage:
                st.markdown(f"**Erklärung:** {frage['explanation']}")

    else:
        st.sidebar.write("Keine falsch beantworteten Fragen.")



if st.sidebar.button("🔄 Spiel zurücksetzen"):
    if os.path.exists(SPEICHERDATEI):
        os.remove(SPEICHERDATEI)
    for key in list(st.session_state.keys()):
        if key.startswith(key_prefix):
            del st.session_state[key]
    st.rerun()
