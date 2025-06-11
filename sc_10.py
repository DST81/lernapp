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
        "question": "Welche Aussage zur linearen Regression ist korrekt?",
        "options": [
            "Die lineare Regression minimiert die Mean Absolute Error (MAE).",
            "Die lineare Regression minimiert die Summe der quadratischen Abweichungen (SSE).",
            "Die lineare Regression minimiert den Bias-Fehler.",
            "Die lineare Regression ist nicht anfällig für Ausreißer."
        ],
        "correct_index": 1,
        "explanation": "Die lineare Regression minimiert die Summe der quadrierten Fehler (SSE), was ihre Hauptoptimierungsfunktion darstellt."
    },
    {
        "question": "Welche Annahme trifft nicht auf die lineare Regression zu?",
        "options": [
            "Die Beziehung zwischen den unabhängigen und abhängigen Variablen ist linear.",
            "Die Residuen sind unabhängig voneinander.",
            "Die abhängige Variable ist kategorisch.",
            "Es gibt keine Multikollinearität unter den unabhängigen Variablen."
        ],
        "correct_index": 2,
        "explanation": "Lineare Regression ist nur für kontinuierliche abhängige Variablen geeignet, nicht für kategoriale."
    },
    {
        "question": "Was unterscheidet Lasso von Ridge Regression?",
        "options": [
            "Ridge Regression kann Koeffizienten exakt auf 0 setzen, Lasso nicht.",
            "Lasso kann Koeffizienten exakt auf 0 setzen, Ridge nicht.",
            "Beide setzen alle Koeffizienten exakt auf 0.",
            "Beide funktionieren nur mit normalisierten Daten."
        ],
        "correct_index": 1,
        "explanation": "Lasso führt zu sparsamen Modellen, indem es einige Koeffizienten auf exakt 0 setzt."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf Ridge Regression zu?",
        "options": [
            "Ridge Regression fügt eine Regularisierungsstrafe basierend auf der Summe der quadrierten Koeffizienten hinzu.",
            "Ridge Regression setzt einige Koeffizienten auf exakt 0.",
            "Ridge Regression ist empfindlich gegenüber Multikollinearität.",
            "Ridge Regression minimiert ausschließlich den Mean Absolute Error (MAE)."
        ],
        "correct_index": 0,
        "explanation": "Ridge Regression nutzt eine L2-Regularisierung, um Überanpassung zu vermeiden."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf Lasso Regression zu?",
        "options": [
            "Lasso Regression verwendet eine L2-Regularisierung.",
            "Lasso Regression kann Koeffizienten exakt auf 0 setzen.",
            "Lasso Regression ignoriert Korrelationen zwischen Variablen vollständig.",
            "Lasso Regression minimiert nur den Mean Squared Error (MSE)."
        ],
        "correct_index": 1,
        "explanation": "Lasso Regression verwendet eine L1-Regularisierung, die Koeffizienten auf 0 setzen kann."
    },
    {
        "question": "Was beschreibt den Zusammenhang zwischen Bias in Modellen und der Modellkomplexität?",
        "options": [
            "Modelle mit hoher Flexibilität haben in der Regel einen hohen Bias.",
            "Modelle mit geringer Flexibilität haben in der Regel einen hohen Bias.",
            "Modelle mit hoher Flexibilität sind anfällig für hohen Bias und hohe Varianz.",
            "Bias wird durch die Wahl der Evaluationsmetrik direkt bestimmt."
        ],
        "correct_index": 1,
        "explanation": "Geringe Flexibilität führt zu einem hohen Bias, da das Modell die Daten zu stark vereinfacht."
    },
    {
        "question": "Was passiert, wenn ein Modell zu flexibel ist?",
        "options": [
            "Es führt zu einem hohen Bias und niedrigem Overfitting.",
            "Es führt zu einem hohen Varianzfehler und Overfitting.",
            "Es minimiert den Bias und Varianz gleichzeitig.",
            "Es ignoriert die Testdaten bei der Modellanpassung."
        ],
        "correct_index": 1,
        "explanation": "Zu flexible Modelle überanpassen die Trainingsdaten und generalisieren schlecht."
    },
    {
        "question": "Welche Maßnahme kann einen hohen Bias in einem Modell reduzieren?",
        "options": [
            "Die Reduzierung der Trainingsdatenmenge.",
            "Das Streichen von Regularisierungsparametern wie in Ridge Regression.",
            "Die Verwendung eines Modells mit weniger Flexibilität.",
            "Die Erhöhung der Modellkomplexität."
        ],
        "correct_index": 3,
        "explanation": "Höhere Komplexität reduziert Bias, erhöht jedoch das Risiko von Overfitting."
    },
    {
        "question": "Welche Evaluationsmetrik misst die durchschnittliche Abweichung eines Modells in den gleichen Einheiten wie die Zielvariable?",
        "options": [
            "R²",
            "Mean Squared Error (MSE)",
            "Root Mean Squared Error (RMSE)",
            "Mean Absolute Error (MAE)"
        ],
        "correct_index": 3,
        "explanation": "Der MAE gibt die durchschnittliche Abweichung in denselben Einheiten wie die Zielvariable an."
    },
    {
        "question": "Welche Aussage über den R²-Wert ist korrekt?",
        "options": [
            "Ein negativer R²-Wert bedeutet, dass das Modell schlechter ist als ein konstantes Modell.",
            "Ein R²-Wert von 0 bedeutet, dass das Modell die Daten perfekt beschreibt.",
            "Ein R²-Wert von 1 bedeutet, dass das Modell hohe Varianz hat.",
            "Ein positiver R²-Wert bedeutet immer ein perfektes Modell."
        ],
        "correct_index": 0,
        "explanation": "Ein negativer R²-Wert zeigt an, dass das Modell schlechter ist als ein konstantes Modell, das den Mittelwert vorhersagt."
    },
    {
        "question": "Welche der folgenden Metriken wird verwendet, um die Varianz eines Modells zu bewerten?",
        "options": [
            "Mean Absolute Error (MAE)",
            "R²",
            "Mean Squared Error (MSE)",
            "Accuracy"
        ],
        "correct_index": 2,
        "explanation": "MSE misst die durchschnittlichen quadratischen Abweichungen und ist empfindlich gegenüber Varianz."
    },
    {
        "question": "Was ist das Ziel der linearen Regression?",
        "options": [
            "Minimierung der Varianz der Schätzwerte",
            "Maximierung der Korrelation zwischen unabhängigen Variablen",
            "Finden einer linearen Beziehung zwischen abhängigen und unabhängigen Variablen",
            "Maximierung des R²-Wertes"
        ],
        "correct_index": 2,
        "explanation": "Das Hauptziel der linearen Regression ist es, eine lineare Beziehung zwischen den Variablen zu modellieren."
    },
    {
        "question": "In der linearen Regression entspricht der Koeffizient β₀:",
        "options": [
            "Der Steigung der Regressionslinie",
            "Dem y-Achsenabschnitt der Regressionslinie",
            "Dem Fehlerterm",
            "Der Varianz des Modells"
        ],
        "correct_index": 1,
        "explanation": "Der Koeffizient β₀ repräsentiert den Punkt, an dem die Regressionslinie die y-Achse schneidet."
    },
    {
        "question": "Welcher der folgenden Punkte beschreibt die Residuen in einer linearen Regression?",
        "options": [
            "Der Unterschied zwischen den vorhergesagten und den tatsächlichen Werten",
            "Die unabhängigen Variablen im Modell",
            "Die Koeffizienten des Modells",
            "Der Durchschnitt der tatsächlichen Werte"
        ],
        "correct_index": 0,
        "explanation": "Residuen sind die Abweichungen zwischen den tatsächlichen und den vorhergesagten Werten."
    },
    {
        "question": "In welchem Fall ist eine lineare Regression möglicherweise nicht geeignet?",
        "options": [
            "Wenn die Beziehung zwischen den Variablen nicht linear ist",
            "Wenn die Daten nur aus zwei Variablen bestehen",
            "Wenn die Residuen normalverteilt sind",
            "Wenn keine Multikollinearität vorhanden ist"
        ],
        "correct_index": 0,
        "explanation": "Lineare Regression setzt eine lineare Beziehung zwischen den Variablen voraus."
    },
    {
        "question": "Was misst der R²-Wert in einer Regressionsanalyse?",
        "options": [
            "Den Durchschnitt der Fehlerquadrate",
            "Die Streuung der Residuen",
            "Den Anteil der Varianz der abhängigen Variablen, der durch das Modell erklärt wird",
            "Die Differenz zwischen den tatsächlichen und den geschätzten Werten"
        ],
        "correct_index": 2,
        "explanation": "Der R²-Wert gibt an, wie viel der Varianz der abhängigen Variablen durch das Modell erklärt wird."
    },
    {
        "question": "Welche der folgenden Metriken ist besonders anfällig für Ausreißer?",
        "options": [
            "MAE (Mean Absolute Error)",
            "MSE (Mean Squared Error)",
            "R²",
            "Adjusted R²"
        ],
        "correct_index": 1,
        "explanation": "MSE quadratiert die Fehler, was Ausreißer stark gewichtet."
    },
    {
        "question": "Was ist ein Hauptnachteil der Verwendung des R²-Wertes?",
        "options": [
            "Er ist leicht zu interpretieren.",
            "Er kann durch Hinzufügen irrelevanter Variablen steigen.",
            "Er gibt die Varianz des Fehlerterms an.",
            "Er kann nicht negative Werte annehmen."
        ],
        "correct_index": 1,
        "explanation": "Der R²-Wert kann steigen, auch wenn die hinzugefügten Variablen keinen tatsächlichen Nutzen haben."
    },
    {
        "question": "Welches Shrinkage-Modell verwendet eine L1-Regularisierung?",
        "options": [
            "Ridge",
            "Lasso",
            "Lineare Regression",
            "Polynomial Regression"
        ],
        "correct_index": 1,
        "explanation": "Lasso Regression nutzt L1-Regularisierung, um Koeffizienten auf exakt 0 zu setzen."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf Ridge-Regression zu?",
        "options": [
            "Sie führt zu sparsamen Modellen mit vielen Koeffizienten, die genau null sind.",
            "Sie minimiert den MSE, während gleichzeitig die Summe der absoluten Koeffizienten minimiert wird.",
            "Sie fügt eine Strafe für die Summe der quadrierten Koeffizienten hinzu, um Überanpassung zu verhindern.",
            "Sie kann keine multikollinearen Features handhaben."
        ],
        "correct_index": 2,
        "explanation": "Ridge Regression verwendet eine L2-Regularisierung, um große Koeffizienten zu vermeiden."
    },
    {
        "question": "Was ist der Hauptvorteil der Verwendung von Regularisierung in der Regression?",
        "options": [
            "Verbesserung der Trainingsgenauigkeit",
            "Reduzierung der Vorhersagefehler auf den Trainingsdaten",
            "Vermeidung von Überanpassung durch Bestrafung großer Koeffizienten",
            "Erhöhung der Anzahl der verwendeten Variablen"
        ],
        "correct_index": 2,
        "explanation": "Regularisierung reduziert Overfitting, indem große Koeffizienten bestraft werden."
    },
    {
        "question": "Welche Strategie kann verwendet werden, um das Bias-Variance-Dilemma zu lösen?",
        "options": [
            "Erhöhung der Modellkomplexität, ohne Regularisierung",
            "Reduzierung der Anzahl der Trainingsdaten",
            "Verwendung von Ensemble-Methoden wie Bagging oder Boosting",
            "Minimierung der Anzahl der Features im Modell"
        ],
        "correct_index": 2,
        "explanation": "Ensemble-Methoden kombinieren mehrere Modelle, um Bias und Varianz auszugleichen."
    },
    {
        "question": "Wenn ein Modell sowohl auf Trainings- als auch auf Testdaten schlecht abschneidet, spricht man von:",
        "options": [
            "Overfitting",
            "Underfitting",
            "Heteroskedastizität",
            "Multikollinearität"
        ],
        "correct_index": 1,
        "explanation": "Underfitting tritt auf, wenn das Modell zu einfach ist und weder Trainings- noch Testdaten gut beschreibt."
    },
    {
        "question": "Was ist ein häufiger Grund für die Verwendung von Dummy-Variablen in der Regression?",
        "options": [
            "Um die Anzahl der Beobachtungen zu erhöhen",
            "Um kategoriale Variablen in numerische Variablen umzuwandeln",
            "Um die Interpretierbarkeit des Modells zu reduzieren",
            "Um die Multikollinearität zu erhöhen"
        ],
        "correct_index": 1,
        "explanation": "Dummy-Variablen erlauben die Einbindung kategorialer Variablen in Regressionsmodelle."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
