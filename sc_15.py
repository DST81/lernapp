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
        "question": "Was ist das Hauptziel von Dimensionsreduktionsverfahren?",
        "options": [
            "Daten zu erweitern und zusätzliche Dimensionen hinzuzufügen.",
            "Die Anzahl der Dimensionen zu reduzieren, um Rechenaufwand zu minimieren.",
            "Daten zu löschen, die nicht mehr benötigt werden.",
            "Eine visuelle Darstellung in 3D zu erstellen."
        ],
        "correct_index": 1,
        "explanation": "Dimensionsreduktionsverfahren zielen darauf ab, die Anzahl der Dimensionen zu reduzieren, um den Rechenaufwand zu senken und die Daten interpretierbarer zu machen."
    },
    {
        "question": "Welches der folgenden Verfahren ist ein lineares Dimensionsreduktionsverfahren?",
        "options": [
            "PCA (Principal Component Analysis).",
            "t-SNE (t-Distributed Stochastic Neighbor Embedding).",
            "UMAP (Uniform Manifold Approximation and Projection).",
            "LDA (Linear Discriminant Analysis)."
        ],
        "correct_index": 0,
        "explanation": "PCA ist ein lineares Verfahren, das die Hauptkomponenten (Principal Components) eines Datensatzes berechnet, um die Varianz zu maximieren. Es projiziert die Daten in eine neue lineare Basis mit weniger Dimensionen."
    },
    {
        "question": "Was bedeutet 'Curse of Dimensionality'?",
        "options": [
            "Der Verlust von Interpretierbarkeit bei hochdimensionalen Daten.",
            "Die Schwierigkeit, Muster oder Beziehungen in hochdimensionalen Daten zu finden.",
            "Die Zunahme der benötigten Datenmenge mit wachsender Dimension.",
            "Alle oben genannten."
        ],
        "correct_index": 3,
        "explanation": "Der 'Curse of Dimensionality' umfasst verschiedene Herausforderungen, die mit hochdimensionalen Daten einhergehen, einschließlich Interpretationsverlust, Mustererkennung und Datenanforderungen."
    },
    {
        "question": "Welcher Ansatz kann helfen, den Curse of Dimensionality zu bewältigen?",
        "options": [
            "Hinzufügen von mehr Dimensionen.",
            "Dimensionsreduktion.",
            "Erhöhen der Trainingsdaten.",
            "Dimensionsreduktion und Erhöhen der Trainingsdaten."
        ],
        "correct_index": 3,
        "explanation": "Die Kombination aus Dimensionsreduktion und Erhöhung der Datenmenge hilft, die Probleme des Curse of Dimensionality zu lindern."
    },
    {
        "question": "Was ist das Ziel von PCA?",
        "options": [
            "Maximierung der Datenvarianz in niedrigeren Dimensionen.",
            "Erhaltung der originalen Datenstruktur.",
            "Klassifizierung von Daten.",
            "Clusteranalyse."
        ],
        "correct_index": 0,
        "explanation": "PCA reduziert die Dimensionen eines Datensatzes, indem es die Varianz in den Hauptkomponenten maximiert."
    },
    {
        "question": "Welche Einschränkung hat PCA?",
        "options": [
            "Es ist nicht für nicht-lineare Strukturen geeignet.",
            "Es kann nicht mit hochdimensionalen Daten arbeiten.",
            "Es erfordert große Trainingsdatenmengen.",
            "Es kann keine Varianz erhalten."
        ],
        "correct_index": 0,
        "explanation": "PCA basiert auf linearen Zusammenhängen und ist nicht geeignet, nicht-lineare Muster in den Daten zu erkennen."
    },
    {
        "question": "Wofür wird t-SNE typischerweise verwendet?",
        "options": [
            "Lineare Regression.",
            "Visualisierung hochdimensionaler Daten.",
            "Clusteranalyse.",
            "Klassifikation."
        ],
        "correct_index": 1,
        "explanation": "t-SNE ist ein nicht-lineares Verfahren, das häufig zur Visualisierung hochdimensionaler Daten in niedrigdimensionalen Räumen eingesetzt wird."
    },
    {
        "question": "Welche Eigenschaft hat t-SNE im Vergleich zu PCA?",
        "options": [
            "Es ist schneller als PCA.",
            "Es erhält globale Strukturen besser als PCA.",
            "Es erhält lokale Strukturen besser als PCA.",
            "Es kann nur mit linearen Daten arbeiten."
        ],
        "correct_index": 2,
        "explanation": "t-SNE bewahrt lokale Strukturen und Beziehungen besser als PCA, eignet sich jedoch weniger für globale Strukturen."
    },
    {
        "question": "Was ist eine typische Einschränkung von t-SNE?",
        "options": [
            "Es funktioniert nicht mit mehr als zwei Dimensionen.",
            "Es ist rechnerisch intensiv und langsam bei großen Datensätzen.",
            "Es kann keine Visualisierungen erzeugen.",
            "Es benötigt keine Hyperparameter."
        ],
        "correct_index": 1,
        "explanation": "t-SNE ist rechnerisch aufwendig und kann bei großen Datensätzen sehr langsam sein."
    },
    {
        "question": "Welche der folgenden Aussagen beschreibt UMAP korrekt?",
        "options": [
            "UMAP ist ein lineares Dimensionsreduktionsverfahren.",
            "UMAP eignet sich nicht für Clusteranalysen.",
            "UMAP ist schneller und behält lokale sowie globale Strukturen besser als t-SNE.",
            "UMAP basiert auf der Varianzmaximierung."
        ],
        "correct_index": 2,
        "explanation": "UMAP ist schneller als t-SNE und kann sowohl lokale als auch globale Strukturen besser bewahren, weshalb es oft bevorzugt wird."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
