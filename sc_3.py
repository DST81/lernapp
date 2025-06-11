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
        "question": "Welche der folgenden Variablentypen kann als numerische und kategorische Variable zugleich verstanden werden?",
        "options": [
            "Diskrete Variablen",
            "Kontinuierliche Variablen",
            "Ordinale Variablen",
            "Kategoriale Variablen"
        ],
        "correct_index": 2,
        "explanation": "Ordinale Variablen haben eine Rangfolge."
    },
    {
        "question": "Was beschreibt die Kardinalität einer kategorialen Variablen?",
        "options": [
            "Die Reihenfolge der Kategorien.",
            "Die Anzahl der Kategorien.",
            "Die Anzahl der Beobachtungen in jeder Kategorie.",
            "Die Summe aller Kategorienwerte."
        ],
        "correct_index": 1,
        "explanation": "Kardinalität bezieht sich auf die Anzahl unterschiedlicher Werte (Kategorien), die eine kategoriale Variable annehmen kann."
    },
    {
        "question": "Was sind seltene Labels?",
        "options": [
            "Labels, die eine hohe Wahrscheinlichkeit haben, in den Trainingsdaten vorzukommen.",
            "Kategorien, die in einer Variablen nur selten auftreten.",
            "Labels, die eine feste Reihenfolge haben.",
            "Labels mit sehr hoher Kardinalität."
        ],
        "correct_index": 1,
        "explanation": "Seltene Labels treten nur in wenigen Beobachtungen auf und können zu Problemen wie schlechter Generalisierung des Modells führen."
    },
    {
        "question": "Wie definiert Hawkins (1980) einen Ausreißer?",
        "options": [
            "Eine Beobachtung, die innerhalb der erwarteten Werte liegt.",
            "Eine Beobachtung, die aufgrund ihrer Reihenfolge auffällt.",
            "Eine Beobachtung, die stark von anderen abweicht und auf ein anderes Erzeugungsprinzip hinweist.",
            "Eine Beobachtung, die keine numerischen Werte enthält."
        ],
        "correct_index": 2,
        "explanation": "Ausreißer sind ungewöhnliche Datenpunkte, die sich stark von der Mehrheit unterscheiden und oft auf ein anderes Erzeugungsprinzip hinweisen."
    },
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
