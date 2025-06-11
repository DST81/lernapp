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
        "question": "Was ist das Hauptziel der Cross-Validation?",
        "options": [
            "Daten zu normalisieren",
            "Das Modell auf Überanpassung (Overfitting) und Unteranpassung (Underfitting) zu testen",
            "Hyperparameter zu optimieren",
            "Ein Modell mit dem höchsten Trainingsfehler zu erstellen"
        ],
        "correct_index": 1,
        "explanation": "Cross-Validation dient dazu, die Generalisierungsfähigkeit eines Modells zu bewerten und Über- sowie Unteranpassung zu identifizieren."
    },
    {
        "question": "Was ist ein häufiges Ziel von Cross-Validation in der Modelloptimierung?",
        "options": [
            "Die Testdaten besser anzupassen",
            "Ein Modell zu finden, das in allen Trainingsfalten überanpasst",
            "Hyperparameter zu optimieren",
            "Die Effizienz des Modells zu maximieren"
        ],
        "correct_index": 2,
        "explanation": "Cross-Validation wird oft verwendet, um die besten Hyperparameter für ein Modell zu bestimmen."
    },
    {
        "question": "Worin besteht der Hauptunterschied zwischen Leave-One-Out Cross-Validation (LOOCV) und k-Fold Cross-Validation?",
        "options": [
            "LOOCV verwendet alle Datenpunkte außer einem als Trainingsdaten, während k-Fold die Daten in k gleiche Teile aufteilt.",
            "LOOCV führt zu Ergebnissen mit hoher Varianz, da jede Iteration nur einen Testpunkt verwendet.",
            "LOOCV ist schneller als k-Fold Cross-Validation.",
            "LOOCV und k-Fold Cross-Validation sind identisch."
        ],
        "correct_index": 0,
        "explanation": "LOOCV testet nacheinander jeden Datenpunkt, während k-Fold die Daten in gleich große Falten teilt."
    },
    {
        "question": "Was unterscheidet Stratified Cross-Validation von regulärem k-Fold Cross-Validation?",
        "options": [
            "Stratified Cross-Validation ist für alle Datentypen geeignet.",
            "Stratified Cross-Validation stellt sicher, dass jede Klasse in jedem Fold proportional zur Originalverteilung bleibt.",
            "Stratified Cross-Validation verwendet nur Trainingsdaten, keine Validierungsdaten.",
            "Stratified Cross-Validation funktioniert nur mit binären Klassifikationen."
        ],
        "correct_index": 1,
        "explanation": "Stratified Cross-Validation sorgt dafür, dass Klassenverhältnisse in jedem Fold erhalten bleiben, was besonders bei unausgewogenen Datensätzen wichtig ist."
    },
    {
        "question": "Welche der folgenden Aussagen ist korrekt bezüglich Grid Search?",
        "options": [
            "Grid Search durchsucht einen vordefinierten Hyperparameter-Raum systematisch.",
            "Grid Search wählt die Hyperparameter zufällig aus.",
            "Grid Search ist schneller als Random Search.",
            "Grid Search verwendet keine Cross-Validation."
        ],
        "correct_index": 0,
        "explanation": "Grid Search durchsucht systematisch alle möglichen Kombinationen eines vorgegebenen Hyperparameter-Raums."
    },
    {
        "question": "Wann ist Random Search typischerweise effizienter als Grid Search?",
        "options": [
            "Wenn der Hyperparameter-Raum sehr klein ist.",
            "Wenn alle Hyperparameter gleich wichtig sind.",
            "Wenn nur ein Hyperparameter optimiert wird.",
            "Wenn der Hyperparameter-Raum sehr groß ist."
        ],
        "correct_index": 3,
        "explanation": "Random Search testet zufällig ausgewählte Kombinationen und ist daher bei großen Hyperparameter-Räumen effizienter."
    },
    {
        "question": "Warum wird Stratified Cross-Validation häufig bei Klassifikationsproblemen verwendet?",
        "options": [
            "Um die Berechnungen zu beschleunigen.",
            "Um sicherzustellen, dass jede Klasse in den Trainings- und Validierungsdaten proportional vertreten ist.",
            "Um Overfitting zu verhindern.",
            "Weil es einfacher zu implementieren ist."
        ],
        "correct_index": 1,
        "explanation": "Stratified Cross-Validation bewahrt die Klassenverteilung und ist somit ideal für Klassifikationsprobleme."
    },
    {
        "question": "Was ist ein Nachteil von Leave-One-Out Cross-Validation?",
        "options": [
            "Es ist rechnerisch sehr aufwendig.",
            "LOOCV führt zu Ergebnissen mit hoher Varianz, da jede Iteration nur einen Testpunkt verwendet.",
            "Es kann nicht für Klassifikationsprobleme verwendet werden.",
            "Es verwendet keine Cross-Validation."
        ],
        "correct_index": 1,
        "explanation": "LOOCV ist ressourcenintensiv und neigt zu hoher Varianz, da nur ein Testpunkt pro Iteration genutzt wird."
    },
    {
        "question": "Was ist der Hauptunterschied zwischen Grid Search und Random Search?",
        "options": [
            "Grid Search probiert alle Kombinationen aus, Random Search probiert eine zufällige Auswahl.",
            "Grid Search ist effizienter als Random Search.",
            "Random Search garantiert die beste Lösung, Grid Search nicht.",
            "Grid Search funktioniert nicht mit großen Datensätzen."
        ],
        "correct_index": 0,
        "explanation": "Grid Search testet alle Kombinationen, während Random Search eine zufällige Auswahl testet."
    },
    {
        "question": "Welche Aussage trifft auf Cross-Validation zu?",
        "options": [
            "Sie wird nur bei linearen Modellen verwendet.",
            "Sie verbessert automatisch die Modellgenauigkeit.",
            "Sie teilt die Daten in Trainings- und Validierungsdaten auf.",
            "Sie benötigt keine Hyperparameter."
        ],
        "correct_index": 2,
        "explanation": "Cross-Validation teilt die Daten in Trainings- und Validierungssets, um die Modellleistung zu bewerten."
    },
    {
        "question": "Wann sollte Stratified Cross-Validation NICHT verwendet werden?",
        "options": [
            "Bei einer unbalancierten Klassendatenverteilung.",
            "Bei einem Regressionsproblem.",
            "Bei einem binären Klassifikationsproblem.",
            "Bei einer Multiklassenklassifikation."
        ],
        "correct_index": 1,
        "explanation": "Stratified Cross-Validation wird speziell für Klassifikationsprobleme verwendet, um Klassenverhältnisse zu bewahren. Bei Regressionen ist es nicht anwendbar."
    },
    {
        "question": "Was ist das Hauptziel bei der Verwendung von Ridge-Regression in Kombination mit Cross-Validation?",
        "options": [
            "Die beste Baumtiefe zu finden.",
            "Den optimalen Regularisierungsparameter α zu wählen, um Überanpassung zu vermeiden.",
            "Die Anzahl der Merkmale im Modell zu maximieren.",
            "Die Vorhersagekraft auf den Trainingsdaten zu optimieren."
        ],
        "correct_index": 1,
        "explanation": "Cross-Validation hilft, den optimalen Regularisierungsparameter α zu wählen, der Überanpassung reduziert."
    },
    {
        "question": "Welche Hyperparameter können bei der Lasso-Regression optimiert werden?",
        "options": [
            "Die Anzahl der Falten in der Cross-Validation.",
            "Der Regularisierungsparameter α, der die Stärke der Feature-Selektion steuert.",
            "Die maximale Tiefe des Entscheidungsbaums.",
            "Die Anzahl der Schichten im neuronalen Netz."
        ],
        "correct_index": 1,
        "explanation": "Der Regularisierungsparameter α steuert die Stärke der Regularisierung und Feature-Selektion in der Lasso-Regression."
    },
    {
        "question": "Was ist das Ziel des Tree Prunings in Entscheidungsbäumen?",
        "options": [
            "Die Tiefe des Baumes zu maximieren.",
            "Die Anzahl der Merkmale zu erhöhen.",
            "Überanpassung zu reduzieren, indem unnötige Zweige entfernt werden.",
            "Die Leistung auf den Trainingsdaten zu erhöhen."
        ],
        "correct_index": 2,
        "explanation": "Pruning entfernt unnötige Zweige, um die Komplexität des Baumes zu reduzieren und Überanpassung zu vermeiden."
    },
    {
        "question": "Wie hilft Grid Search bei der Optimierung von Random Forests?",
        "options": [
            "Es reduziert automatisch die Anzahl der Bäume.",
            "Es testet verschiedene Kombinationen von Hyperparametern wie maximale Tiefe, Anzahl der Bäume und maximale Merkmale.",
            "Es führt die Random Forests ohne Cross-Validation aus.",
            "Es erhöht die Anzahl der Trainingsdaten."
        ],
        "correct_index": 1,
        "explanation": "Grid Search optimiert Random Forests durch systematisches Testen verschiedener Kombinationen von Hyperparametern."
    },
    {
        "question": "Warum könnte Random Search effizienter sein als Grid Search bei der Hyperparameteroptimierung von Random Forests?",
        "options": [
            "Es testet automatisch alle Parameterkombinationen.",
            "Es reduziert die Varianz des Modells.",
            "Es konzentriert sich auf zufällige Stichproben und kann bei einem großen Hyperparameterraum bessere Ergebnisse in kürzerer Zeit liefern.",
            "Es erhöht die Modellkomplexität."
        ],
        "correct_index": 2,
        "explanation": "Random Search testet zufällige Kombinationen und ist effizienter bei großen Hyperparameter-Räumen."
    },
    {
        "question": "Wie hilft Stratified Cross-Validation bei der Optimierung von Ridge- und Lasso-Modellen?",
        "options": [
            "Sie stellt sicher, dass jede Klasse in den Falten gleichmäßig verteilt ist, was für Klassifikationsprobleme mit Regularisierungsmodellen wichtig ist.",
            "Sie maximiert die Tiefe der Entscheidungsbäume.",
            "Sie erhöht die Anzahl der Testdaten.",
            "Sie wird nur bei Random Forests verwendet."
        ],
        "correct_index": 0,
        "explanation": "Stratified Cross-Validation stellt sicher, dass die Klassenverteilung in den Falten erhalten bleibt, was besonders bei Klassifikationsproblemen wichtig ist."
    },
    {
        "question": "Welche Hyperparameter sollten typischerweise bei der Optimierung eines Entscheidungsbaums durch Grid Search untersucht werden?",
        "options": [
            "Die Anzahl der Bäume und die Anzahl der Features.",
            "Die maximale Tiefe des Baums, die minimale Anzahl von Samples pro Blatt, und die minimale Anzahl von Samples, um einen Split zu machen.",
            "Der Regularisierungsparameter α.",
            "Die Anzahl der Knoten in jedem Blatt."
        ],
        "correct_index": 1,
        "explanation": "Wichtige Hyperparameter bei Entscheidungsbäumen sind die Baumtiefe und die Mindestanzahl von Datenpunkten für Splits oder Blätter."
    },
    {
        "question": "Warum wird Lasso-Regression oft bei Feature-Selektion eingesetzt?",
        "options": [
            "Weil sie alle Features gleich behandelt.",
            "Weil sie irrelevante Features automatisch auf null setzt.",
            "Weil sie die Anzahl der Trainingsdaten erhöht.",
            "Weil sie keine Regularisierung verwendet."
        ],
        "correct_index": 1,
        "explanation": "Lasso-Regression setzt irrelevante Koeffizienten auf null und selektiert somit automatisch wichtige Features."
    },
    {
        "question": "Welche Kombination von Verfahren ist am besten geeignet, um ein Modell mit Random Forests zu optimieren?",
        "options": [
            "Cross-Validation in Kombination mit Grid Search oder Random Search zur Auswahl der besten Hyperparameter.",
            "Leave-One-Out Cross-Validation, um jeden Datenpunkt als Testdaten zu verwenden.",
            "Maximale Tiefe erhöhen, ohne andere Hyperparameter zu ändern.",
            "Baumpruning anwenden, um die Komplexität zu reduzieren."
        ],
        "correct_index": 0,
        "explanation": "Die Kombination von Cross-Validation mit Grid oder Random Search ist eine bewährte Methode zur Optimierung von Random Forests."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
