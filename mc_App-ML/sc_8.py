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
        "question": "Welche der folgenden Methoden ist eine gängige Technik für den Umgang mit fehlenden Werten?",
        "options": [
            "Daten ignorieren",
            "Mittelwert-Auffüllung",
            "Dropout",
            "Doppelte Werte hinzufügen"
        ],
        "correct_index": 1,
        "explanation": "Die Mittelwert-Auffüllung ist eine verbreitete Technik, um fehlende Werte durch den Durchschnitt der existierenden Werte zu ersetzen."
    },
    {
        "question": "Welche der folgenden Strategien führt zu einem Informationsverlust?",
        "options": [
            "Imputation durch den Median",
            "One-hot Encoding",
            "Löschen von Zeilen mit fehlenden Werten",
            "Skalierung der Daten"
        ],
        "correct_index": 2,
        "explanation": "Das Löschen von Zeilen mit fehlenden Werten reduziert die Datenmenge und führt oft zu Informationsverlust."
    },
    {
        "question": "Was ist der Zweck des One-hot Encodings?",
        "options": [
            "Um numerische Variablen zu kategorischen zu machen",
            "Um kategorische Variablen in numerische Variablen umzuwandeln",
            "Um die Reihenfolge in ordinalen Daten zu kodieren",
            "Um fehlende Werte zu behandeln"
        ],
        "correct_index": 1,
        "explanation": "One-hot Encoding wandelt kategoriale Variablen in binäre Indikatorvariablen um."
    },
    {
        "question": "Welches Problem kann auftreten, wenn man One-hot Encoding auf eine kategorische Variable mit sehr vielen einzigartigen Werten anwendet?",
        "options": [
            "Der Datensatz wird sehr groß und schwer zu verarbeiten",
            "Alle Werte werden zu Null",
            "Es gibt keine Auswirkungen",
            "Es führt immer zu einer besseren Performance"
        ],
        "correct_index": 0,
        "explanation": "One-hot Encoding bei vielen Kategorien erhöht die Dimension des Datensatzes drastisch, was die Verarbeitung erschwert."
    },
    {
        "question": "Was ist der Hauptzweck der Yeo-Johnson-Transformation?",
        "options": [
            "Fehlende Werte zu ersetzen",
            "Kategorische Daten zu kodieren",
            "Numerische Daten zu normalisieren",
            "Verteilungen von Variablen zu stabilisieren und Normalverteilung zu erreichen"
        ],
        "correct_index": 3,
        "explanation": "Die Yeo-Johnson-Transformation hilft, schiefe Verteilungen zu stabilisieren und eine Normalverteilung herzustellen."
    },
    {
        "question": "Worin liegt der Unterschied zwischen der Yeo-Johnson-Transformation und der Box-Cox-Transformation?",
        "options": [
            "Yeo-Johnson kann nur positive Werte transformieren, während Box-Cox auch negative Werte verarbeiten kann.",
            "Box-Cox kann nur positive Werte transformieren, während Yeo-Johnson auch negative Werte verarbeiten kann.",
            "Beide Transformationsmethoden arbeiten nur mit ordinalen Variablen.",
            "Es gibt keinen Unterschied zwischen beiden Transformationsmethoden."
        ],
        "correct_index": 1,
        "explanation": "Die Yeo-Johnson-Transformation ist flexibler, da sie auch negative Werte transformieren kann."
    },
    {
        "question": "Welche der folgenden Skalierungsmethoden setzt voraus, dass die Daten eine Normalverteilung aufweisen?",
        "options": [
            "Min-Max-Skalierung",
            "RobustScaler",
            "StandardScaler",
            "Keine der oben genannten"
        ],
        "correct_index": 2,
        "explanation": "Der StandardScaler setzt Normalverteilung voraus, da er den Mittelwert auf 0 und die Standardabweichung auf 1 setzt."
    },
    {
        "question": "Was ist der Unterschied zwischen Min-Max-Skalierung und Standard-Skalierung?",
        "options": [
            "Min-Max-Skalierung setzt den Mittelwert auf Null, während die Standard-Skalierung die Werte zwischen 0 und 1 skaliert.",
            "Min-Max-Skalierung bringt alle Werte in den Bereich [0, 1], während die Standard-Skalierung den Mittelwert auf 0 und die Standardabweichung auf 1 setzt.",
            "Beide Methoden erzeugen identische Ergebnisse.",
            "Min-Max-Skalierung ist nur für ordinale Variablen anwendbar."
        ],
        "correct_index": 1,
        "explanation": "Min-Max-Skalierung skaliert Werte in einen festen Bereich, Standard-Skalierung normiert Werte relativ zu ihrer Verteilung."
    },
    {
        "question": "Welche der folgenden Methoden kann verwendet werden, um fehlende Werte in einer numerischen Spalte aufzufüllen?",
        "options": [
            "Label-Encoding",
            "Median-Interpolation",
            "One-hot-Encoding",
            "Modus-Imputation"
        ],
        "correct_index": 1,
        "explanation": "Median-Interpolation ist eine gängige Methode, um fehlende numerische Werte durch den Median zu ersetzen."
    },
    {
        "question": "Was ist der Hauptnachteil von Label-Encoding für eine nicht ordinale kategorische Variable?",
        "options": [
            "Es funktioniert nicht mit großen Datensätzen.",
            "Es gibt keine Nachteile.",
            "Das Modell könnte fälschlicherweise eine Rangordnung zwischen den Kategorien annehmen.",
            "Es führt zu einer erhöhten Anzahl von Spalten im Datensatz."
        ],
        "correct_index": 2,
        "explanation": "Label-Encoding kann Probleme verursachen, da es impliziert, dass die Kategorien eine Reihenfolge haben."
    },
    {
        "question": "Welches Problem kann beim One-hot Encoding von kategorialen Variablen mit einer großen Anzahl von Kategorien auftreten?",
        "options": [
            "Overfitting durch zu viele Parameter",
            "Verzerrung durch unsachgemäße Normalisierung",
            "Es entsteht zu wenig Varianz",
            "Das Modell kann keine gewichteten Beziehungen lernen"
        ],
        "correct_index": 0,
        "explanation": "Viele Kategorien im One-hot Encoding können zu Overfitting und einer erhöhten Komplexität führen."
    },
    {
        "question": "Wann wäre es nicht sinnvoll, eine Yeo-Johnson- oder Box-Cox-Transformation durchzuführen?",
        "options": [
            "Wenn die Daten bereits normalverteilt sind",
            "Wenn die Daten numerisch sind",
            "Wenn die Daten stark schief sind",
            "Wenn die Daten keine negativen Werte enthalten"
        ],
        "correct_index": 0,
        "explanation": "Eine Transformation ist nicht notwendig, wenn die Daten bereits normalverteilt sind."
    },
    {
        "question": "Welche Art von Transformation sollte angewendet werden, wenn die Verteilung einer Variablen stark positiv schief ist?",
        "options": [
            "Logarithmische Transformation",
            "Quadratische Transformation",
            "Min-Max-Skalierung",
            "Label-Encoding"
        ],
        "correct_index": 0,
        "explanation": "Eine logarithmische Transformation hilft, stark positive Schiefen auszugleichen."
    },
    {
        "question": "Welches Problem kann auftreten, wenn die Daten für das Test-Set und Trainings-Set unterschiedlich skaliert werden?",
        "options": [
            "Es führt zu Overfitting",
            "Es führt zu einem Informationsverlust",
            "Es kann zu Inkonsistenzen und schlechter Performance im Modell führen",
            "Es wird das Modell nicht beeinflussen"
        ],
        "correct_index": 2,
        "explanation": "Unterschiedliche Skalierung zwischen Training und Test führt zu Inkonsistenzen und schlechter Modellleistung."
    },
    {
        "question": "Welcher Algorithmus erfordert nicht zwangsläufig eine Skalierung der Daten, um gut zu funktionieren?",
        "options": [
            "K-Means",
            "Neuronale Netze",
            "Entscheidungsbäume",
            "SVM"
        ],
        "correct_index": 2,
        "explanation": "Entscheidungsbäume sind unempfindlich gegenüber der Skalierung der Eingabedaten."
    },
    {
        "question": "Was ist der Hauptunterschied zwischen Filter-, Wrapper- und Embedded-Methoden der Merkmalsauswahl?",
        "options": [
            "Filter-Methoden berücksichtigen das Ergebnis der Modellierung, Wrapper-Methoden nicht.",
            "Wrapper-Methoden nutzen das Modell selbst zur Bewertung von Features, Filter-Methoden basieren auf statistischen Tests ohne Modell.",
            "Embedded-Methoden sind unabhängig vom verwendeten Modell, während Filter-Methoden das Modell beeinflussen.",
            "Filter-Methoden basieren auf Cross-Validation, Wrapper-Methoden nicht."
        ],
        "correct_index": 1,
        "explanation": "Wrapper-Methoden verwenden das Modell zur Bewertung von Features, während Filter-Methoden modellunabhängig sind."
    },
    {
        "question": "Was ist der Hauptnachteil von Wrapper-Methoden?",
        "options": [
            "Sie berücksichtigen die Abhängigkeit zwischen den Features nicht.",
            "Sie können bei großen Datensätzen sehr rechenintensiv und langsam sein.",
            "Sie sind immer weniger präzise als Filter-Methoden.",
            "Sie basieren nur auf der Statistik und ignorieren Modellperformance."
        ],
        "correct_index": 1,
        "explanation": "Wrapper-Methoden sind rechenintensiv, da sie das Modell mehrfach trainieren."
    },
    {
        "question": "Was ist ein konstantes Feature?",
        "options": [
            "Ein Feature, das einen sehr kleinen Wertebereich aufweist.",
            "Ein Feature, das denselben Wert für alle Beobachtungen enthält.",
            "Ein Feature, das stark mit dem Zielwert korreliert.",
            "Ein Feature, das einen hohen Anteil fehlender Werte hat."
        ],
        "correct_index": 1,
        "explanation": "Ein konstantes Feature hat keine Varianz und enthält daher keine nützliche Information."
    },
    {
        "question": "Warum ist es wichtig, konstante und quasikonstante Features zu entfernen?",
        "options": [
            "Weil sie die Modellgenauigkeit verbessern.",
            "Weil sie die Modellleistung oft verschlechtern und gleichzeitig keinen Nutzen bringen.",
            "Weil sie immer Ausreißer enthalten.",
            "Weil sie zu hohe Korrelationen verursachen."
        ],
        "correct_index": 1,
        "explanation": "Konstante und quasikonstante Features liefern keine zusätzliche Information und können das Modell unnötig komplizieren."
    },
{
        "question": "Welches Kriterium wird häufig verwendet, um quasikonstante Features zu identifizieren?",
        "options": [
            "Ein Feature, bei dem mehr als 95% der Werte identisch sind.",
            "Ein Feature, das eine Nullvarianz aufweist.",
            "Ein Feature, dessen Werte vollständig fehlend sind.",
            "Ein Feature, das eine Korrelation von 1 aufweist."
        ],
        "correct_index": 0,
        "explanation": "Quasikonstante Features haben einen sehr hohen Anteil identischer Werte."
    },
    {
        "question": "Welche Methode wird typischerweise verwendet, um Features mit starker Korrelation zu entfernen?",
        "options": [
            "Pearson-Korrelation",
            "Lasso-Regression",
            "Chi-Quadrat-Test",
            "Sequential Feature Selection"
        ],
        "correct_index": 0,
        "explanation": "Die Pearson-Korrelation misst die lineare Beziehung zwischen zwei Variablen."
    },
    {
        "question": "Was ist der Hauptgrund dafür, dass stark korrelierte Features in der Datenaufbereitung entfernt werden sollten?",
        "options": [
            "Sie verlangsamen den Trainingsprozess des Modells.",
            "Sie verursachen Multikollinearität und können die Modellinterpretation erschweren.",
            "Sie erhöhen die Anzahl der benötigten Trainingsdaten.",
            "Sie erhöhen die Anzahl der Modellparameter."
        ],
        "correct_index": 1,
        "explanation": "Stark korrelierte Features können Multikollinearität verursachen, was die Stabilität und Interpretierbarkeit des Modells beeinträchtigt."
    },
    {
        "question": "Welche Methode gehört zu den Filter-Methoden?",
        "options": [
            "Rückwärts-Eliminierung",
            "Lasso-Regression",
            "Pearson-Korrelation",
            "Random-Forest-Feature-Importances"
        ],
        "correct_index": 2,
        "explanation": "Die Pearson-Korrelation ist eine Filter-Methode, da sie unabhängig vom Modell verwendet wird."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf Embedded-Methoden zu?",
        "options": [
            "Sie basieren ausschließlich auf statistischen Tests und berücksichtigen keine Modellperformance.",
            "Sie nutzen das Modelltraining, um gleichzeitig Features zu bewerten und zu selektieren.",
            "Sie testen jedes Feature einzeln und unabhängig von anderen Features.",
            "Sie erfordern kein Modelltraining und basieren nur auf den Datenmerkmalen."
        ],
        "correct_index": 1,
        "explanation": "Embedded-Methoden integrieren die Feature-Auswahl direkt in den Modellierungsprozess."
    },
    {
        "question": "Welche der folgenden Aussagen beschreibt den Hauptnachteil von Embedded-Methoden?",
        "options": [
            "Sie sind sehr langsam, da sie alle Feature-Kombinationen durchprobieren.",
            "Sie können zu Overfitting führen, wenn das Modell zu komplex ist.",
            "Sie berücksichtigen keine Abhängigkeiten zwischen den Features.",
            "Sie können keine großen Datensätze verarbeiten."
        ],
        "correct_index": 1,
        "explanation": "Komplexe Modelle bei Embedded-Methoden können zu Overfitting führen."
    },
    {
        "question": "Was ist eine übliche Schwelle für quasikonstante Features?",
        "options": [
            "Wenn mehr als 80% der Werte gleich sind.",
            "Wenn weniger als 2% der Werte unterschiedlich sind.",
            "Wenn mehr als 95% der Werte gleich sind.",
            "Wenn der Mittelwert der Werte Null ist."
        ],
        "correct_index": 2,
        "explanation": "Quasikonstante Features werden oft identifiziert, wenn 95% oder mehr der Werte identisch sind."
    },
    {
        "question": "Warum sollten quasikonstante Features entfernt werden?",
        "options": [
            "Sie enthalten keine Variabilität und können das Modell verlangsamen.",
            "Sie haben einen großen Einfluss auf das Modell.",
            "Sie haben hohe Korrelationen mit anderen Features.",
            "Sie verursachen immer Multikollinearität."
        ],
        "correct_index": 0,
        "explanation": "Quasikonstante Features tragen keine signifikante Information bei und erhöhen die Modellkomplexität unnötig."
    },
    {
        "question": "Warum sollten doppelte Features entfernt werden?",
        "options": [
            "Sie haben immer fehlende Werte.",
            "Sie verursachen hohe Rechenkosten ohne Mehrwert.",
            "Sie haben keine Korrelationen mit dem Zielwert.",
            "Sie verursachen Multikollinearität und erhöhen die Komplexität."
        ],
        "correct_index": 1,
        "explanation": "Doppelte Features bieten keine zusätzlichen Informationen und erhöhen nur den Rechenaufwand."
    },
    {
        "question": "Welche Korrelationstechnik wird normalerweise für numerische Features verwendet?",
        "options": [
            "Chi-Quadrat-Test",
            "Pearson-Korrelation",
            "Lasso-Regression",
            "Varianzschwellenwert"
        ],
        "correct_index": 1,
        "explanation": "Die Pearson-Korrelation misst die lineare Beziehung zwischen zwei numerischen Variablen."
    },
    {
        "question": "Welche Schwelle wird häufig verwendet, um stark korrelierte Features zu identifizieren?",
        "options": [
            "Ein Korrelationskoeffizient von 0,1 oder höher.",
            "Ein Korrelationskoeffizient von 0,3 oder höher.",
            "Ein Korrelationskoeffizient von 0,6 oder höher.",
            "Ein Korrelationskoeffizient von 0,7 oder höher."
        ],
        "correct_index": 3,
        "explanation": "Eine Schwelle von 0,7 oder höher wird häufig verwendet, um starke Korrelationen zu identifizieren."
    },
    {
        "question": "Was sollte getan werden, wenn zwei Features stark miteinander korrelieren?",
        "options": [
            "Beide Features entfernen.",
            "Eines der beiden Features entfernen, basierend auf dessen Wichtigkeit.",
            "Die Features miteinander kombinieren.",
            "Die Korrelation ignorieren, da sie keinen Einfluss hat."
        ],
        "correct_index": 1,
        "explanation": "Das Entfernen eines der beiden Features reduziert Redundanz und verbessert die Modellinterpretation."
    },
    {
        "question": "Welcher Algorithmus ist besonders empfindlich gegenüber stark korrelierten Features?",
        "options": [
            "Entscheidungsbäume",
            "Neuronale Netze",
            "K-Nearest Neighbors (k-NN)",
            "Lineare Regression"
        ],
        "correct_index": 3,
        "explanation": "Lineare Regression ist besonders anfällig für Multikollinearität, die durch stark korrelierte Features verursacht wird."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
