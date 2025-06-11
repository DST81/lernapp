class LernApp:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("Willkommen zur Single-Choice-Lern-App!\n")
        input("Drücke Enter, um zu starten...\n")

        for i, q in enumerate(self.questions):
            print(f"Frage {i + 1}: {q['question']}\n")
            print(f"Frage {i + 1} (von {len(self.questions)}): {q['question']}\n")
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
        "question": "Was ist der Hauptunterschied zwischen Regression und Klassifikation?",
        "options": [
            "Die Zielvariable bei der Regression ist kategorial, während sie bei der Klassifikation kontinuierlich ist.",
            "Bei der Regression werden Verlustfunktionen wie Gini oder Entropie verwendet, während bei der Klassifikation MSE bevorzugt wird.",
            "Die Zielvariable bei der Klassifikation ist kategorial, während sie bei der Regression kontinuierlich ist.",
            "Es gibt keinen Unterschied; beide verwenden dieselben Methoden."
        ],
        "correct_index": 2,
        "explanation": "Klassifikation arbeitet mit kategorialen Zielvariablen, während Regression kontinuierliche Zielvariablen vorhersagt."
    },
    {
        "question": "Welches Kriterium wird häufig verwendet, um einen Split in einem Entscheidungsbaum zu bewerten?",
        "options": [
            "Mean Squared Error (MSE)",
            "Gini-Index",
            "R-Squared",
            "Pearson-Korrelation"
        ],
        "correct_index": 1,
        "explanation": "Der Gini-Index misst die Unreinheit eines Knotens und wird häufig für Splits in Entscheidungsbäumen verwendet."
    },
    {
        "question": "Was misst der Gini-Index in einem Entscheidungsbaum?",
        "options": [
            "Die Stärke der linearen Beziehung zwischen Variablen.",
            "Die Unreinheit oder Diversität eines Knotens.",
            "Die Anzahl der Klassen in einem Datensatz.",
            "Die Wahrscheinlichkeit einer perfekten Klassifikation."
        ],
        "correct_index": 1,
        "explanation": "Der Gini-Index bewertet die Unreinheit eines Knotens, indem er die Wahrscheinlichkeit misst, dass ein Punkt falsch klassifiziert wird."
    },
    {
        "question": "Welche Aussage über Entropie ist korrekt?",
        "options": [
            "Entropie ist rechnerisch effizienter als der Gini-Index.",
            "Entropie misst die Varianz in kontinuierlichen Daten.",
            "Entropie misst die Unsicherheit oder den Grad der Unordnung in einem Knoten.",
            "Entropie wird ausschließlich in Random Forests verwendet."
        ],
        "correct_index": 2,
        "explanation": "Entropie misst den Grad der Unsicherheit in einem Knoten und wird oft zur Bewertung von Splits verwendet."
    },
    {
        "question": "Wie wird die finale Klasse in einem Random Forest vorhergesagt?",
        "options": [
            "Durch Minimierung der Entropie.",
            "Durch Mehrheitsentscheidung basierend auf den Endknoten aller Bäume.",
            "Durch Durchschnitt der vorhergesagten Werte.",
            "Durch die Verwendung eines einzelnen Entscheidungsbaums mit der höchsten Genauigkeit."
        ],
        "correct_index": 1,
        "explanation": "Random Forests verwenden die Mehrheitsentscheidung (Voting) über alle Bäume, um die finale Klasse vorherzusagen."
    },
    {
        "question": "Was ist der Hauptzweck von Gradient Boosting?",
        "options": [
            "Einen einzigen Baum mit minimaler Tiefe zu erstellen.",
            "Mehrere Bäume gleichzeitig zu trainieren, um eine höhere Genauigkeit zu erreichen.",
            "Schwache Lernalgorithmen schrittweise zu verbessern, um die Klassifikationsverluste zu minimieren.",
            "Die Gewichte aller Datenpunkte konstant zu halten."
        ],
        "correct_index": 2,
        "explanation": "Gradient Boosting verbessert schwache Modelle iterativ, um die Verluste zu minimieren."
    },
    {
        "question": "Welcher der folgenden Verluste wird häufig in Gradient Boosting bei Klassifikationsproblemen verwendet?",
        "options": [
            "Mean Squared Error (MSE)",
            "Exponential Loss",
            "Gini-Index",
            "Mean Absolute Error (MAE)"
        ],
        "correct_index": 1,
        "explanation": "Exponential Loss wird häufig in Klassifikationsproblemen verwendet, um falsch klassifizierte Punkte stärker zu gewichten."
    },
    {
        "question": "Welche der folgenden Aussagen beschreibt Log Loss korrekt?",
        "options": [
            "Log Loss misst die Unsicherheit in kontinuierlichen Variablen.",
            "Log Loss bestraft falsche Vorhersagen logarithmisch basierend auf den vorhergesagten Wahrscheinlichkeiten.",
            "Log Loss ist empfindlicher gegenüber Ausreißern als Exponential Loss.",
            "Log Loss wird nur in Entscheidungsbäumen verwendet."
        ],
        "correct_index": 1,
        "explanation": "Log Loss misst den Fehler basierend auf der Entfernung der vorhergesagten Wahrscheinlichkeit von der tatsächlichen Klasse."
    },
    {
        "question": "Wann ist der Gini-Index gegenüber Entropie zu bevorzugen?",
        "options": [
            "Wenn theoretische Fundierung wichtiger ist als Rechenzeit.",
            "Wenn eine höhere Rechenleistung zur Verfügung steht.",
            "Wenn einfache Berechnungen und Geschwindigkeit erforderlich sind.",
            "Wenn die Zielvariable kontinuierlich ist."
        ],
        "correct_index": 2,
        "explanation": "Der Gini-Index ist rechnerisch effizienter als Entropie und daher bei begrenzter Rechenzeit bevorzugt."
    },
    {
        "question": "Welcher Unterschied zwischen Exponential Loss und Log Loss ist korrekt?",
        "options": [
            "Exponential Loss bestraft Fehler logarithmisch, während Log Loss exponentiell bestraft.",
            "Exponential Loss ist robuster gegenüber Ausreißern als Log Loss.",
            "Exponential Loss fokussiert stärker auf falsch klassifizierte Punkte als Log Loss.",
            "Es gibt keinen Unterschied; beide Loss-Funktionen sind identisch."
        ],
        "correct_index": 2,
        "explanation": "Exponential Loss gewichtet falsch klassifizierte Punkte stärker und ist daher bei Boosting-Algorithmen beliebt."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
