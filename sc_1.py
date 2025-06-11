class LernApp:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("Willkommen zur Single-Choice-Lern-App!\n")
        input("Drücke Enter, um zu starten...\n")

        for i, q in enumerate(self.questions):
            print(f"Frage {i + 1}: {q['question']}\n")
            for j, option in enumerate(q['options']):
                print(f"{j + 1}. {option}")
            answer = input("\nBitte gib die Nummer deiner Antwort ein: ")

            # Antwort überprüfen
            if answer.isdigit() and int(answer) - 1 == q['correct_index']:
                print("\n✅ Richtig!")
                self.score += 1
            else:
                print("\n❌ Falsch!")
                print(f'Richtig wäre: {q["correct_index"] + 1}. {q["options"][q["correct_index"]]}')
            print(f"Erklärung: {q['explanation']}\n")
            input("Drücke Enter, um zur nächsten Frage zu gelangen...")

        print(f"\nErgebnis: {self.score}/{len(self.questions)} korrekt beantwortet!")
        print("Vielen Dank fürs Mitmachen!\n")


fragen = [
    {
        "question": "Was ist die Hauptcharakteristik des überwachten Lernens?",
        "options": [
            "Es benötigt keine Labels für die Trainingsdaten.",
            "Es nutzt eine Zielvariable, um ein Modell zu trainieren.",
            "Es basiert ausschließlich auf der Interaktion mit einer Umgebung.",
            "Es verwendet Clustering-Methoden zur Datenanalyse."
        ],
        "correct_index": 1,
        "explanation": "Überwachtes Lernen erfordert eine Zielvariable (Label), um ein Modell zu trainieren, das Vorhersagen oder Klassifikationen basierend auf den Eingaben treffen kann."
    },
    {
        "question": "Welche der folgenden Aufgaben wird typischerweise im unüberwachten Lernen durchgeführt?",
        "options": ["Klassifikation", "Regression", "Clustering", "Reinforcement"],
        "correct_index": 2,
        "explanation": "Unüberwachtes Lernen dient der Analyse von Daten ohne Zielvariablen. Eine typische Aufgabe ist das Clustering, bei dem Daten in Gruppen mit ähnlichen Eigenschaften unterteilt werden."
    },
    {
        "question": "Welche Aussage trifft auf halbüberwachtes Lernen zu?",
        "options": [
            "Es benötigt für jede Beobachtung eine Zielvariable.",
            "Es verwendet eine Kombination aus Beobachtungen mit und ohne Zielvariable.",
            "Es basiert ausschließlich auf unstrukturierten Daten.",
            "Es verwendet keine Zielvariablen."
        ],
        "correct_index": 1,
        "explanation": "Halbüberwachtes Lernen kombiniert Daten mit und ohne Zielvariablen, was besonders nützlich ist, wenn nur ein kleiner Teil der Daten gelabelt ist."
    },
    {
        "question": "Was ist das Ziel des Reinforcement Learnings?",
        "options": [
            "Das Finden verborgener Strukturen in Daten.",
            "Das Minimieren von Underfitting durch Datenaugmentation.",
            "Das Maximieren einer kumulativen Belohnung durch Interaktion mit der Umgebung.",
            "Das Erstellen eines Modells auf Basis einer Zielvariable."
        ],
        "correct_index": 2,
        "explanation": "Reinforcement Learning zielt darauf ab, durch Interaktion mit einer Umgebung eine Strategie zu entwickeln, die langfristige Belohnungen maximiert."
    },
    {
        "question": "Wann ist Online Learning besonders nützlich?",
        "options": [
            "Bei sehr großen Datensätzen, die nicht vollständig auf einmal verarbeitet werden können.",
            "Wenn alle Beobachtungen eine Zielvariable enthalten.",
            "Wenn das Modell nicht kontinuierlich aktualisiert werden soll.",
            "Wenn ein statisches Modell bevorzugt wird."
        ],
        "correct_index": 0,
        "explanation": "Online Learning ist nützlich, wenn Daten kontinuierlich eintreffen oder die Verarbeitung eines kompletten Datensatzes auf einmal nicht möglich ist."
    },
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
