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
        "question": "Welche Phase ist nicht Teil des CRISP-DM-Prozesses?",
        "options": [
            "Datenaufbereitung",
            "Modellierung",
            "Software-Entwicklung",
            "Evaluierung"
        ],
        "correct_index": 2,
        "explanation": "Der CRISP-DM-Prozess umfasst die Phasen Business Understanding, Datenverständnis, Datenaufbereitung, Modellierung, Evaluierung und Deployment. Software-Entwicklung ist nicht Teil dieses Prozesses."
    },
    {
        "question": "Was ist das Ziel der Phase 'Business Understanding' im CRISP-DM-Modell?",
        "options": [
            "Die Daten für Machine-Learning-Algorithmen vorzubereiten.",
            "Den geschäftlichen Kontext und die Ziele zu verstehen.",
            "Datenmodelle zu evaluieren.",
            "Ein endgültiges Modell bereitzustellen."
        ],
        "correct_index": 1,
        "explanation": "In der Phase 'Business Understanding' wird der geschäftliche Kontext analysiert, um sicherzustellen, dass die Datenanalyse den gewünschten Geschäftszielen entspricht."
    },
    {
        "question": "Welcher Schritt ist Teil eines End-to-End Machine Learning Projekts?",
        "options": [
            "Daten visualisieren, um Erkenntnisse zu gewinnen.",
            "Daten löschen, die nicht benötigt werden.",
            "Ein endgültiges Modell auswählen, ohne es zu testen.",
            "Die Ergebnisse direkt in einem Bericht dokumentieren."
        ],
        "correct_index": 0,
        "explanation": "Datenvisualisierung ist ein zentraler Schritt in Machine-Learning-Projekten, da sie dabei hilft, Muster und Zusammenhänge in den Daten zu erkennen."
    },
    {
        "question": "Was ist der letzte Schritt in einem End-to-End Machine Learning Projekt?",
        "options": [
            "Die Daten vorverarbeiten.",
            "Die Lösung präsentieren.",
            "Das System starten, überwachen und warten.",
            "Modelle vergleichen und bewerten."
        ],
        "correct_index": 2,
        "explanation": "Der letzte Schritt besteht darin, das Modell in Produktion zu bringen, kontinuierlich zu überwachen und bei Bedarf zu aktualisieren, um langfristig zuverlässige Ergebnisse zu liefern."
    },
    {
        "question": "Welche Aussage beschreibt die Datenvorbereitung in einem Machine-Learning-Prozess korrekt?",
        "options": [
            "Daten werden in Kategorien eingeteilt, um Muster zu erkennen.",
            "Daten werden bereinigt und transformiert, um sie für Algorithmen nutzbar zu machen.",
            "Daten werden ausschließlich zur Visualisierung verwendet.",
            "Daten werden direkt für die Modellierung verwendet, ohne Anpassungen vorzunehmen."
        ],
        "correct_index": 1,
        "explanation": "Die Datenvorbereitung umfasst Schritte wie Bereinigung, Transformation und Feature Engineering, um sicherzustellen, dass die Daten für die Modellierung geeignet sind."
    },
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
