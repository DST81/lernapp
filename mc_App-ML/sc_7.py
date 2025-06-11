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
        "question": "Was ist der erste Fehler (α-Fehler) in der statistischen Hypothesenprüfung?",
        "options": [
            "Die Wahrscheinlichkeit, die Nullhypothese fälschlicherweise zu akzeptieren.",
            "Die Wahrscheinlichkeit, die Nullhypothese fälschlicherweise abzulehnen.",
            "Die Wahrscheinlichkeit, die Alternativhypothese fälschlicherweise zu akzeptieren.",
            "Die Wahrscheinlichkeit, die Alternativhypothese fälschlicherweise abzulehnen."
        ],
        "correct_index": 1,
        "explanation": "Der α-Fehler tritt auf, wenn die Nullhypothese abgelehnt wird, obwohl sie wahr ist."
    },
    {
        "question": "Was ist der zweite Fehler (β-Fehler) in der statistischen Hypothesenprüfung?",
        "options": [
            "Die Wahrscheinlichkeit, die Nullhypothese fälschlicherweise zu akzeptieren.",
            "Die Wahrscheinlichkeit, die Nullhypothese fälschlicherweise abzulehnen.",
            "Die Wahrscheinlichkeit, die Alternativhypothese fälschlicherweise abzulehnen.",
            "Die Wahrscheinlichkeit, die Alternativhypothese fälschlicherweise zu akzeptieren."
        ],
        "correct_index": 0,
        "explanation": "Der β-Fehler tritt auf, wenn die Nullhypothese akzeptiert wird, obwohl sie falsch ist."
    },
    {
        "question": "Was beschreibt die statistische Power eines Tests?",
        "options": [
            "Die Wahrscheinlichkeit, den ersten Fehler zu begehen.",
            "Die Wahrscheinlichkeit, den zweiten Fehler zu begehen.",
            "Die Wahrscheinlichkeit, die Nullhypothese korrekt abzulehnen, wenn sie falsch ist.",
            "Die Wahrscheinlichkeit, die Alternativhypothese korrekt abzulehnen."
        ],
        "correct_index": 2,
        "explanation": "Die Power eines Tests misst die Fähigkeit, einen tatsächlich vorhandenen Effekt zu erkennen."
    },
    {
        "question": "Was bedeutet es, wenn die Power eines Tests 0,8 ist?",
        "options": [
            "Es besteht eine 80% Chance, die Nullhypothese korrekt abzulehnen.",
            "Es besteht eine 80% Chance, den ersten Fehler zu vermeiden.",
            "Es besteht eine 80% Chance, den zweiten Fehler zu begehen.",
            "Es besteht eine 20% Chance, die Nullhypothese korrekt abzulehnen."
        ],
        "correct_index": 0,
        "explanation": "Eine Power von 0,8 bedeutet, dass der Test eine 80%ige Wahrscheinlichkeit hat, einen Effekt zu erkennen, falls die Nullhypothese falsch ist."
    },
    {
        "question": "Wofür wird ein Q-Q-Plot verwendet?",
        "options": [
            "Um die Homogenität der Varianz zu überprüfen.",
            "Um die Normalverteilung von Daten zu überprüfen.",
            "Um die Korrelation zwischen zwei Variablen zu überprüfen.",
            "Um die Größe des Effekts in einem Experiment zu bestimmen."
        ],
        "correct_index": 1,
        "explanation": "Ein Q-Q-Plot überprüft die Übereinstimmung der Daten mit einer Normalverteilung."
    },
    {
        "question": "Was zeigt ein linearer Q-Q-Plot an?",
        "options": [
            "Eine perfekte Normalverteilung.",
            "Eine Abweichung von der Normalverteilung.",
            "Eine Homoskedastizität der Varianz.",
            "Eine Heteroskedastizität der Varianz."
        ],
        "correct_index": 0,
        "explanation": "Liegen die Punkte eines Q-Q-Plots auf einer Linie, deutet dies auf eine Normalverteilung hin."
    },
    {
        "question": "Was zeigt eine signifikante Abweichung von der Diagonalen in einem Q-Q-Plot an?",
        "options": [
            "Eine hohe Korrelation zwischen den Daten.",
            "Eine Abweichung von der Normalverteilung.",
            "Eine hohe Varianz innerhalb der Daten.",
            "Eine Abweichung vom Mittelwert."
        ],
        "correct_index": 1,
        "explanation": "Abweichungen von der Diagonalen zeigen, dass die Daten keine Normalverteilung aufweisen."
    },
    {
        "question": "Was testet der Levene-Test?",
        "options": [
            "Die Normalverteilung der Daten.",
            "Die Gleichheit der Varianzen (Homoskedastizität).",
            "Die Abweichung vom Mittelwert.",
            "Die Korrelation zwischen zwei Variablen."
        ],
        "correct_index": 1,
        "explanation": "Der Levene-Test prüft, ob die Varianzen in verschiedenen Gruppen gleich sind."
    },
    {
        "question": "Was ist die Nullhypothese des Levene-Tests?",
        "options": [
            "Die Mittelwerte der Gruppen sind gleich.",
            "Die Varianzen der Gruppen sind gleich.",
            "Die Daten sind normalverteilt.",
            "Die Daten sind unkorreliert."
        ],
        "correct_index": 1,
        "explanation": "Die Nullhypothese des Levene-Tests lautet, dass die Varianzen der Gruppen gleich sind."
    },
    {
        "question": "Wenn der Levene-Test signifikant ist, was bedeutet das?",
        "options": [
            "Die Varianzen der Gruppen sind gleich.",
            "Die Varianzen der Gruppen sind ungleich.",
            "Die Mittelwerte der Gruppen sind gleich.",
            "Die Mittelwerte der Gruppen sind ungleich."
        ],
        "correct_index": 1,
        "explanation": "Ein signifikanter Levene-Test weist darauf hin, dass die Gruppenvarianzen unterschiedlich sind."
    },
    {
        "question": "Welcher Test ist eine Alternative zum Levene-Test, wenn die Normalverteilung der Daten nicht gewährleistet ist?",
        "options": [
            "Bartlett-Test.",
            "T-Test.",
            "Kolmogorov-Smirnov-Test.",
            "ANOVA-Test."
        ],
        "correct_index": 0,
        "explanation": "Der Bartlett-Test ist eine Alternative zum Levene-Test, wenn die Normalverteilung nicht erfüllt ist."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
