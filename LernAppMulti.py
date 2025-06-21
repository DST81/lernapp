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
    "Geschichte": "mc/mc_Geschichte.json",
    "BIO": "mc/mc_bio.json",
    "WR": "mc/mc_wr.json",
    "Deep Learning": "mc/mc_questions_with_explanations.json",
    "Deep Learning for pros": "mc/mc_DL_next_level.json",
    "NLP": "mc/mc_NLP.json",
    "UNIX": "mc/mc_unix_for_poets.json",
    "Banken": "mc/mc_bank.json"
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
    ausgewählt = st.radio("Wähle eine Antwort:", frage['options'], key=antwort_key)

    if not ss('antwort_gegeben', False):
        if st.button("Antwort überprüfen"):
            if ausgewählt is None:
                st.warning("Bitte wähle eine Antwort aus.")
                st.stop()

            richtige_antwort = frage['options'][frage['correct_index']]
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
        richtige_antwort = frage['options'][frage['correct_index']]
        gegebene_antwort = st.session_state.get(antwort_key)

        if gegebene_antwort == richtige_antwort:
            st.success("✅ Richtig!")
        else:
            st.error(f"❌ Falsch. Richtig wäre: {richtige_antwort}")
        if 'explanation' in frage:
            st.info(f"ℹ️ Erklärung: {frage['explanation']}")

        if st.button("Nächste Frage anzeigen"):
            akt_frage = ss('aktuelle_frage', None)
            antwort_radio_key = f"antwort_radio-{akt_frage['id']}" if isinstance(akt_frage, dict) else None
            for k in ['aktuelle_frage', 'antwort_gegeben']:
                full_key = f"{key_prefix}{k}"
                if full_key in st.session_state:
                    del st.session_state[full_key]
            if antwort_radio_key:
                full_key = f"{key_prefix}{antwort_radio_key}"
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

nur_falsche = st.sidebar.checkbox("Nur falsch beantwortete wiederholen", value=ss('nur_falsche_wiederholung', False))

if nur_falsche != ss('nur_falsche_wiederholung', False):
    ss_set('nur_falsche_wiederholung', nur_falsche)

    # Hole den passenden Fragenpool
    if nur_falsche:
        verfügbare_fragen_neu = [f for f in alle_fragen if f['id'] in ss('falsch_beantwortete_ids', [])]
    else:
        verfügbare_fragen_neu = [f for f in alle_fragen if f['id'] not in ss('beantwortete_ids', [])]

    if verfügbare_fragen_neu:
        frage_neu = random.choice(verfügbare_fragen_neu)
        ss_set('aktuelle_frage', frage_neu)
        ss_set('antwort_gegeben', False)
        # Antwort-Radio-Key ggf. löschen, damit Radio frisch ist
        antwort_key = f"{key_prefix}antwort_radio-{frage_neu['id']}"
        if antwort_key in st.session_state:
            del st.session_state[antwort_key]
    else:
        ss_set('aktuelle_frage', None)
        ss_set('antwort_gegeben', False)


if st.sidebar.button("🔄 Spiel zurücksetzen"):
    if os.path.exists(SPEICHERDATEI):
        os.remove(SPEICHERDATEI)
    for key in list(st.session_state.keys()):
        if key.startswith(key_prefix):
            del st.session_state[key]
    st.rerun()
