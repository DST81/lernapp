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
        "question": "Welche der folgenden Aussagen beschreibt die Lokalisierung bzw. zentrale Tendenz der Daten in der Statistik korrekt?",
        "options": [
            "Die Verteilung der Datenpunkte über eine Skala hinweg.",
            "Die Streuung der Daten um einen zentralen Wert.",
            "Der Punkt, an dem die meisten Datenpunkte konzentriert sind.",
            "Die Abweichungen einzelner Datenpunkte vom Mittelwert."
        ],
        "correct_index": 2,
        "explanation": "Die zentrale Tendenz beschreibt den Punkt, an dem die meisten Datenwerte konzentriert sind, z. B. durch Mittelwert, Median oder Modus."
    },
    {
        "question": "Welcher der folgenden Werte beschreibt nicht die Lokalisierung?",
        "options": [
            "Median",
            "Modus",
            "Standardabweichung",
            "Mittelwert"
        ],
        "correct_index": 2,
        "explanation": "Die Standardabweichung misst die Streuung der Daten, nicht die zentrale Tendenz."
    },
    {
        "question": "Wie wird die Streuung der Daten in einem Boxplot dargestellt?",
        "options": [
            "Durch den Abstand zwischen dem oberen Quartil und den Extremwerten.",
            "Durch die Länge der Whiskers.",
            "Durch den Abstand zwischen dem oberen und unteren Quartil.",
            "Durch den Abstand zwischen dem Median und den Extremwerten."
        ],
        "correct_index": 2,
        "explanation": "Die Streuung wird im Boxplot durch den Interquartilsabstand (IQR) zwischen erstem und drittem Quartil dargestellt."
    },
    {
        "question": "Ein Ausreißer in einem Datensatz wird erkannt, wenn er um welchen Faktor über den Interquartilsabstand (IQR) hinausgeht?",
        "options": [
            "0.5",
            "1.0",
            "1.5",
            "2.0"
        ],
        "correct_index": 2,
        "explanation": "Ein Ausreißer liegt vor, wenn er mehr als 1.5 IQR über dem oberen oder unter dem unteren Quartil liegt."
    },
    {
        "question": "Welche Form hat ein Histogramm normalerweise, wenn die Daten normalverteilt sind?",
        "options": [
            "Symmetrisch und glockenförmig.",
            "Schief nach rechts.",
            "Schief nach links.",
            "U-förmig."
        ],
        "correct_index": 0,
        "explanation": "Eine Normalverteilung erzeugt eine symmetrische, glockenförmige Kurve."
    },
    {
        "question": "Welcher der folgenden Werte misst die Streuung bei symmetrischen Beobachtungen einer Variable?",
        "options": [
            "Modus",
            "Median",
            "Interquartile",
            "Standardabweichung"
        ],
        "correct_index": 3,
        "explanation": "Die Standardabweichung ist ein Standardmaß für die Streuung bei symmetrischen Daten."
    },
    {
        "question": "In welchem Fall kann eine der vier primären Eigenschaften nicht berechnet werden?",
        "options": [
            "Bei der Analyse von kontinuierlichen Variablen.",
            "Bei der Berechnung der Interquartile.",
            "Bei der Berechnung des Mittelwertes.",
            "Bei der Analyse von kategorischen Variablen."
        ],
        "correct_index": 3,
        "explanation": "Für kategoriale Variablen können keine numerischen Maße wie Mittelwert oder Standardabweichung berechnet werden."
    },
    {
        "question": "Was beschreibt die Standardabweichung eines Datensatzes?",
        "options": [
            "Den durchschnittlichen Abstand der Datenwerte vom Mittelwert.",
            "Den Mittelwert der Daten.",
            "Den häufigsten Wert in den Daten.",
            "Die Verteilung der Extremwerte."
        ],
        "correct_index": 0,
        "explanation": "Die Standardabweichung gibt den durchschnittlichen Abstand der Werte vom Mittelwert an."
    },
    {
        "question": "Welche Wahrscheinlichkeitsverteilung eignet sich besonders gut zur Modellierung von Ereignissen mit zwei möglichen Ausgängen?",
        "options": [
            "Normalverteilung",
            "Binomialverteilung",
            "Poissonverteilung",
            "Exponentialverteilung"
        ],
        "correct_index": 1,
        "explanation": "Die Binomialverteilung modelliert Ereignisse mit zwei möglichen Ergebnissen, z. B. Erfolg oder Misserfolg."
    },
    {
        "question": "Welcher der folgenden Werte misst die Lokalisierung bei symmetrischen Beobachtungen einer Variable?",
        "options": [
            "Mittelwert",
            "Median",
            "Interquartile",
            "Standardabweichung"
        ],
        "correct_index": 0,
        "explanation": "Der Mittelwert ist das Maß für die zentrale Tendenz bei symmetrischen Daten."
    },
    {
        "question": "Welcher der folgenden Werte misst die Streuung bei schiefen Beobachtungen einer Variable?",
        "options": [
            "Modus",
            "Median",
            "Interquartile",
            "Standardabweichung"
        ],
        "correct_index": 2,
        "explanation": "Der Interquartilsabstand (IQR) ist robust gegenüber Ausreißern und geeignet für schiefe Daten."
    },
    {
        "question": "Welche der folgenden Verteilungen wird oft verwendet, um die Wahrscheinlichkeiten diskreter Ereignisse zu modellieren, die nur diskrete Werte wie 1, 2, 3, ... annehmen?",
        "options": [
            "Normalverteilung",
            "Binomialverteilung",
            "Poissonverteilung",
            "Exponentialverteilung"
        ],
        "correct_index": 2,
        "explanation": "Die Poissonverteilung wird für diskrete Ereignisse wie die Anzahl von E-Mails pro Stunde verwendet."
    },
    {
        "question": "Welcher der folgenden Werte misst die Lokalisierung bei schiefen Beobachtungen einer Variable?",
        "options": [
            "Mittelwert",
            "Median",
            "Interquartile",
            "Standardabweichung"
        ],
        "correct_index": 1,
        "explanation": "Der Median wird oft für schiefe Daten genutzt, da er weniger empfindlich gegenüber Ausreißern ist."
    },
    {
        "question": "Welche der folgenden Verteilungen wird oft verwendet, um die Wahrscheinlichkeiten kontinuierlicher Ereignisse zu modellieren?",
        "options": [
            "Normalverteilung",
            "Binomialverteilung",
            "Poissonverteilung",
            "Exponentialverteilung"
        ],
        "correct_index": 0,
        "explanation": "Die Normalverteilung ist die am häufigsten verwendete Verteilung für kontinuierliche Variablen."
    },
    {
        "question": "Welcher der folgenden Werte misst die Lokalisierung bei kategorialen Variablen eines Datensatzes?",
        "options": [
            "Median",
            "Modus",
            "Interquartile",
            "Standardabweichung"
        ],
        "correct_index": 1,
        "explanation": "Der Modus gibt den häufigsten Wert einer kategorialen Variable an."
    },
    {
        "question": "Ein Histogramm zeigt eine stark linksschiefe Verteilung. Welcher der folgenden Aussagen ist dann wahrscheinlich korrekt?",
        "options": [
            "Der Mittelwert ist größer als der Median.",
            "Der Mittelwert ist kleiner als der Median.",
            "Der Median ist größer als der Modus.",
            "Der Modus ist kleiner als der Mittelwert."
        ],
        "correct_index": 1,
        "explanation": "Bei einer linksschiefen Verteilung liegt der Mittelwert links vom Median."
    },
    {
        "question": "Was misst der Interquartilsabstand (IQR) in einem Datensatz?",
        "options": [
            "Den Abstand zwischen dem Mittelwert und den Extremwerten.",
            "Die Differenz zwischen dem ersten und dem dritten Quartil.",
            "Den durchschnittlichen Abstand der Datenwerte vom Median.",
            "Die Differenz zwischen dem Median und dem Mittelwert."
        ],
        "correct_index": 1,
        "explanation": "Der IQR misst die mittlere Streuung der zentralen 50 % der Daten."
    },
    {
        "question": "Welches der folgenden Diagramme wird typischerweise verwendet, um die Verteilung von Daten visuell zu veranschaulichen?",
        "options": [
            "Balkendiagramm",
            "Boxplot",
            "Punktdiagramm",
            "Tortendiagramm"
        ],
        "correct_index": 1,
        "explanation": "Ein Boxplot zeigt die Verteilung und mögliche Ausreißer eines Datensatzes."
    },
    {
        "question": "Welcher Wert ist der Median eines Datensatzes?",
        "options": [
            "Der häufigste Wert.",
            "Der Mittelwert der größten und kleinsten Werte.",
            "Der mittlere Wert, wenn die Daten der Größe nach geordnet sind.",
            "Der Punkt mit der größten Streuung."
        ],
        "correct_index": 2,
        "explanation": "Der Median ist der zentrale Wert, wenn die Daten geordnet sind."
    },
    {
        "question": "Ein Histogramm zeigt eine Verteilung, wo die meisten Beobachtungen kleine Werte aufzeigen und wenige große Werte vorhanden sind. Welcher der folgenden Werte beschreibt diese Verteilung am besten?",
        "options": [
            "Symmetrisch",
            "Schief nach rechts",
            "Schief nach links",
            "U-förmig"
        ],
        "correct_index": 1,
        "explanation": "Eine rechtsschiefe Verteilung hat wenige große Werte und viele kleine Werte."
    },
    {
        "question": "Welche der folgenden Statistiken ist am besten geeignet, um den Einfluss von Ausreißern zu minimieren?",
        "options": [
            "Mittelwert",
            "Median",
            "Standardabweichung",
            "Modus"
        ],
        "correct_index": 1,
        "explanation": "Der Median ist robust gegenüber Ausreißern und wird deshalb in solchen Fällen bevorzugt."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
