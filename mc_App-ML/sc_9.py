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
        "question": "Welche der folgenden Distanzen wird am häufigsten im k-Means-Clustering verwendet?",
        "options": [
            "Manhattan-Distanz",
            "Kosinus-Distanz",
            "Euklidische Distanz",
            "Mahalanobis-Distanz"
        ],
        "correct_index": 2,
        "explanation": "Die euklidische Distanz wird standardmäßig im k-Means-Algorithmus verwendet, da sie die kürzeste gerade Linie zwischen zwei Punkten misst."
    },
    {
        "question": "Welche Methode wird verwendet, um die optimale Anzahl von Clustern für das k-Means-Verfahren zu bestimmen?",
        "options": [
            "Elbow-Methode",
            "Silhouette-Analyse",
            "Gap-Statistik",
            "Alle der oben genannten"
        ],
        "correct_index": 3,
        "explanation": "Elbow-Methode, Silhouette-Analyse und Gap-Statistik sind gängige Methoden zur Bestimmung der optimalen Clusteranzahl."
    },
    {
        "question": "Was beschreibt der Silhouette-Score in einem Clustering-Ergebnis?",
        "options": [
            "Die Distanz zwischen den Clustern",
            "Die Stabilität der Clusterzentren",
            "Die Konsistenz innerhalb eines Clusters und die Distanz zu anderen Clustern",
            "Die Anzahl der Cluster"
        ],
        "correct_index": 2,
        "explanation": "Der Silhouette-Score misst, wie gut die Datenpunkte zu ihren Clustern passen, verglichen mit den nächsten Clustern."
    },
    {
        "question": "Welches Clustering-Verfahren nutzt die Methode der agglomerativen und divisiven Strategien?",
        "options": [
            "k-Means-Clustering",
            "Dichtebasiertes Clustering (DBSCAN)",
            "Hierarchisches Clustering",
            "Fuzzy C-Means Clustering"
        ],
        "correct_index": 2,
        "explanation": "Das hierarchische Clustering kann entweder durch Agglomeration (Bottom-up) oder Division (Top-down) durchgeführt werden."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf das k-Means-Clustering zu?",
        "options": [
            "Es bildet Cluster mit beliebiger Form und Dichte.",
            "Es teilt die Daten in nicht-überlappende Gruppen mit fixer Anzahl Gruppen.",
            "Es benötigt keine Initialisierung der Clusterzentren.",
            "Es ist für hierarchische Clusterstrukturen geeignet."
        ],
        "correct_index": 1,
        "explanation": "k-Means erstellt nicht-überlappende Cluster mit einer festgelegten Anzahl."
    },
    {
        "question": "Welche Metrik wird in der Gap-Statistik verwendet, um die Clusterqualität zu messen?",
        "options": [
            "Euklidische Distanz",
            "Die Differenz der Cluster-Silhouette",
            "Der Abstand zwischen der Daten-Verteilung und einer Referenz-Verteilung",
            "Die Summe der quadratischen Abweichungen"
        ],
        "correct_index": 2,
        "explanation": "Die Gap-Statistik vergleicht die Clusterstruktur der Daten mit einer zufälligen Referenzverteilung."
    },
    {
        "question": "Welches Ziel hat das k-Means-Verfahren?",
        "options": [
            "Minimierung der durchschnittlichen Distanz zwischen Punkten und Cluster-Zentren",
            "Maximierung der Anzahl der Cluster",
            "Minimierung der Anzahl der Cluster",
            "Maximierung der Varianz innerhalb der Cluster"
        ],
        "correct_index": 0,
        "explanation": "k-Means minimiert die Summe der quadratischen Abweichungen innerhalb der Cluster."
    },
    {
        "question": "Welche der folgenden Aussagen über die Elbow-Methode ist richtig?",
        "options": [
            "Sie zeigt den optimalen Punkt an, bei dem die Distanz zwischen Clustern maximal ist.",
            "Sie zeigt den Punkt, an dem die Reduktion der Gesamtvarianz stabilisiert.",
            "Sie ist besonders effektiv für hierarchisches Clustering.",
            "Sie zeigt den Punkt an, an dem die Clustergröße minimal ist."
        ],
        "correct_index": 1,
        "explanation": "Die Elbow-Methode identifiziert den Punkt, an dem die Varianzreduktion nachlässt, als optimal."
    },
    {
        "question": "In welchem Szenario ist das hierarchische Clustering besonders nützlich?",
        "options": [
            "Wenn die Clusteranzahl bekannt ist",
            "Wenn es eine natürliche Hierarchie in den Daten gibt",
            "Wenn die Daten stark überlappen",
            "Wenn nur wenige Datenpunkte vorhanden sind"
        ],
        "correct_index": 1,
        "explanation": "Hierarchisches Clustering eignet sich für Daten mit natürlicher Hierarchie."
    },
    {
        "question": "Was versteht man unter der Manhattan-Distanz?",
        "options": [
            "Die direkte Luftlinie zwischen zwei Punkten",
            "Die Summe der absoluten Differenzen entlang jeder Dimension",
            "Die Quadratwurzel der Summe der quadrierten Differenzen entlang jeder Dimension",
            "Die Differenz der Standardabweichungen der Punkte"
        ],
        "correct_index": 1,
        "explanation": "Die Manhattan-Distanz misst die Distanz entlang der Achsen."
    },
    {
        "question": "Welche Aussage trifft auf die Kosinus-Distanz zu?",
        "options": [
            "Sie misst die Ähnlichkeit zweier Vektoren basierend auf ihrem Winkel.",
            "Sie berücksichtigt ausschließlich den Betrag eines Vektors.",
            "Sie verwendet quadratische Abstände zwischen Punkten.",
            "Sie ist immer kleiner als die Euklidische Distanz."
        ],
        "correct_index": 0,
        "explanation": "Die Kosinus-Distanz misst den Winkel zwischen Vektoren, nicht die absolute Entfernung."
    },
    {
        "question": "Was ist eine Hauptbeschränkung des k-Means-Algorithmus?",
        "options": [
            "Er ist langsam bei kleinen Datensätzen.",
            "Er kann nur Cluster mit kreisförmigen Formen finden.",
            "Er kann keine überlappenden Cluster erkennen.",
            "Er erfordert eine hierarchische Struktur."
        ],
        "correct_index": 1,
        "explanation": "Der k-Means-Algorithmus funktioniert am besten bei kugelförmigen Clustern und hat Schwierigkeiten bei komplexeren Formen."
    },
    {
        "question": "Wie funktioniert die agglomerative Methode im hierarchischen Clustering?",
        "options": [
            "Es beginnt mit einem Cluster und trennt Datenpunkte schrittweise.",
            "Es beginnt mit allen Datenpunkten als Einzelcluster und fusioniert sie iterativ.",
            "Es berechnet die Summe aller Distanzen.",
            "Es maximiert die Varianz innerhalb der Cluster."
        ],
        "correct_index": 1,
        "explanation": "Bei der agglomerativen Methode starten alle Datenpunkte als Einzelcluster und werden sukzessive zusammengeführt."
    },
    {
        "question": "Was versteht man unter einem Dendrogramm?",
        "options": [
            "Ein Modell, das die Regressionslinie zeigt.",
            "Eine visuelle Darstellung hierarchischer Clusterstruktur.",
            "Ein Diagramm zur Messung von Datenpunkten.",
            "Ein Algorithmus zur Berechnung der Cluster."
        ],
        "correct_index": 1,
        "explanation": "Ein Dendrogramm zeigt die hierarchische Struktur der Cluster und die Reihenfolge ihrer Fusionen."
    },
    {
        "question": "Warum wird der Silhouette-Score verwendet?",
        "options": [
            "Um die beste Clusteranzahl für hierarchisches Clustering zu wählen.",
            "Um die Kompaktheit und Trennbarkeit von Clustern zu bewerten.",
            "Um Cluster überlappend zu machen.",
            "Um die Distanzmetriken zu analysieren."
        ],
        "correct_index": 1,
        "explanation": "Der Silhouette-Score bewertet, wie gut die Datenpunkte zu ihren Clustern passen."
    },
    {
        "question": "Was ist das Ziel des Optimierungsprozesses im Clustering?",
        "options": [
            "Maximierung der Clusteranzahl.",
            "Minimierung der Clusteranzahl.",
            "Maximierung der Distanz zu den Cluster-Zentren.",
            "Minimierung der Variabilität innerhalb der Cluster."
        ],
        "correct_index": 3,
        "explanation": "Das Ziel ist es, Cluster zu erstellen, die intern kohäsiv und extern gut getrennt sind."
    },
    {
        "question": "Welche Rolle spielt die Initialisierung der Cluster-Zentren im k-Means-Algorithmus?",
        "options": [
            "Sie hat keinen Einfluss auf das Ergebnis.",
            "Sie beeinflusst die Geschwindigkeit der Konvergenz und die Qualität des Endergebnisses.",
            "Sie wird nur für die erste Iteration verwendet.",
            "Sie beeinflusst die Wahl der Distanzmethode."
        ],
        "correct_index": 1,
        "explanation": "Die Wahl der initialen Cluster-Zentren kann das Endergebnis und die Konvergenz des k-Means-Algorithmus stark beeinflussen."
    },
    {
        "question": "Welches Problem kann auftreten, wenn die Anzahl der Cluster in k-Means zu groß gewählt wird?",
        "options": [
            "Das Modell wird zu komplex und schwer interpretierbar.",
            "Die Datenpunkte überlappen vollständig.",
            "Die Cluster werden zu homogen.",
            "Es gibt keine Auswirkungen."
        ],
        "correct_index": 0,
        "explanation": "Zu viele Cluster führen zu einem komplexeren Modell, das schwer zu interpretieren ist."
    },
    {
        "question": "Was bedeutet ein Silhouette-Score nahe bei eins?",
        "options": [
            "Die Beobachtung gehört dem richtigen Cluster an.",
            "Die Clusterzentren liegen nah beieinander.",
            "Die Beobachtung liegt im falschen Cluster.",
            "Die Beobachtung liegt zwischen zwei Clustern."
        ],
        "correct_index": 0,
        "explanation": "Ein hoher Silhouette-Score zeigt, dass ein Datenpunkt gut in seinem Cluster integriert ist und weit von anderen Clustern entfernt liegt."
    },
    {
        "question": "Welche der folgenden Aussagen trifft auf die Ward-Methode im hierarchischen Clustering zu?",
        "options": [
            "Sie minimiert die Summe der quadrierten Abweichungen zu den Clusterzentren.",
            "Sie maximiert die Anzahl der Cluster.",
            "Sie ordnet Daten nach ihrer Ähnlichkeit in einen Cluster.",
            "Sie basiert ausschließlich auf der Manhattan-Distanz."
        ],
        "correct_index": 0,
        "explanation": "Die Ward-Methode minimiert die Varianz innerhalb der Cluster."
    },
    {
        "question": "Warum wird die Gap-Statistik häufig gegenüber der Elbow-Methode bevorzugt?",
        "options": [
            "Sie bietet eine genauere visuelle Darstellung der Clusterqualität.",
            "Sie ist einfacher zu berechnen.",
            "Sie basiert auf einem Vergleich der Clusterstruktur mit zufälligen Daten.",
            "Sie benötigt keine Distanzmetriken."
        ],
        "correct_index": 2,
        "explanation": "Die Gap-Statistik vergleicht die Clusterstruktur mit zufälligen Daten, was sie robuster macht."
    },
    {
        "question": "Welcher Clustering-Algorithmus ist geeignet für Daten mit unterschiedlicher Dichte und Form der Cluster?",
        "options": [
            "k-Means",
            "Hierarchisches Clustering",
            "DBSCAN",
            "Ward’s Methode"
        ],
        "correct_index": 2,
        "explanation": "DBSCAN erkennt Cluster beliebiger Form und Dichte und ist robust gegenüber Ausreißern."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
