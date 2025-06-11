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
        "question": "Was ist der Hauptvorteil eines Entscheidungsbaums für Regression?",
        "options": [
            "Er ist immer linear.",
            "Er ist einfach zu interpretieren.",
            "Er ist immer genau.",
            "Er benötigt keine Hyperparameter."
        ],
        "correct_index": 1,
        "explanation": "Entscheidungsbäume sind intuitiv verständlich, da sie in hierarchischer Form Bedingungen darstellen."
    },
    {
        "question": "Welche Funktion minimiert ein Entscheidungsbaum im Falle der Regression?",
        "options": [
            "Logarithmischer Verlust",
            "Huber-Verlust",
            "Entropieverlust",
            "Quadratischer Verlust"
        ],
        "correct_index": 3,
        "explanation": "Entscheidungsbäume für Regression minimieren die Summe der quadrierten Abweichungen innerhalb der Blätter."
    },
    {
        "question": "Wie kann ein Entscheidungsbaum vor Überanpassung geschützt werden?",
        "options": [
            "Durch Cross-Validation",
            "Durch Pruning",
            "Durch das Hinzufügen von mehr Daten",
            "Durch das Reduzieren der Anzahl der Merkmale"
        ],
        "correct_index": 1,
        "explanation": "Pruning schneidet übermäßige Tiefe des Entscheidungsbaums zurück, um Überanpassung zu vermeiden."
    },
    {
        "question": "Welche Art von Merkmalen kann ein Entscheidungsbaum verarbeiten?",
        "options": [
            "Nur numerische",
            "Nur kategorische",
            "Sowohl numerische als auch kategorische",
            "Keine der genannten"
        ],
        "correct_index": 2,
        "explanation": "Entscheidungsbäume sind vielseitig und können sowohl numerische als auch kategoriale Daten verarbeiten."
    },
    {
        "question": "Was ist eine Schwäche eines Entscheidungsbaums?",
        "options": [
            "Er kann keine Kategorien verarbeiten.",
            "Er ist schlecht bei großen Datenmengen.",
            "Er kann leicht überanpassen.",
            "Er benötigt eine logarithmische Skalierung der Daten."
        ],
        "correct_index": 2,
        "explanation": "Entscheidungsbäume neigen dazu, die Trainingsdaten zu überanpassen, wenn sie nicht reguliert werden."
    },
    {
        "question": "Woraus besteht ein Random Forest?",
        "options": [
            "Einer Kombination aus linearen Modellen",
            "Mehreren Entscheidungsbäumen",
            "Einer Kombination aus neuronalen Netzen",
            "Einem einzigen tiefen Entscheidungsbaum"
        ],
        "correct_index": 1,
        "explanation": "Ein Random Forest besteht aus einer Vielzahl von Entscheidungsbäumen, die auf Bootstrap-Samples trainiert werden."
    },
    {
        "question": "Was ist der Hauptvorteil eines Random Forest gegenüber einem einzelnen Entscheidungsbaum?",
        "options": [
            "Geringere Trainingszeit",
            "Höhere Interpretierbarkeit",
            "Weniger Überanpassung",
            "Bessere Unterstützung für kategorische Merkmale"
        ],
        "correct_index": 2,
        "explanation": "Random Forests reduzieren Überanpassung durch die Kombination mehrerer Bäume."
    },
    {
        "question": "Welcher der folgenden Begriffe beschreibt eine Technik im Random Forest?",
        "options": [
            "Gradient Descent",
            "Bagging",
            "Boosting",
            "Regularisierung"
        ],
        "correct_index": 1,
        "explanation": "Bagging ist die Technik, die Random Forests zugrunde liegt, indem Modelle auf Bootstrap-Samples trainiert werden."
    },
    {
        "question": "Welche Methode wird verwendet, um die Zufälligkeit in einem Random Forest einzuführen?",
        "options": [
            "Reduktion der Anzahl der Merkmale",
            "Zufällige Auswahl von Datenproben und Merkmalen",
            "Erhöhung der Baumtiefe",
            "Hinzufügen von Noise zu den Daten"
        ],
        "correct_index": 1,
        "explanation": "Zufälligkeit wird eingeführt, indem bei jedem Baum zufällig Daten und Merkmale ausgewählt werden."
    },
    {
        "question": "Was wird in einem Random Forest als \"Out-of-Bag Error\" bezeichnet?",
        "options": [
            "Der Fehler außerhalb des Modells",
            "Der Fehler auf einer Validierungsmenge",
            "Der Fehler auf den nicht für einen bestimmten Baum verwendeten Daten",
            "Der Fehler auf neuen Daten"
        ],
        "correct_index": 2,
        "explanation": "Der Out-of-Bag Error wird basierend auf Datenpunkten berechnet, die nicht in das Bootstrap-Sample eines Baums aufgenommen wurden."
    },
    {
        "question": "Wie kann die Leistung eines Random Forest verbessert werden?",
        "options": [
            "Erhöhen der Anzahl der Bäume",
            "Erhöhen der Baumtiefe",
            "Reduzieren der Trainingsdaten",
            "Hinzufügen von mehr Kategorien zu den Merkmalen"
        ],
        "correct_index": 0,
        "explanation": "Mehr Bäume erhöhen die Stabilität und Leistung des Random Forest."
    },
    {
        "question": "Welche Aussage über Random Forests ist korrekt?",
        "options": [
            "Sie sind anfällig für Überanpassung.",
            "Sie haben eine geringe Robustheit gegen Ausreißer.",
            "Sie können sowohl für Regression als auch Klassifikation verwendet werden.",
            "Sie sind nicht parallelisierbar."
        ],
        "correct_index": 2,
        "explanation": "Random Forests sind flexibel und können für Regression und Klassifikation eingesetzt werden."
    },
    {
        "question": "Was ist der Hauptunterschied zwischen Boosting und Bagging?",
        "options": [
            "Boosting kombiniert mehrere Modelle, um Varianz zu reduzieren.",
            "Boosting erstellt Modelle sequenziell.",
            "Bagging verwendet keine Entscheidungsbäume.",
            "Bagging minimiert Bias."
        ],
        "correct_index": 1,
        "explanation": "Boosting trainiert Modelle sequentiell, wobei jedes Modell Fehler des vorherigen korrigiert."
    },
    {
        "question": "Was optimiert Gradient Boosting für Regression?",
        "options": [
            "Quadratischer Verlust",
            "Cross-Entropy",
            "Mean Absolute Error",
            "Hinge Loss"
        ],
        "correct_index": 0,
        "explanation": "Gradient Boosting optimiert den quadratischen Verlust für Regression."
    },
    {
        "question": "Welche Rolle spielt die Lernrate in Gradient Boosting?",
        "options": [
            "Sie steuert die Anzahl der Bäume.",
            "Sie reduziert die Komplexität der Bäume.",
            "Sie kontrolliert die Gewichtung jedes Baums.",
            "Sie erhöht die Anzahl der Iterationen."
        ],
        "correct_index": 2,
        "explanation": "Die Lernrate bestimmt, wie stark jeder Baum den Fehler des vorherigen korrigiert."
    },
    {
        "question": "Welche Technik wird verwendet, um Gradient Boosting Modelle vor Überanpassung zu schützen?",
        "options": [
            "Tiefe Entscheidungsbäume",
            "Regularisierung",
            "Hinzufügen von Noise zu den Labels",
            "Verwendung von mehr Daten"
        ],
        "correct_index": 1,
        "explanation": "Regularisierung (z. B. L1 oder L2) hilft, Überanpassung bei Gradient Boosting zu vermeiden."
    },
    {
        "question": "Was ist XGBoost?",
        "options": [
            "Ein spezieller Typ eines neuronalen Netzes",
            "Eine implementierte Version von Gradient Boosting",
            "Ein Ensemble von Random Forests",
            "Ein einfacher linearer Regressor"
        ],
        "correct_index": 1,
        "explanation": "XGBoost ist eine leistungsstarke Implementierung des Gradient Boosting Algorithmus mit zusätzlichen Features."
    },
    {
        "question": "Welche Aussage über Gradient Boosting ist korrekt?",
        "options": [
            "Es minimiert nur Bias.",
            "Es trainiert Modelle unabhängig voneinander.",
            "Es minimiert sequentiell den Restfehler.",
            "Es ist nicht anfällig für Überanpassung."
        ],
        "correct_index": 2,
        "explanation": "Gradient Boosting arbeitet sequentiell, um den Restfehler jedes Modells zu minimieren."
    },
    {
        "question": "Welche Hyperparameter sind wichtig für Gradient Boosting Modelle?",
        "options": [
            "Lernrate, Baumtiefe, Anzahl der Bäume",
            "Lernrate, Dropout-Rate, Batch-Größe",
            "Loss-Funktion, Out-of-Bag Fehler, Anzahl der Merkmale",
            "Regularisierung, Entropieverlust, Cross-Validation"
        ],
        "correct_index": 0,
        "explanation": "Lernrate, Baumtiefe und die Anzahl der Bäume sind entscheidende Hyperparameter für Gradient Boosting."
    },
    {
        "question": "Welcher Ensemble-Ansatz wird verwendet, um Bias und Varianz zu minimieren?",
        "options": [
            "Bagging und Boosting",
            "Boosting und Clustering",
            "PCA und Lasso",
            "Cross-Validation und Feature Scaling"
        ],
        "correct_index": 0,
        "explanation": "Sowohl Bagging als auch Boosting helfen, Bias und Varianz zu minimieren, jedoch auf unterschiedliche Weise."
    },
    {
        "question": "Welche Metrik wird häufig verwendet, um Modelle wie Gradient Boosting zu evaluieren?",
        "options": [
            "R²",
            "Mean Absolute Percentage Error (MAPE)",
            "Root Mean Squared Error (RMSE)",
            "Cross-Entropy Loss"
        ],
        "correct_index": 2,
        "explanation": "RMSE ist eine gängige Metrik, um die Leistung von Regressionsmodellen wie Gradient Boosting zu bewerten."
    },
    {
        "question": "Warum ist Gradient Boosting anfälliger für Überanpassung als Random Forests?",
        "options": [
            "Weil es weniger Daten benötigt.",
            "Weil es Modelle sequenziell trainiert und stärker an die Trainingsdaten anpasst.",
            "Weil es keine regulären Hyperparameter hat.",
            "Weil es keine Cross-Validation unterstützt."
        ],
        "correct_index": 1,
        "explanation": "Gradient Boosting passt die Modelle sequentiell an, was die Gefahr von Überanpassung erhöht."
    },
    {
        "question": "Welche Vorteile bietet XGBoost im Vergleich zu herkömmlichem Gradient Boosting?",
        "options": [
            "Es reduziert den Speicherbedarf.",
            "Es verwendet lineare Regression statt Entscheidungsbäume.",
            "Es bietet zusätzliche Features wie Regularisierung, paralleles Training und Early Stopping.",
            "Es unterstützt keine fehlenden Werte."
        ],
        "correct_index": 2,
        "explanation": "XGBoost ist bekannt für seine Effizienz, paralleles Training und erweiterte Features wie Regularisierung und Early Stopping."
    },
    {
        "question": "Wie unterscheidet sich Bagging von Boosting?",
        "options": [
            "Bagging trainiert Modelle sequenziell, während Boosting sie parallel trainiert.",
            "Bagging trainiert Modelle parallel, während Boosting sie sequenziell trainiert.",
            "Bagging ist immer effektiver als Boosting.",
            "Bagging minimiert Bias, während Boosting Varianz minimiert."
        ],
        "correct_index": 1,
        "explanation": "Bagging trainiert Modelle parallel, während Boosting sie sequenziell optimiert."
    },
    {
        "question": "Was ist ein Hauptvorteil von Random Forests gegenüber Gradient Boosting?",
        "options": [
            "Sie sind schneller bei der Hyperparameteroptimierung.",
            "Sie sind robuster gegenüber Ausreißern.",
            "Sie haben eine höhere Vorhersagegenauigkeit.",
            "Sie benötigen weniger Daten für das Training."
        ],
        "correct_index": 1,
        "explanation": "Random Forests sind robuster gegenüber Ausreißern, da sie auf einer Vielzahl von Bäumen basieren."
    },
    {
        "question": "Welche Rolle spielt die Lernrate in Gradient Boosting Modellen?",
        "options": [
            "Sie minimiert die Varianz der Modelle.",
            "Sie kontrolliert, wie stark jedes Modell die Fehler des vorherigen korrigiert.",
            "Sie maximiert die Baumtiefe.",
            "Sie verringert die Anzahl der Iterationen."
        ],
        "correct_index": 1,
        "explanation": "Die Lernrate bestimmt die Gewichtung der einzelnen Modelle in Gradient Boosting."
    },
    {
        "question": "Warum wird Regularisierung in Gradient Boosting Modellen verwendet?",
        "options": [
            "Um die Lernrate zu erhöhen.",
            "Um die Trainingszeit zu reduzieren.",
            "Um Überanpassung zu verhindern.",
            "Um die Varianz zu maximieren."
        ],
        "correct_index": 2,
        "explanation": "Regularisierung hilft, Überanpassung in Gradient Boosting Modellen zu verhindern, indem sie komplexe Modelle bestraft."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
