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
        "question": "Welche der folgenden Aussagen trifft auf die logistische Regression zu?",
        "options": [
            "Sie wird zur Vorhersage kontinuierlicher Variablen verwendet.",
            "Sie gibt die Wahrscheinlichkeit einer Klasse zurück.",
            "Sie verwendet einen linearen Aktivierungsfunktionsansatz.",
            "Sie ist eine nicht-parametrische Methode."
        ],
        "correct_index": 1,
        "explanation": "Die logistische Regression wird für Klassifikationsprobleme verwendet und gibt Wahrscheinlichkeiten für die Zugehörigkeit zu einer Klasse zurück."
    },
    {
        "question": "Welche der folgenden Annahmen trifft bei der logistischen Regression zu?",
        "options": [
            "Die unabhängigen Variablen sind linear unabhängig.",
            "Die Zielvariable ist kontinuierlich.",
            "Die Beziehung zwischen unabhängigen Variablen und der Logit-Transformation ist linear.",
            "Es wird keine Annahme über die Verteilung der Fehler gemacht."
        ],
        "correct_index": 2,
        "explanation": "Die logistische Regression nimmt an, dass die Beziehung zwischen den unabhängigen Variablen und der Logit-Transformation linear ist."
    },
    {
        "question": "Wie wird die Entscheidungsgrenze bei der logistischen Regression normalerweise definiert?",
        "options": [
            "0.5",
            "0.0",
            "-1",
            "Es hängt vom Modelltyp ab."
        ],
        "correct_index": 0,
        "explanation": "Die Standard-Entscheidungsgrenze für die Klassifikation in der logistischen Regression ist 0.5."
    },
    {
        "question": "Welche der folgenden Methoden wird verwendet, um die Parameter der logistischen Regression zu schätzen?",
        "options": [
            "Ordinary Least Squares (OLS)",
            "Maximum-Likelihood-Schätzung (MLE)",
            "Hauptkomponentenanalyse (PCA)",
            "Lagrange-Multiplikatoren"
        ],
        "correct_index": 1,
        "explanation": "Die Maximum-Likelihood-Schätzung maximiert die Wahrscheinlichkeit, dass das Modell die beobachteten Daten beschreibt."
    },
    {
        "question": "Welche Metrik ist besonders nützlich bei einem unausgeglichenen Datensatz?",
        "options": [
            "Accuracy",
            "Precision",
            "F1-Score",
            "Mean Absolute Error"
        ],
        "correct_index": 2,
        "explanation": "Der F1-Score berücksichtigt sowohl Precision als auch Recall und ist besonders nützlich bei unausgeglichenen Datensätzen."
    },
    {
        "question": "Was zeigt die Fläche unter der ROC-Kurve (AUC) an?",
        "options": [
            "Die Genauigkeit des Modells.",
            "Die Wahrscheinlichkeit, dass das Modell einen zufälligen positiven Wert korrekt klassifiziert.",
            "Die Varianz des Modells.",
            "Die durchschnittliche Vorhersagewahrscheinlichkeit."
        ],
        "correct_index": 1,
        "explanation": "Die AUC misst die Fähigkeit eines Modells, zwischen positiven und negativen Klassen zu unterscheiden."
    },
    {
        "question": "Was bedeutet ein hoher Wert im F1-Score?",
        "options": [
            "Hohe Sensitivität und niedrige Spezifität.",
            "Ein Gleichgewicht zwischen Präzision und Sensitivität.",
            "Eine hohe Vorhersagegenauigkeit.",
            "Niedrige Falsch-Positiv-Rate."
        ],
        "correct_index": 1,
        "explanation": "Ein hoher F1-Score zeigt ein gutes Gleichgewicht zwischen Precision und Recall an."
    },
    {
        "question": "Welche Aussage über die Konfusionsmatrix trifft zu?",
        "options": [
            "Sie wird nur für lineare Regressionen verwendet.",
            "Sie zeigt die wahre positive und wahre negative Rate eines Modells.",
            "Sie gibt den Anteil der Fehler in einem Modell an.",
            "Sie gibt die Bedeutung jeder Variable im Modell an."
        ],
        "correct_index": 1,
        "explanation": "Die Konfusionsmatrix gibt die Verteilung von Vorhersagen in wahre und falsche Positiv- und Negativwerte an."
    },
    {
        "question": "Ein Modell hat eine hohe Accuracy, aber einen niedrigen Recall. Was könnte die Ursache sein?",
        "options": [
            "Hohe Anzahl an wahren Negativen.",
            "Hohe Anzahl an Falsch-Positiven.",
            "Hohe Anzahl an Falsch-Negativen.",
            "Es gibt keinen Zusammenhang."
        ],
        "correct_index": 2,
        "explanation": "Ein niedriger Recall deutet darauf hin, dass viele positive Fälle falsch klassifiziert wurden (Falsch-Negative)."
    },
    {
        "question": "Welcher der folgenden Begriffe beschreibt die Sensitivität in einer Klassifikationsaufgabe?",
        "options": [
            "Wahre Positive geteilt durch die Gesamtheit der tatsächlichen Positiven.",
            "Wahre Negative geteilt durch die Gesamtheit der tatsächlichen Negativen.",
            "Wahre Positive geteilt durch die Summe von wahren Positiven und Falsch-Positiven.",
            "Falsch-Negative geteilt durch die Gesamtheit der Positiven."
        ],
        "correct_index": 0,
        "explanation": "Sensitivität misst die Fähigkeit eines Modells, tatsächlich positive Fälle korrekt zu klassifizieren."
    }
]


# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
