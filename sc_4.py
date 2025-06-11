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
        "question": "Was beschreibt die 'objektive' Datenqualität?",
        "options": [
            "Die persönliche Meinung des Datennutzers über die Daten.",
            "Die messbare Genauigkeit, Vollständigkeit und Konsistenz der Daten.",
            "Die Möglichkeit, die Daten für unterschiedliche Zwecke zu interpretieren.",
            "Die Bewertung der Daten durch Experten in einem bestimmten Bereich."
        ],
        "correct_index": 1,
        "explanation": "Objektive Datenqualität bezieht sich auf messbare Eigenschaften wie Genauigkeit, Vollständigkeit und Konsistenz."
    },
    {
        "question": "Welche der folgenden Aspekte betrifft die 'subjektive' Datenqualität?",
        "options": [
            "Die Reproduzierbarkeit von Ergebnissen.",
            "Die Meinung der Nutzer, ob die Daten für ihre Zwecke geeignet sind.",
            "Die Anzahl fehlender Datenpunkte.",
            "Die Genauigkeit der Messungen."
        ],
        "correct_index": 1,
        "explanation": "Subjektive Datenqualität hängt von der Einschätzung der Nutzer ab, ob die Daten ihren spezifischen Anforderungen entsprechen."
    },
    {
        "question": "Wie kann die 'Vollständigkeit' von Daten in Bezug auf die objektive Datenqualität am besten beschrieben werden?",
        "options": [
            "Die Genauigkeit der erfassten Daten.",
            "Der Grad, in dem alle erwarteten Daten verfügbar sind.",
            "Die Fähigkeit, die Daten ohne Fehler zu interpretieren.",
            "Die Subjektivität der Datenbewertung durch den Nutzer."
        ],
        "correct_index": 1,
        "explanation": "Vollständigkeit beschreibt, ob alle erforderlichen Datenpunkte vorhanden sind."
    },
    {
        "question": "Welche der folgenden Aussagen beschreibt am besten den subjektiven Aspekt der Datenqualität?",
        "options": [
            "Daten sind konsistent, wenn sie in allen Datensätzen die gleichen Werte haben.",
            "Die Daten wurden präzise und ohne Fehler gemessen.",
            "Der Nutzer empfindet die Daten als nützlich und vertrauenswürdig für seinen spezifischen Zweck.",
            "Alle Datenfelder enthalten die erforderlichen Informationen."
        ],
        "correct_index": 2,
        "explanation": "Subjektive Qualität spiegelt die Einschätzung der Nützlichkeit und Vertrauenswürdigkeit der Daten wider."
    },
    {
        "question": "Ein Nutzer beschwert sich, dass die Daten für seine Analyse unbrauchbar sind, obwohl sie technisch korrekt sind. Welcher Aspekt der Datenqualität wird hier kritisiert?",
        "options": [
            "Genauigkeit",
            "Subjektive Qualität",
            "Vollständigkeit",
            "Objektive Qualität"
        ],
        "correct_index": 1,
        "explanation": "Dies betrifft die subjektive Datenqualität, da die Daten für den Nutzer nicht nützlich erscheinen, obwohl sie korrekt sind."
    },
    {
        "question": "Welche der folgenden Aussagen ist ein Beispiel für eine objektive Datenqualitätsprüfung?",
        "options": [
            "Die Daten sind für die Analyse meiner Forschung geeignet.",
            "Ich habe das Gefühl, dass die Daten nützlich sind.",
            "Ich kann die Daten in meinem speziellen Kontext gut nutzen.",
            "Die Daten enthalten keine fehlerhaften Werte oder Widersprüche."
        ],
        "correct_index": 3,
        "explanation": "Objektive Datenqualität wird durch messbare Kriterien wie Fehlerfreiheit oder Konsistenz geprüft."
    },
    {
        "question": "Wie kann die Genauigkeit von Daten als Teil der objektiven Datenqualität bewertet werden?",
        "options": [
            "Durch das Vertrauen des Nutzers in die Daten.",
            "Durch den Vergleich der Daten mit einer bekannten, wahren Referenz.",
            "Durch die Einschätzung der Nützlichkeit für den aktuellen Anwendungszweck.",
            "Durch den subjektiven Eindruck, den die Daten vermitteln."
        ],
        "correct_index": 1,
        "explanation": "Genauigkeit wird durch den Vergleich mit einer verlässlichen Referenz bewertet."
    },
    {
        "question": "Welcher der folgenden Begriffe bezieht sich auf die subjektive Einschätzung der Datenqualität?",
        "options": [
            "Konsistenz",
            "Genauigkeit",
            "Verlässlichkeit",
            "Relevanz"
        ],
        "correct_index": 3,
        "explanation": "Subjektive Datenqualität umfasst die Einschätzung, wie relevant die Daten für den jeweiligen Zweck sind."
    },
    {
        "question": "Ein Datensatz enthält alle notwendigen Datenpunkte, aber einige der Daten sind falsch oder ungenau. Welche Dimension der Datenqualität wird hier beeinträchtigt?",
        "options": [
            "Vollständigkeit",
            "Konsistenz",
            "Genauigkeit",
            "Objektivität"
        ],
        "correct_index": 2,
        "explanation": "Falsche oder ungenaue Daten beeinträchtigen die Genauigkeit."
    },
    {
        "question": "Ein Datensatz wird von zwei unterschiedlichen Personen verwendet, aber beide bewerten ihn unterschiedlich hinsichtlich seiner Nützlichkeit. Dies ist ein Beispiel für:",
        "options": [
            "Subjektive Datenqualität",
            "Objektive Datenqualität",
            "Vollständigkeit",
            "Konsistenz"
        ],
        "correct_index": 0,
        "explanation": "Die subjektive Datenqualität variiert, da sie auf individuellen Bewertungen basiert."
    },
    {
        "question": "Welche der folgenden Aussagen beschreibt die Konsistenz von Daten?",
        "options": [
            "Alle Datenpunkte stimmen mit einem externen Standard überein.",
            "Die Daten sind für alle Nutzer in ihrem spezifischen Anwendungsfall geeignet.",
            "Die Daten sind innerhalb des Datensatzes einheitlich und enthalten keine widersprüchlichen Informationen.",
            "Der Datensatz enthält alle erwarteten Informationen."
        ],
        "correct_index": 2,
        "explanation": "Konsistenz bedeutet, dass Daten intern widerspruchsfrei sind."
    },
    {
        "question": "Welche der folgenden Maßnahmen kann zur Verbesserung der subjektiven Datenqualität beitragen?",
        "options": [
            "Sicherstellen, dass die Daten korrekt und konsistent sind.",
            "Erheben der Daten in einem standardisierten Format.",
            "Einholen von Nutzerfeedback, um zu verstehen, wie die Daten für ihre Zwecke besser nutzbar sind.",
            "Vermeidung von fehlenden Datenpunkten."
        ],
        "correct_index": 2,
        "explanation": "Nutzerfeedback ist entscheidend, um die subjektive Datenqualität zu verbessern."
    },
    {
        "question": "Welcher der folgenden Begriffe gehört zur objektiven Datenqualität?",
        "options": [
            "Nutzerzufriedenheit",
            "Relevanz",
            "Genauigkeit",
            "Zweckmäßigkeit"
        ],
        "correct_index": 2,
        "explanation": "Genauigkeit ist eine objektiv messbare Eigenschaft der Daten."
    },
    {
        "question": "Wenn ein Datensatz vollständig und korrekt ist, aber von einem Nutzer als irrelevant empfunden wird, welches Datenqualitätsproblem tritt auf?",
        "options": [
            "Ein objektives Problem mit der Vollständigkeit",
            "Ein subjektives Problem mit der Relevanz",
            "Ein objektives Problem mit der Genauigkeit",
            "Ein subjektives Problem mit der Konsistenz"
        ],
        "correct_index": 1,
        "explanation": "Relevanz ist eine subjektive Dimension der Datenqualität, die von der Nützlichkeit für den jeweiligen Zweck abhängt."
    }
]

# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
