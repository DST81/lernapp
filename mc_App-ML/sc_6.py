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
        "question": "Was ist die Nullhypothese (H0) in einem Hypothesentest?",
        "options": [
            "Eine Aussage, die besagt, dass es einen signifikanten Unterschied gibt.",
            "Eine Aussage, die besagt, dass es keinen Unterschied oder Effekt gibt.",
            "Eine Aussage, die die Alternativhypothese unterstützt.",
            "Eine Aussage, die immer abgelehnt wird."
        ],
        "correct_index": 1,
        "explanation": "Die Nullhypothese geht davon aus, dass es keinen Effekt oder Unterschied gibt. Sie wird getestet, um zu entscheiden, ob sie abgelehnt werden kann."
    },
    {
        "question": "Was ist die Alternativhypothese (H1) in einem Hypothesentest?",
        "options": [
            "Die Hypothese, die besagt, dass es keinen Unterschied gibt.",
            "Die Hypothese, die besagt, dass die Nullhypothese wahr ist.",
            "Die Hypothese, die besagt, dass ein Unterschied oder Effekt existiert.",
            "Die Hypothese, die immer akzeptiert wird."
        ],
        "correct_index": 2,
        "explanation": "Die Alternativhypothese beschreibt den Unterschied oder Effekt, den man beweisen möchte."
    },
    {
        "question": "Was beschreibt der p-Wert in einem Hypothesentest?",
        "options": [
            "Die Wahrscheinlichkeit, dass die Nullhypothese wahr ist.",
            "Die Wahrscheinlichkeit, dass die beobachteten Daten unter der Annahme der Nullhypothese tatsächlich echt sind.",
            "Die Wahrscheinlichkeit, dass die Alternativhypothese wahr ist.",
            "Den Unterschied zwischen den Mittelwerten zweier Gruppen."
        ],
        "correct_index": 1,
        "explanation": "Der p-Wert gibt an, wie wahrscheinlich die beobachteten Daten sind, wenn die Nullhypothese wahr ist."
    },
    {
        "question": "Welches Signifikanzniveau (α) wird oft als Standard verwendet, um die Nullhypothese zu testen?",
        "options": ["0.02", "0.05", "0.10", "0.50"],
        "correct_index": 1,
        "explanation": "Ein Signifikanzniveau von 0.05 ist der gängige Standard, um die Nullhypothese zu testen."
    },
    {
        "question": "Wenn der p-Wert kleiner als α (das Signifikanzniveau) ist, dann:",
        "options": [
            "Akzeptieren wir die Nullhypothese.",
            "Lehnen wir die Nullhypothese ab.",
            "Akzeptieren wir die Alternativhypothese.",
            "Der Test ist ungültig."
        ],
        "correct_index": 1,
        "explanation": "Wenn der p-Wert kleiner als das Signifikanzniveau ist, gibt es genügend Beweise, um die Nullhypothese abzulehnen."
    },
    {
        "question": "Der t-Test wird typischerweise verwendet, um:",
        "options": [
            "Den Zusammenhang zwischen zwei kategorialen Variablen zu testen.",
            "Mehr als zwei Mittelwerte zu vergleichen.",
            "Die Mittelwerte zweier Gruppen zu vergleichen.",
            "Die Varianz innerhalb einer Gruppe zu testen."
        ],
        "correct_index": 2,
        "explanation": "Der t-Test wird verwendet, um Unterschiede zwischen den Mittelwerten zweier Gruppen zu untersuchen."
    },
    {
        "question": "Welcher der folgenden Hypothesentests wird verwendet, um Unterschiede zwischen den Mittelwerten von mehr als zwei Gruppen zu testen?",
        "options": ["ANOVA", "t-Test", "Chi-Quadrat-Test", "Z-Test"],
        "correct_index": 0,
        "explanation": "ANOVA (Analyse der Varianz) wird verwendet, um Unterschiede zwischen Mittelwerten von mehr als zwei Gruppen zu analysieren."
    },
    {
        "question": "Welcher der folgenden Tests wird verwendet, um zu überprüfen, ob zwei kategoriale Variablen unabhängig sind?",
        "options": ["t-Test", "ANOVA", "Chi-Quadrat-Test", "Z-Test"],
        "correct_index": 2,
        "explanation": "Der Chi-Quadrat-Test prüft die Unabhängigkeit zwischen zwei kategorialen Variablen."
    },
    {
        "question": "Wenn der F-Wert in einer ANOVA groß ist und der p-Wert klein, dann:",
        "options": [
            "Gibt es keinen signifikanten Unterschied zwischen den Gruppen.",
            "Gibt es einen signifikanten Unterschied zwischen mindestens zwei Gruppen.",
            "Ist die Nullhypothese korrekt.",
            "Sind die Daten fehlerhaft."
        ],
        "correct_index": 1,
        "explanation": "Ein großer F-Wert und ein kleiner p-Wert deuten darauf hin, dass mindestens zwei Gruppen signifikant unterschiedlich sind."
    },
    {
        "question": "Der t-Test wird verwendet, wenn:",
        "options": [
            "Es einen Zusammenhang zwischen zwei kategorialen Variablen gibt.",
            "Die Stichproben aus der gleichen Population stammen.",
            "Zwei unabhängige Gruppen verglichen werden.",
            "Mehr als zwei Mittelwerte verglichen werden."
        ],
        "correct_index": 2,
        "explanation": "Der t-Test wird eingesetzt, um die Mittelwerte von zwei unabhängigen Gruppen zu vergleichen."
    },
    {
        "question": "Was ist der Zweck der Teststatistik in einem Hypothesentest?",
        "options": [
            "Sie bestimmt das Signifikanzniveau.",
            "Sie hilft, den p-Wert zu berechnen.",
            "Sie gibt den wahren Wert der Parameter an.",
            "Sie beschreibt die Dimension der Daten."
        ],
        "correct_index": 1,
        "explanation": "Die Teststatistik ist die Grundlage für die Berechnung des p-Werts und den Vergleich mit der Nullhypothese."
    },
    {
        "question": "Der Chi-Quadrat-Test eignet sich am besten für:",
        "options": [
            "Den Vergleich von Mittelwerten kontinuierlicher Daten.",
            "Den Vergleich von Proportionen zwischen Kategorien.",
            "Den Vergleich von Varianzen zwischen mehreren Gruppen.",
            "Den Vergleich von Verteilungen kontinuierlicher Daten."
        ],
        "correct_index": 1,
        "explanation": "Der Chi-Quadrat-Test vergleicht die Häufigkeiten oder Proportionen zwischen Kategorien."
    },
    {
        "question": "Welcher der folgenden Werte ist KEINE Voraussetzung für die Durchführung eines t-Tests?",
        "options": [
            "Normalverteilung der Daten.",
            "Unabhängigkeit der Stichproben.",
            "Homogenität der Varianzen.",
            "Mindestens drei Gruppen."
        ],
        "correct_index": 3,
        "explanation": "Ein t-Test wird nur für zwei Gruppen verwendet, nicht für drei oder mehr."
    },
    {
        "question": "Welche Aussage beschreibt den Unterschied zwischen einem einseitigen und einem zweiseitigen t-Test?",
        "options": [
            "Ein einseitiger Test prüft, ob es Unterschiede in eine bestimmte Richtung gibt, während ein zweiseitiger Test in beide Richtungen prüft.",
            "Ein einseitiger Test erfordert zwei Gruppen, ein zweiseitiger Test nicht.",
            "Ein zweiseitiger Test hat immer einen höheren p-Wert als ein einseitiger Test.",
            "Ein einseitiger Test ist nur bei nominalen Daten anwendbar."
        ],
        "correct_index": 0,
        "explanation": "Ein einseitiger Test prüft Unterschiede in einer Richtung, während ein zweiseitiger Test beide Richtungen berücksichtigt."
    },
    {
        "question": "Bei einem F-Test (ANOVA) bedeutet ein großer F-Wert in der Regel:",
        "options": [
            "Die Varianz zwischen den Gruppen ist klein.",
            "Es gibt keinen signifikanten Unterschied zwischen den Gruppen.",
            "Die Varianz zwischen den Gruppen ist größer als die Varianz innerhalb der Gruppen.",
            "Der p-Wert ist hoch."
        ],
        "correct_index": 2,
        "explanation": "Ein großer F-Wert zeigt an, dass die Gruppenunterschiede größer sind als die Varianz innerhalb der Gruppen."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
