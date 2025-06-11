import random

class LernApp:
    def __init__(self, questions):
        self.all_questions = questions
        self.score = 0

    def start(self):
        print("Willkommen zur Single-Choice-Lern-App!\n")
        input("Drücke Enter, um zu starten...\n")

        #Anzahl Fragen abfragen
        max_fragen= len(self.all_questions)
        while True:
            try:
                anzahl= int(input(f'Wieviele Fragen möchtest du beantworten?(1-{max_fragen}:)'))
                if 1 <=anzahl <= max_fragen:
                    break
                else:
                    print(f'Bitte gib eine Zahl zwischen 1 und {max_fragen} ein. ')
            except ValueError:
                print('Ungültie Eingabe. Bitte eine ganze Zahl eingeben')

        #Fragen zufällig auswählen:
        self.questions =random.sample(self.all_questions, anzahl)
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
            "question": "Welcher Satz beschreibt den Hauptunterschied zwischen Dense- und Convolutional-Schichten?",
            "options": [
                "Dense-Schichten lernen lokale Muster",
                "Dense-Schichten lernen globale Muster, Convolutional-Schichten lokale Muster",
                "Beide lernen nur globale Muster",
                "Beide lernen nur lokale Muster"
            ],
            "correct_index": 1,
            "explanation": "Dense-Schichten sind vollständig verbunden und lernen globale Muster, während Convolutional-Schichten lokale Filter verwenden, um lokale Muster zu erkennen."
        },
        {
            "question": "Welches Prinzip ermöglicht es einem CNN, ein gelerntes Muster an jeder Bildposition zu erkennen?",
            "options": [
                "Datenaugmentierung",
                "Translation Invariance",
                "Überanpassung",
                "Dropout"
            ],
            "correct_index": 1,
            "explanation": "Translation Invariance ermöglicht CNNs, Muster unabhängig von ihrer Position im Bild zu erkennen, indem dieselben Filter auf unterschiedliche Bildbereiche angewendet werden."
        },
        {
            "question": "Wie groß ist die Tiefenachse eines RGB-Bildes?",
            "options": ["1", "2", "3", "4"],
            "correct_index": 2,
            "explanation": "Ein RGB-Bild besteht aus drei Farbkanälen – Rot, Grün und Blau – was eine Tiefenachse von 3 ergibt."
        },
        {
            "question": "Welche zwei Hyperparameter definieren eine Faltung maßgeblich?",
            "options": [
                "Aktivierungsfunktion und Lernrate",
                "Patch-Größe und Ausgabetiefe",
                "Optimierer und Batch-Größe",
                "Anzahl der Epochen und Padding"
            ],
            "correct_index": 1,
            "explanation": "Die Patch-Größe bestimmt die Filtergröße und die Ausgabetiefe definiert die Anzahl der erstellten Merkmale."
        },
        {
            "question": "Ein 3x3-Fenster wird auf eine 5x5-Feature-Map ohne Padding angewendet. Um wie viele Tiles schrumpft jede räumliche Dimension?",
            "options": ["1", "2", "3", "5"],
            "correct_index": 1,
            "explanation": "Ohne Padding reduziert ein 3x3-Filter jede Dimension um 2 Pixel, da er sich jeweils um eins an den Rand bewegt."
        },
        {
            "question": "Wie heißt die Technik, bei der zusätzliche Zeilen und Spalten hinzugefügt werden, um Eingabe- und Ausgabegröße gleichzuhalten?",
            "options": ["Normalisierung", "Padding", "Striding", "Pooling"],
            "correct_index": 1,
            "explanation": "Padding fügt zusätzliche Pixel hinzu, sodass sich die Ausgabegröße nicht reduziert."
        },
        {
            "question": "Welche Auswirkung hat Stride=2 bei einer Faltung?",
            "options": [
                "Keine Veränderung der Größe",
                "Vergrößert Höhe und Breite",
                "Verkleinert Höhe und Breite um Faktor 2",
                "Verdoppelt die Anzahl der Filter"
            ],
            "correct_index": 2,
            "explanation": "Ein Stride von 2 bedeutet, dass der Filter sich um jeweils zwei Pixel weiterbewegt, wodurch die Feature-Map halbiert wird."
        },
        {
            "question": "Was ist das primäre Ziel von Max-Pooling?",
            "options": [
                "Gewichte aktualisieren",
                "Feature-Maps aggressiv verkleinern",
                "Modell regulieren",
                "Filterzahl erhöhen"
            ],
            "correct_index": 1,
            "explanation": "Max-Pooling reduziert die räumlichen Dimensionen einer Feature-Map, indem nur die höchsten Werte innerhalb eines Patch beibehalten werden."
        },
        {
            "question": "Eine Feature-Map besitzt immer Achsen für ...",
            "options": [
                "Breite, Höhe, Zeit",
                "Höhe, Tiefe, Batch",
                "Höhe, Breite, Tiefe",
                "Filter, Verlust, Genauigkeit"
            ],
            "correct_index": 2,
            "explanation": "Feature-Maps enthalten Höhe und Breite für räumliche Informationen sowie Tiefe für verschiedene Filterausgaben."
        },
        {
            "question": "Was lernen tiefere Convolutional-Schichten typischerweise?",
            "options": [
                "Einfache Kanten",
                "Rauschen",
                "Größere, abstraktere Muster aus früheren Features",
                "Gewichtsinitialisierung"
            ],
            "correct_index": 2,
            "explanation": "Frühe Schichten erfassen grundlegende Muster wie Kanten, während spätere Schichten komplexere Merkmale aus diesen zusammensetzen."
        },
        {
            "question": "Average Pooling berechnet als Ausgabe eines Patches",
            "options": [
                "das Maximum jeder Tiefe",
                "den Median jeder Tiefe",
                "den Durchschnitt jeder Tiefe",
                "das Minimum jeder Tiefe"
            ],
            "correct_index": 2,
            "explanation": "Average Pooling berechnet den Mittelwert aller Pixel innerhalb eines Patches und reduziert so die Größe der Feature-Map."
        },
        {
            "question": "Wofür ist Max-Pooling nicht hauptsächlich zuständig?",
            "options": [
                "Raumhierarchien zu lernen",
                "Parameterzahl reduzieren",
                "Aktivierungen normalisieren",
                "Downsampling durchführen"
            ],
            "correct_index": 2,
            "explanation": "Max-Pooling reduziert die Größe der Feature-Map, ist jedoch nicht direkt für Aktivierungsnormalisierung zuständig."
        },
        {
            "question": "Wenn Sie eine Feature-Map um Faktor 2 verkleinern möchten, wählen Sie am wahrscheinlichsten",
            "options": [
                "Max Pooling mit Stride 2",
                "Padding",
                "Faltung mit Stride 1",
                "Average Pooling mit Stride 1"
            ],
            "correct_index": 0,
            "explanation": "Max-Pooling mit Stride 2 reduziert die Größe der Feature-Map direkt, indem jedes zweite Pixel verworfen wird."
        },
        {
            "question": "Welche Art von Mustern lernt typischerweise die erste Convolution-Schicht?",
            "options": [
                "Komplexe Objekte wie Gesichter",
                "Kleine lokale Merkmale (z.B. Kanten)",
                "Globale Semantik",
                "Farbverteilungen"
            ],
            "correct_index": 1,
            "explanation": "Erste Convolution-Schichten erkennen grundlegende Strukturen wie Kanten und Texturen, bevor sie komplexere Muster lernen."
        },
        {
            "question": "Nach der ersten Convolution repräsentiert die Tiefenachse der Feature Map ...",
            "options": [
                "Farbkanäle",
                "Einzelne Pixel",
                "Filter / Features",
                "Zeitschritte"
            ],
            "correct_index": 2,
            "explanation": "Nach der ersten Faltung werden die Tiefenachsen der Feature Map durch verschiedene Filter bestimmt, die unterschiedliche Muster erfassen."
        },
        {
            "question": "Hauptzweck des Paddings ist ...",
            "options": [
                "Training zu beschleunigen",
                "Overfitting zu verhindern",
                "Räumliche Dimensionen des Inputs zu erhalten",
                "Die Output-Depth zu reduzieren"
            ],
            "correct_index": 2,
            "explanation": "Padding stellt sicher, dass die Größe der Eingabe erhalten bleibt, indem zusätzliche Pixel um die Bildränder hinzugefügt werden."
        },
        {
            "question": "Flattening in einem CNN bedeutet ...",
            "options": [
                "Eine 1×1-Convolution anwenden",
                "Die 3D-Feature-Map vor Dense-Layern in einen 1D-Vektor umwandeln",
                "Feature-Maps Zero-Padden",
                "Über Kanäle mitteln"
            ],
            "correct_index": 1,
            "explanation": "Flattening wandelt die mehrdimensionale Feature Map in einen Vektor um, damit sie an Dense-Layer weitergegeben werden kann."
        },
        {
            "question": "Convolution-Layer _____ lernen Muster, während Dense-Layer _____ Muster lernen.",
            "options": [
                "globale; lokale",
                "sequentielle; räumliche",
                "lokale; globale",
                "zeitliche; kategoriale"
            ],
            "correct_index": 2,
            "explanation": "Convolution-Layer extrahieren lokale Muster, während Dense-Layer Muster auf einer globalen Ebene verarbeiten."
        },
        {
            "question": "Ein Filter in einem CNN ist am besten beschrieben als ...",
            "options": [
                "Einzelner Pixelwert",
                "Gelernte Gewichtsmatrix, die ein spezifisches Merkmal detektiert",
                "Lernratenplan",
                "Stride der Convolution"
            ],
            "correct_index": 1,
            "explanation": "Ein Filter in einem CNN ist eine kleine Gewichtsmatrix, die über das Eingangsbild bewegt wird und spezifische Merkmale lernt."
        },
        {
            "question": "Wird kein Padding verwendet und der Kernel ist 3×3, wie viele Pixel gehen an jedem Rand verloren?",
            "options": ["0", "1", "2", "3"],
            "correct_index": 1,
            "explanation": "Ohne Padding verliert eine 3×3-Faltung einen Pixel an jedem Rand des Bildes, da die Filter nicht über die Grenze hinaus operieren können."
        },
        {
            "question": "Welche Pooling-Operation liefert den Maximalwert jedes Fensters?",
            "options": [
                "Min-Pooling",
                "Average-Pooling",
                "Sum-Pooling",
                "Max-Pooling"
            ],
            "correct_index": 3,
            "explanation": "Max-Pooling wählt den höchsten Wert innerhalb eines definierten Bereichs aus und reduziert so die Bildgröße."
        },
        {
            "question": "Hierarchisches Lernen von Features in CNNs bedeutet, dass ...",
            "options": [
                "Alle Layer dieselbe Abstraktionsebene lernen",
                "Tiefere Layer Kombinationen einfacher Features früherer Layer lernen",
                "Frühe Layer auf globalen Kontext fokussieren",
                "Pooling-Layer Filter lernen"
            ],
            "correct_index": 1,
            "explanation": "CNNs lernen in hierarchischer Weise: Frühe Layer erfassen einfache Muster wie Kanten, während tiefere Layer komplexere Features kombinieren."
        },
        {
            "question": "Ein CNN benötigt weniger Trainingsdaten als ein vergleichbares Dense-Netz hauptsächlich wegen ...",
            "options": [
                "Datenaugmentation",
                "Translationsinvarianz & Weight Sharing",
                "Hoher Lernrate",
                "Dropout-Regularisierung"
            ],
            "correct_index": 1,
            "explanation": "CNNs nutzen Gewichts-Sharing und Translation-Invariance, wodurch sie Muster effizienter lernen und weniger Daten benötigen."
        },
        {
            "question": "Was ist das Hauptziel der Regularisierung?",
            "options": [
                "Die Lernrate zu erhöhen",
                "Die Trainingszeit zu verkürzen",
                "Overfitting zu vermeiden",
                "Die Datenmenge zu reduzieren"
            ],
            "correct_index": 2,
            "explanation": "Regularisierung hilft, Overfitting zu vermeiden, indem zu komplexe Muster begrenzt und das Modell verallgemeinerungsfähiger gemacht wird."
        },
        {
            "question": "Wie wird die Regularisierung technisch in der Optimierung des Modells umgesetzt?",
            "options": [
                "Durch Erhöhung der Lernrate",
                "Durch Hinzufügen eines Strafterms zur Verlustfunktion",
                "Durch Reduktion der Batchgröße",
                "Durch Datenaugmentation"
            ],
            "correct_index": 1,
            "explanation": "Die Regularisierung wird durch einen zusätzlichen Strafterm in der Verlustfunktion umgesetzt, der große Gewichte im Modell reduziert."
        },
        {
            "question": "Was bewirkt der Strafterm in der Regularisierung?",
            "options": [
                "Er erhöht die Gewichte des Modells",
                "Er macht das Modell langsamer",
                "Er verhindert, dass das Modell die Trainingsdaten zu genau lernt",
                "Er reduziert die Anzahl der Epochen"
            ],
            "correct_index": 2,
            "explanation": "Der Strafterm verhindert Overfitting, indem er große Gewichtswerte reduziert und somit die Anpassung an die Trainingsdaten begrenzt."
        },
        {
            "question": "Was ist ein typischer Effekt von L1-Regularisierung?",
            "options": [
                "Erhöhte Anzahl an Epochen",
                "Gleichmäßige Verteilung der Gewichte",
                "Setzt Gewichte auf Null",
                "Schnelleres Training"
            ],
            "correct_index": 2,
            "explanation": "Die L1-Regularisierung führt dazu, dass viele Gewichte auf Null gesetzt werden, was zu einer sparsamen Modellrepräsentation führt."
        },
        {
            "question": "Welche Norm wird in der L2-Regularisierung verwendet?",
            "options": [
                "Absolutwert",
                "Quadratwurzel der quadrierten Gewichte",
                "Kubikwurzel",
                "Maximumswert"
            ],
            "correct_index": 1,
            "explanation": "Die L2-Regularisierung nutzt die Quadratsumme der Gewichtswerte, um große Gewichtswerte zu bestrafen und das Modell stabiler zu machen."
        },
        {
            "question": "Was bewirkt die L2-Regularisierung im Modell?",
            "options": [
                "Sie reduziert die Datenmenge",
                "Sie bevorzugt größere Gewichte",
                "Sie schränkt die Größe der Gewichte ein",
                "Sie entfernt irrelevante Features"
            ],
            "correct_index": 2,
            "explanation": "L2-Regularisierung verhindert übermäßig große Gewichtswerte und hilft, das Modell vor Overfitting zu schützen."
        },
        {
            "question": "Welche Aussage trifft auf L1-Regularisierung zu?",
            "options": [
                "Führt zu gleichmäßiger Gewichtung",
                "Führt zu Feature Selektion",
                "Erhöht die Modellkomplexität",
                "Führt zu längerer Trainingszeit"
            ],
            "correct_index": 1,
            "explanation": "L1-Regularisierung führt oft zu sparsamen Lösungen, indem sie nicht relevante Features auf Null setzt und damit Feature-Selektion ermöglicht."
        },
        {
            "question": "Was stellt der Regularisierungsparameter dar?",
            "options": [
                "Die Lernrate des Modells",
                "Die maximale Anzahl an Epochen",
                "Das Gewicht des Strafterms in der Verlustfunktion",
                "Die Anzahl der Features"
            ],
            "correct_index": 2,
            "explanation": "Der Regularisierungsparameter bestimmt, wie stark der Strafterm die Modellgewichte beeinflusst und reguliert das Risiko von Overfitting."
        },
        {
            "question": "Was passiert bei zu starker Regularisierung?",
            "options": [
                "Das Modell overfittet schneller",
                "Die Gewichte werden zu klein und das Modell underfittet",
                "Es entsteht kein Unterschied zur normalen Verlustfunktion",
                "Die Batchgröße steigt"
            ],
            "correct_index": 1,
            "explanation": "Zu starke Regularisierung kann dazu führen, dass die Gewichte zu klein werden und das Modell nicht mehr genug Muster aus den Daten lernt."
        },
        {
            "question": "Was bewirkt Dropout?",
            "options": [
                "Es reduziert die Anzahl der Trainingsdaten",
                "Es entfernt dauerhaft Neuronen",
                "Es deaktiviert zufällig Neuronen während des Trainings",
                "Es erhöht die Netzwerkkomplexität"
            ],
            "correct_index": 2,
            "explanation": "Dropout deaktiviert zufällig Neuronen in verschiedenen Trainingsdurchläufen, um das Modell robuster gegenüber Overfitting zu machen."
        },
        {
            "question": "Wozu dient Early Stopping?",
            "options": [
                "Um das Modell schneller zu machen",
                "Um die Anzahl der Neuronen zu reduzieren",
                "Um das Training zu stoppen, wenn sich der Validierungsfehler nicht mehr verbessert",
                "Um alle Epochen vollständig zu nutzen"
            ],
            "correct_index": 2,
            "explanation": "Early Stopping unterbricht das Training automatisch, wenn die Validierungsgenauigkeit nicht mehr steigt, um Overfitting zu vermeiden."
        },
        {
            "question": "Was beschreibt das Bagging-Verfahren?",
            "options": [
                "Lernen mit nur einem Modell",
                "Kombination von Modellen durch Mittelung ihrer Vorhersagen",
                "Reduktion der Datenmenge",
                "Entfernen von Ausreißern"
            ],
            "correct_index": 1,
            "explanation": "Bagging kombiniert mehrere Modelle, indem es ihre Vorhersagen mittelt, um die Robustheit gegenüber Schwankungen zu verbessern."
        },
        {
            "question": "Welche Technik erweitert künstlich den Datensatz?",
            "options": [
                "Dropout",
                "Batch Normalization",
                "Data Augmentation",
                "Early Stopping"
            ],
            "correct_index": 2,
            "explanation": "Data Augmentation generiert künstlich neue Trainingsbeispiele, indem bestehende Daten verändert werden, z. B. durch Rotation oder Farbänderung."
        },
        {
            "question": "Welche Transformation ist kein typisches Beispiel für Data Augmentation?",
            "options": [
                "Rotation",
                "Cropping",
                "Normalisierung",
                "Farbänderung"
            ],
            "correct_index": 2,
            "explanation": "Normalisierung dient der Skalierung der Daten und gehört nicht zu den klassischen Data Augmentation-Techniken."
        },
        {
            "question": "Was ist eine Einschränkung von Data Augmentation?",
            "options": [
                "Funktioniert nur mit numerischen Daten",
                "Kann nicht für Klassifikationen verwendet werden",
                "Ist bei stark korrelierten neuen Daten begrenzt wirksam",
                "Verändert die Netzwerkarchitektur"
            ],
            "correct_index": 2,
            "explanation": "Data Augmentation kann problematisch sein, wenn erzeugte Daten zu ähnlich den Originaldaten sind und somit keine neuen Informationen hinzufügen."
        },
        {
            "question": "Was wird bei der Batch Normalization normalisiert?",
            "options": [
                "Die Daten vor dem Training",
                "Die Eingabeschicht",
                "Die Gewichte der Output-Schicht",
                "Die Aktivierungen innerhalb eines Layers"
            ],
            "correct_index": 3,
            "explanation": "Batch Normalization normalisiert die Aktivierungen eines Layers, um stabile und gut verteilte Eingaben für nachfolgende Schichten zu gewährleisten."
        },
        {
            "question": "Was ist das Ziel von Batch Normalization?",
            "options": [
                "Overfitting zu verstärken",
                "Nur die Trainingsdaten zu normalisieren",
                "Die Verteilung der Aktivierungen zu stabilisieren",
                "Die Gewichtsmatrix zu vergrößern"
            ],
            "correct_index": 2,
            "explanation": "Batch Normalization hilft, Aktivierungen über verschiedene Trainingsdurchläufe hinweg stabil zu halten und verbessert die Modellkonvergenz."
        },
        {
            "question": "Wann wird Batch Normalization durchgeführt?",
            "options": [
                "Einmalig vor dem Training",
                "Nach jeder Epoche",
                "Nach jedem Batch",
                "Nur bei großen Modellen"
            ],
            "correct_index": 2,
            "explanation": "Batch Normalization wird nach jedem Batch durchgeführt, um sicherzustellen, dass die Verteilung der Aktivierungen stabil bleibt."
        },
        {
            "question": "Was ist das Hauptziel von Data Augmentation?",
            "options": [
                "Die Genauigkeit des Validierungsdatensatzes zu reduzieren",
                "Den Trainingsprozess zu verlangsamen",
                "Mehr Trainingsdaten aus bestehenden Bildern zu generieren",
                "Bilder zufällig zu löschen"
            ],
            "correct_index": 2,
            "explanation": "Data Augmentation erzeugt neue Trainingsdaten durch Modifikationen wie Skalierung, Rotation und Farbänderung, um die Modellrobustheit zu verbessern."
        },
        {
            "question": "Warum sieht ein Modell mit Data Augmentation nie das gleiche Bild zweimal?",
            "options": [
                "Weil das Bildformat geändert wird",
                "Weil immer neue Informationen generiert werden",
                "Weil durch Zufallstransformationen jede Version leicht unterschiedlich ist",
                "Weil alte Bilder gelöscht werden"
            ],
            "correct_index": 2,
            "explanation": "Durch zufällige Transformationen entstehen leicht unterschiedliche Versionen jedes Bildes, wodurch das Modell besser generalisieren kann."
        },
        {
            "question": "Was ist ein Vorteil vortrainierter Modelle?",
            "options": [
                "Sie löschen irrelevante Daten automatisch",
                "Sie lernen ohne Labels",
                "Sie können gelernte Features auf andere Datensätze überführen",
                "Sie ignorieren visuelle Merkmale"
            ],
            "correct_index": 2,
            "explanation": "Vortrainierte Modelle haben bereits nützliche Merkmale gelernt und können diese auf andere Aufgaben übertragen, wodurch weniger Trainingsdaten benötigt werden."
        },
        {
            "question": "Warum wird der Dense Classifier eines pretrained CNNs nicht wiederverwendet?",
            "options": [
                "Er ist zu komplex",
                "Er ist zufällig",
                "Er ist spezifisch für die alten Klassen",
                "Er ist zu langsam"
            ],
            "correct_index": 2,
            "explanation": "Der Dense Classifier eines vortrainierten CNNs wurde auf bestimmte Klassen trainiert. Bei einer neuen Aufgabe sind die ursprünglichen Klassen meist nicht relevant."
        },
        {
            "question": "Was bedeutet 'Freezing' in Bezug auf ein Modell?",
            "options": [
                "Die GPU wird deaktiviert",
                "Trainingsdaten werden gesperrt",
                "Layers und deren Gewichte werden eingefroren",
                "Alle Bilder werden eingefroren gespeichert"
            ],
            "correct_index": 2,
            "explanation": "Beim 'Freezing' werden bestimmte Schichten eines neuronalen Netzes unveränderlich gemacht, sodass ihre zuvor gelernten Gewichte beibehalten werden."
        },
        {
            "question": "Wann darf man die oberen Schichten einer CNN zum Fine-Tuning freigeben?",
            "options": [
                "Sofort nach Modellinitialisierung",
                "Bevor der Classifier trainiert wurde",
                "Nachdem der Classifier trainiert wurde",
                "Vor dem Einfrieren"
            ],
            "correct_index": 2,
            "explanation": "Fine-Tuning wird üblicherweise nach dem Training des neuen Classifiers angewendet, damit die oberen Schichten sich besser an die neue Aufgabe anpassen."
        },
        {
            "question": "Welche Eigenschaft trifft auf die unteren Schichten eines CNN zu?",
            "options": [
                "Sie erkennen komplexe Formen",
                "Sie erkennen spezifische Objekte",
                "Sie extrahieren generische Merkmale",
                "Sie haben keine Funktion"
            ],
            "correct_index": 2,
            "explanation": "Untere Schichten eines CNN erfassen einfache Merkmale wie Kanten oder Texturen, die für viele Aufgaben wiederverwendet werden können."
        },
        {
            "question": "Was passiert beim 'Fine-Tuning'?",
            "options": [
                "Neue Bilder werden erzeugt",
                "Der Convolutional Base wird vollständig neu trainiert",
                "Nur obere Schichten des Bases werden weitertrainiert",
                "Dropout wird deaktiviert"
            ],
            "correct_index": 2,
            "explanation": "Fine-Tuning beinhaltet das Training der oberen Schichten eines CNN, während die unteren Schichten meist eingefroren bleiben."
        },
        {
            "question": "Warum ist ein kleines Learning Rate beim Fine-Tuning wichtig?",
            "options": [
                "Um schneller zu trainieren",
                "Um große Änderungen an gelernten Repräsentationen zu vermeiden",
                "Um das Modell zurückzusetzen",
                "Um Data Augmentation zu verbessern"
            ],
            "correct_index": 1,
            "explanation": "Eine kleine Lernrate verhindert drastische Änderungen an den Gewichten eines vortrainierten Modells und sorgt für stabiles Lernen."
        },
        {
            "question": "Worin besteht ein Nachteil, zu viele Schichten feinzujustieren?",
            "options": [
                "Modelle werden unbrauchbar",
                "Man kann keine Merkmale mehr extrahieren",
                "Erhöhtes Risiko für Overfitting",
                "Speicherplatz wird knapp"
            ],
            "correct_index": 2,
            "explanation": "Zu viele feinjustierte Schichten können zum Overfitting führen, weil das Modell sich zu stark an die neuen Daten anpasst."
        },
        {
            "question": "Warum ist die Wiederverwendung von Features über verschiedene Probleme hinweg möglich?",
            "options": [
                "Weil alle Bilder gleich sind",
                "Weil CNNs Bilddaten ignorieren",
                "Weil Feature Maps generisch sind",
                "Weil Labels nicht benötigt werden"
            ],
            "correct_index": 2,
            "explanation": "Feature Maps lernen allgemeine Muster, die auf verschiedene Aufgaben übertragen werden können, anstatt nur spezifische Klassen zu erkennen."
        },
        {
            "question": "Was macht Dropout beim Training mit Data Augmentation?",
            "options": [
                "Fügt Rauschen hinzu",
                "Verhindert das Speichern von Bildern",
                "Ergänzt die Wirkung von Data Augmentation zur Reduzierung von Overfitting",
                "Stoppt den Trainingsprozess"
            ],
            "correct_index": 2,
            "explanation": "Dropout reduziert Overfitting, indem es zufällig Neuronen deaktiviert, wodurch das Modell weniger empfindlich auf einzelne Trainingsbeispiele reagiert."
        },
        {
            "question": "Was bedeutet es, wenn Eingaben 'hoch korrelieren' sind?",
            "options": [
                "Sie sind komplett zufällig",
                "Sie enthalten keine Informationen",
                "Sie stammen aus derselben Quelle und ähneln sich",
                "Sie sind unbrauchbar"
            ],
            "correct_index": 2,
            "explanation": "Hoch korrelierte Eingaben enthalten oft ähnliche oder redundante Informationen, was die Generalisierungsfähigkeit eines Modells verringern kann."
        },
        {
            "question": "Wann ist Feature Extraction besonders hilfreich?",
            "options": [
                "Wenn kein Computer verfügbar ist",
                "Bei extrem großen Datensätzen",
                "Bei kleinen Datensätzen mit ähnlichen Aufgaben",
                "Wenn keine GPU vorhanden ist"
            ],
            "correct_index": 2,
            "explanation": "Feature Extraction ist besonders nützlich bei kleinen Datensätzen, da bereits gelernte Merkmale aus vortrainierten Modellen wiederverwendet werden können."
        },
        {
            "question": "Was beschreibt ein Feed Forward Neural Network am besten?",
            "options": [
                "Ein neuronales Netz mit Rückkopplung",
                "Ein Netz, in dem Informationen nur in eine Richtung – von Input zu Output – fließen",
                "Ein Netz, das ausschließlich für Textverarbeitung verwendet wird",
                "Ein Netz mit unendlich vielen Schichten"
            ],
            "correct_index": 1,
            "explanation": "Ein Feed Forward Neural Network verarbeitet Informationen sequenziell von Eingabe zur Ausgabe, ohne Rückkopplungen zwischen den Schichten."
        },
        {
            "question": "Welche Aussage über Aktivierungsfunktionen ist korrekt?",
            "options": [
                "Sie sind nur in der Ausgabeschicht notwendig",
                "Sie bestimmen die Lernrate",
                "Sie helfen, Nichtlinearitäten im Modell abzubilden",
                "Sie reduzieren die Anzahl der benötigten Datenpunkte"
            ],
            "correct_index": 2,
            "explanation": "Aktivierungsfunktionen wie ReLU oder Sigmoid ermöglichen dem Modell, komplexe Beziehungen und Nichtlinearitäten zwischen den Eingaben zu erfassen."
        },
        {
            "question": "Wozu dient eine Verlustfunktion (Loss Function) in neuronalen Netzen?",
            "options": [
                "Zur Verbesserung der Aktivierungsfunktion",
                "Zur Bewertung der Vorhersagequalität durch Vergleich mit den echten Labels",
                "Zum Generieren neuer Trainingsdaten",
                "Zum Speichern der Gewichtswerte"
            ],
            "correct_index": 1,
            "explanation": "Die Verlustfunktion misst die Differenz zwischen den Modellvorhersagen und den echten Labels, um das Modell während des Trainings zu optimieren."
        },
        {
            "question": "Was macht ein Optimizer im Training eines neuronalen Netzes?",
            "options": [
                "Fügt neue Daten hinzu",
                "Passt die Aktivierungsfunktionen an",
                "Ändert die Struktur des Netzes",
                "Aktualisiert Gewichte und Biases basierend auf der Verlustfunktion"
            ],
            "correct_index": 3,
            "explanation": "Ein Optimizer wie Adam oder SGD passt die Gewichte des neuronalen Netzes schrittweise an, um die Verlustfunktion zu minimieren."
        },
        {
            "question": "Was ist das Ziel beim Trainieren eines Deep-Learning-Modells?",
            "options": [
                "Möglichst viele Schichten und Neuronen zu verwenden",
                "Zufällige Gewichtswerte beizubehalten",
                "Die Vorhersagen möglichst nahe an den echten Labels auszurichten",
                "Immer eine binäre Klassifikation zu verwenden"
            ],
            "correct_index": 2,
            "explanation": "Das Hauptziel des Trainings ist es, das Modell so zu optimieren, dass seine Vorhersagen möglichst genau den echten Labels entsprechen."
        },
        {
            "question": "Was ist ein typisches Ziel bei Regressionsproblemen in neuronalen Netzen?",
            "options": [
                "Die Erkennung von Objekten",
                "Die Vorhersage diskreter Kategorien",
                "Die Reduktion der Trainingszeit",
                "Die Vorhersage kontinuierlicher Werte"
            ],
            "correct_index": 3,
            "explanation": "Bei Regressionsproblemen sagt das neuronale Netz kontinuierliche Werte voraus, beispielsweise Hauspreise oder Temperaturen."
        },
        {
            "question": "Warum ist die Initialisierung der Gewichte wichtig?",
            "options": [
                "Sie beschleunigt das Speichern der Modelle",
                "Sie beeinflusst die Trainingsdatenmenge",
                "Sie kann den Lernprozess positiv oder negativ beeinflussen",
                "Sie bestimmt die Anzahl der Ausgabeklassen"
            ],
            "correct_index": 2,
            "explanation": "Eine schlechte Initialisierung kann zu langsamer Konvergenz oder schlechten Ergebnissen führen, während eine gute Initialisierung das Lernen erleichtert."
        },
        {
            "question": "Welche Aussage zur Wahl der Anzahl versteckter Schichten (Hidden Layers) ist korrekt?",
            "options": [
                "Mehr Schichten sind immer besser",
                "Ein einfaches Problem erfordert viele versteckte Schichten",
                "Die Wahl hängt von der Komplexität des Problems ab",
                "Versteckte Schichten sind optional"
            ],
            "correct_index": 2,
            "explanation": "Die Anzahl der versteckten Schichten sollte der Komplexität des Problems entsprechen – zu wenige können zu schlechter Leistung führen, zu viele zu Overfitting."
        },
        {
            "question": "Welcher Optimierer passt die Lernrate für jeden Parameter an?",
            "options": [
                "SGD",
                "Adam",
                "RMSProp",
                "Momentum"
            ],
            "correct_index": 1,
            "explanation": "Adam passt die Lernrate dynamisch für jede Gewichtsanpassung an und kombiniert die Vorteile von Momentum und RMSProp."
        },
        {
            "question": "Was ist das Hauptziel der Regularisierung in neuronalen Netzwerken?",
            "options": [
                "Die Trainingszeit zu verkürzen",
                "Überanpassung zu verhindern",
                "Die Lernrate zu erhöhen",
                "Die Netzwerkgröße zu vergrößern"
            ],
            "correct_index": 1,
            "explanation": "Regularisierungstechniken wie L1, L2 und Dropout helfen, Überanpassung zu verhindern und die Generalisierungsfähigkeit des Modells zu verbessern."
        },
        {
            "question": "Was passiert beim Dropout während des Trainings?",
            "options": [
                "Die Gewichte werden eingefroren",
                "Einige Neuronen werden zufällig deaktiviert",
                "Der Lernrate wird reduziert",
                "Der Optimierer wird gewechselt"
            ],
            "correct_index": 1,
            "explanation": "Dropout deaktiviert zufällig eine bestimmte Anzahl von Neuronen, um Overfitting zu reduzieren und die Robustheit des Modells zu verbessern."
        },
        {
            "question": "Was sagt die Lernrate aus?",
            "options": [
                "Die Lernrate bestimmt, wie viele Schichten ein neuronales Netz haben darf.",
                "Die Lernrate gibt an, mit welcher Geschwindigkeit das Modell aus Informationen lernt",
                "Die Lernrate legt fest, wie groß das endgültige Modell sein wird.",
                "Die Lernrate gibt an, wie viele Datenpunkte pro Sekunde verarbeitet werden."
            ],
            "correct_index": 1,
            "explanation": "Die Lernrate bestimmt, wie stark die Gewichtsaktualisierung in jedem Optimierungsschritt erfolgt und beeinflusst somit die Konvergenz des Modells."
        },
        {
            "question": "Was ist die Gefahr bei einer zu niedrigen Lernrate?",
            "options": [
                "Das Modell überspringt ständig das Minimum der Fehlerfunktion.",
                "Das Training wird sofort abgebrochen.",
                "Kann in einem lokalen Minimum stecken bleiben",
                "Eine zu niedrige Lernrate führt zu Überanpassung (Overfitting)."
            ],
            "correct_index": 2,
            "explanation": "Eine zu niedrige Lernrate kann das Modell daran hindern, das optimale Minimum der Verlustfunktion effizient zu erreichen."
        },
        {
            "question": "Was ist die Gefahr bei einer zu hohen Lernrate?",
            "options": [
                "Das Modell erreicht das Optimum schneller und genauer.",
                "Die Lösung kann divergieren",
                "Overfitting",
                "Das Training funktioniert nur bei linearen Modellen nicht mehr."
            ],
            "correct_index": 1,
            "explanation": "Eine zu hohe Lernrate kann dazu führen, dass die Gewichte stark schwanken und das Modell nicht zu einer stabilen Lösung konvergiert."
        },
        {
            "question": "Was macht die Lernrate-Strategie Step decay?",
            "options": [
                "Sie erhöht die Lernrate exponentiell mit jeder Epoche.",
                "Macht die Lernrate um fixen Faktor kleiner nach einer gewünschten Anzahl Epochen",
                "Sie passt die Lernrate zufällig während des Trainings an.",
                "Sie setzt die Lernrate nach jeder Epoche auf null und startet neu."
            ],
            "correct_index": 1,
            "explanation": "Step decay reduziert die Lernrate nach einer festgelegten Anzahl von Epochen, um eine feinere Anpassung der Gewichte zu ermöglichen."
        },
        {
            "question": "Was ist eine Epoche?",
            "options": [
                "Eine Epoche ist ein einzelner Durchlauf durch nur einen Datenpunkt des Trainingssatzes.",
                "Eine Epoche ist ein Durchlauf bei dem alle Trainingsdaten einmal verwendet werden.",
                "Eine Epoche beschreibt die Anzahl der Schichten in einem neuronalen Netzwerk.",
                "Eine Epoche ist ein Durchlauf mit einem Anteil der Trainingsdaten"
            ],
            "correct_index": 1,
            "explanation": "Eine Epoche entspricht einem vollständigen Durchlauf durch den gesamten Trainingsdatensatz."
        },
        {
            "question": "Was ist die Gefahr, wenn mit zu weniger Epochen trainiert wird?",
            "options": [
                "Das Modell wird übertrainiert und passt sich zu stark den Trainingsdaten an.",
                "Das Modell konvergiert allenfalls nicht zu einer guten Lösung",
                "Das Modell wird zu stark regularisiert und erzielt daher keine guten Ergebnisse.",
                "Das Modell benötigt keine Feinabstimmung mehr und ist sofort einsatzbereit"
            ],
            "correct_index": 1,
            "explanation": "Zu wenige Epochen können dazu führen, dass das Modell nicht ausreichend trainiert wird und keine optimalen Gewichte lernt."
        },
        {
            "question": "Wann wird die Modellleistung evaluiert?",
            "options": [
                "Am Ende der letzten Epoche",
                "Nach jeder Epoche",
                "Nach jedem gelerntem Datensatz",
                "Vor dem Modell Training"
            ],
            "correct_index": 1,
            "explanation": "Die Modellleistung wird typischerweise nach jeder Epoche überprüft, um die Verbesserung des Modells zu messen."
        },
        {
            "question": "Was ist ein Batch?",
            "options": [
                "Ein Batch ist die Anzahl der Schichten in einem neuronalen Netzwerk.",
                "Ein Batch ist eine Teilmenge des Trainingsdatensatzes, die in einem Schritt verarbeitet wird.",
                "Ein Batch ist eine einzelne Datenprobe, die dem Modell während des Trainings präsentiert wird.",
                "Ein Batch ist eine spezielle Art von Modell, das auf den Trainingsdaten angewendet wird."
            ],
            "correct_index": 1,
            "explanation": "Ein Batch besteht aus einer Gruppe von Datenpunkten, die gemeinsam verarbeitet werden, um das Training zu beschleunigen."
        },
        {
            "question": "Was für eine Gefahr gibt es, wenn man die Anzahl Epochen zu groß wählt?",
            "options": [
                "Das Modell wird zu stark regularisiert und lernt keine sinnvollen Muster.",
                "Das Modell wird zu instabil und verlangsamt das Training.",
                "Das Modell wird zu langsam und benötigt mehr Epochen, um Ergebnisse zu liefern.",
                "Das Modell wird zu stark auf die Trainingsdaten angepasst und zeigt keine Fehler mehr."
            ],
            "correct_index": 3,
            "explanation": "Zu viele Epochen können dazu führen, dass sich das Modell zu sehr an die Trainingsdaten anpasst und schlecht auf neue Daten generalisiert."
        },
        {
            "question": "Welche grundlegende Idee steckt hinter dem Gradient Descent-Verfahren?",
            "options": [
                "Es findet das Maximum der Verlustfunktion durch zufällige Gewichtsanpassung.",
                "Es passt die Gewichte so an, dass die Rechenzeit minimiert wird.",
                "Es bewegt sich entlang der Gradientenrichtung, um lokale Maxima zu erreichen.",
                "Es passt die Modellparameter schrittweise in Richtung des negativsten Gradienten an, um die Verlustfunktion zu minimieren."
            ],
            "correct_index": 3,
            "explanation": "Gradient Descent passt die Gewichte des Modells schrittweise an, um das Minimum der Verlustfunktion zu erreichen."
        },
        {
            "question": "Welche Aufgabe hat ein Optimierer im Training eines neuronalen Netzwerks?",
            "options": [
                "Er bestimmt, wie viele Daten für das Modell gespeichert werden sollen.",
                "Er reduziert den Speicherverbrauch, indem er Parameter entfernt.",
                "Er passt die Gewichte des Modells so an, dass die Verlustfunktion minimiert wird.",
                "Er erhöht die Modellkomplexität automatisch, um Overfitting zu vermeiden."
            ],
            "correct_index": 2,
            "explanation": "Ein Optimierer aktualisiert die Gewichte des Modells so, dass die Verlustfunktion minimiert wird."
        },
        {
            "question": "Wofür wird eine Loss Function im Training verwendet?",
            "options": [
                "Um den Unterschied zwischen Vorhersage und echtem Wert zu messen.",
                "Um die Trainingsdaten zu normalisieren.",
                "Um die Anzahl der Layer zu bestimmen.",
                "Um das Modell schneller zu machen."
            ],
            "correct_index": 0,
            "explanation": "Die Loss Function quantifiziert, wie gut das Modell die Vorhersage an den echten Wert annähert."
        },
        {
            "question": "Warum muss eine Loss Function differenzierbar sein?",
            "options": [
                "Damit Gradient Descent sie minimieren kann.",
                "Damit sie auf alle Probleme passt.",
                "Damit man keine Aktivierungsfunktion braucht.",
                "Damit sie ohne Optimizer funktioniert."
            ],
            "correct_index": 0,
            "explanation": "Eine differenzierbare Loss Function ist nötig, damit Gradient Descent die Ableitung berechnen und die Gewichte entsprechend anpassen kann."
        },
        {
            "question": "Was ist der Hauptunterschied zwischen einer Loss Function und einer Metrik?",
            "options": [
                "Die Loss Function wird zur Optimierung genutzt, die Metrik zur Bewertung.",
                "Beide machen dasselbe.",
                "Metriken funktionieren nur bei Regression.",
                "Die Loss Function wird nur nach dem Training verwendet."
            ],
            "correct_index": 0,
            "explanation": "Die Loss Function wird verwendet, um das Modell zu optimieren, während Metriken genutzt werden, um dessen Leistung zu bewerten."
        },
        {
            "question": "Welche Aussage zu MSE ist korrekt?",
            "options": [
                "Große Fehler werden stärker bestraft als kleine.",
                "Alle Fehler werden gleich bewertet.",
                "MSE funktioniert nur bei Klassifikation.",
                "MSE ist nur für binäre Aufgaben geeignet."
            ],
            "correct_index": 0,
            "explanation": "Mean Squared Error (MSE) bestraft größere Fehler stärker, da die Fehlerwerte quadriert werden."
        },
        {
            "question": "Wofür ist die Categorical Cross-Entropy geeignet?",
            "options": [
                "Für Klassifikation mit mehr als zwei Klassen.",
                "Für Regression mit kontinuierlichen Werten.",
                "Für binäre Entscheidungen.",
                "Für Bilder mit nur einem Farbkanal."
            ],
            "correct_index": 0,
            "explanation": "Categorical Cross-Entropy wird in mehrklassigen Klassifikationsaufgaben verwendet, um die Wahrscheinlichkeit jeder Klasse zu bewerten."
        },
        {
            "question": "Warum kann man bei Multi-Klassifikation keine MSE verwenden?",
            "options": [
                "Weil MSE keine Wahrscheinlichkeitsverteilungen berücksichtigt.",
                "Weil MSE zu schnell konvergiert.",
                "Weil MSE keine Label erkennt.",
                "Weil MSE nur bei Sigmoid funktioniert."
            ],
            "correct_index": 0,
            "explanation": "MSE ist für Klassifikation ungeeignet, da sie keine Wahrscheinlichkeitsverteilungen berücksichtigt."
        },
        {
            "question": "Was passiert mit der Loss Function, wenn das Modell besser wird?",
            "options": [
                "Sie wird kleiner.",
                "Sie bleibt konstant.",
                "Sie wird negativ.",
                "Sie steigt exponentiell."
            ],
            "correct_index": 0,
            "explanation": "Je besser das Modell trainiert ist, desto kleiner wird die Loss Function, da der Unterschied zwischen Vorhersage und echtem Wert minimiert wird."
        },
        {
            "question": "Was misst die Loss Function bei einem Klassifikationsmodell mit Softmax-Ausgabe?",
            "options": [
                "Wie gut die Wahrscheinlichkeitsverteilung zur wahren Klasse passt",
                "Ob die Summe aller Gewichte 1 ist",
                "Wie groß die Lernrate ist",
                "Ob die Metrik Accuracy ≥ 90% ist"
            ],
            "correct_index": 0,
            "explanation": "Die Loss Function eines Klassifikationsmodells mit Softmax überprüft, wie gut die vorhergesagte Wahrscheinlichkeitsverteilung mit der wahren Klasse übereinstimmt."
        },
        {
            "question": "Was ist der Hauptunterschied zwischen Binary und Categorical Cross-Entropy?",
            "options": [
                "Binary ist für 2 Klassen, Categorical für viele Klassen",
                "Binary ist für Regression, Categorical für Bilder",
                "Binary ist schneller, Categorical langsamer",
                "Categorical benötigt keine One-Hot-Encoding"
            ],
            "correct_index": 0,
            "explanation": "Binary Cross-Entropy wird bei binären Klassifikationen eingesetzt, während Categorical Cross-Entropy für mehrklassige Klassifikationen genutzt wird."
        },
        {
            "question": "Welche Loss Function würdest du für Hauspreisvorhersage nehmen?",
            "options": [
                "MSE",
                "Binary Cross-Entropy",
                "Categorical Cross-Entropy",
                "Hinge Loss"
            ],
            "correct_index": 0,
            "explanation": "Mean Squared Error (MSE) ist die gängige Loss Function für Regressionsprobleme wie die Vorhersage von Hauspreisen."
        },
        {
            "question": "Wozu dient ein Optimizer im Training eines neuronalen Netzes?",
            "options": [
                "Er passt die Gewichte an, um die Loss Function zu minimieren",
                "Er misst die Testgenauigkeit",
                "Er kontrolliert die Batch-Größe",
                "Er bestimmt die Anzahl der Epochen"
            ],
            "correct_index": 0,
            "explanation": "Ein Optimizer aktualisiert die Gewichte des neuronalen Netzes, um die Fehler in der Loss Function zu minimieren und bessere Vorhersagen zu treffen."
        },
        {
            "question": "Welche Information benötigt ein Optimizer bei jedem Schritt?",
            "options": [
                "Den Gradienten der Loss Function",
                "Die Zielmetrik (z. B. Accuracy)",
                "Die Anzahl der Layer",
                "Den Dateinamen des Datasets"
            ],
            "correct_index": 0,
            "explanation": "Ein Optimizer benötigt den Gradienten der Loss Function, um die Richtung der Gewichtsänderungen zu bestimmen."
        },
        {
            "question": "Was ist der wichtigste Hyperparameter beim Optimizer?",
            "options": [
                "Die Lernrate",
                "Die Anzahl der Layer",
                "Die Größe des Testsets",
                "Die Aktivierungsfunktion"
            ],
            "correct_index": 0,
            "explanation": "Die Lernrate ist einer der wichtigsten Hyperparameter, da sie bestimmt, wie schnell oder langsam das Modell lernt."
        },
        {
            "question": "Was passiert bei einer zu hohen Lernrate?",
            "options": [
                "Das Modell konvergiert möglicherweise nicht oder divergiert",
                "Das Modell lernt sehr stabil",
                "Es wird kein Backpropagation benötigt",
                "Die Loss Function wird ignoriert"
            ],
            "correct_index": 0,
            "explanation": "Eine zu hohe Lernrate kann dazu führen, dass das Modell nicht konvergiert oder instabile Updates vornimmt."
        },
        {
            "question": "Was passiert bei einer zu niedrigen Lernrate?",
            "options": [
                "Das Modell lernt extrem langsam",
                "Die Genauigkeit steigt sofort auf 100%",
                "Die Loss Function wird unbrauchbar",
                "Das Modell vergisst alle vorherigen Schritte"
            ],
            "correct_index": 0,
            "explanation": "Eine zu niedrige Lernrate kann das Training erheblich verlangsamen, da die Gewichtsupdates sehr klein sind."
        },
        {
            "question": "Was ist 'Learning Rate Decay'?",
            "options": [
                "Eine Technik, bei der die Lernrate schrittweise gesenkt wird",
                "Eine Methode, um die Lernrate zu erhöhen",
                "Eine spezielle Art von Loss Function",
                "Ein Aktivierungstyp in der Ausgangsschicht"
            ],
            "correct_index": 0,
            "explanation": "Learning Rate Decay reduziert die Lernrate während des Trainings, um feinere Anpassungen zu ermöglichen."
        },
        {
            "question": "Was zeichnet Adam gegenüber SGD aus?",
            "options": [
                "Adam passt die Lernrate für jeden Parameter dynamisch an",
                "Adam ignoriert Gradienten",
                "Adam benötigt keine Loss Function",
                "Adam ist deterministisch"
            ],
            "correct_index": 0,
            "explanation": "Adam verbessert SGD durch adaptive Lernraten, die sich an jeden Parameter individuell anpassen."
        },
        {
            "question": "Was ist das Ziel des Gradient Descent Algorithmus?",
            "options": [
                "Das Finden eines Minimums der Loss Function",
                "Die Erstellung neuer Testdaten",
                "Das Erhöhen der Batchgröße",
                "Die Änderung der Modellarchitektur"
            ],
            "correct_index": 0,
            "explanation": "Gradient Descent wird verwendet, um die Loss Function zu minimieren, indem die Gewichte des Modells in die Richtung des negativsten Gradienten angepasst werden."
        },
        {
            "question": "Warum sind rekurrente neuronale Netze (RNNs) besonders geeignet für Sequenzdaten?",
            "options": [
                "Weil sie keine Erinnerung haben.",
                "Weil sie Abhängigkeiten zwischen aufeinanderfolgenden Datenpunkten erfassen können.",
                "Weil sie schneller trainiert werden können.",
                "Weil sie weniger Parameter benötigen."
            ],
            "correct_index": 1,
            "explanation": "RNNs behalten Informationen aus früheren Zeitschritten und erfassen Abhängigkeiten zwischen Sequenzdaten wie Sprache oder Zeitreihen."
        },
        {
            "question": "Welche Art von Daten sind Beispiele für Sequenzdaten?",
            "options": [
                "Bilder",
                "Text und Zeitreihen",
                "Tabellen und Datenbanken",
                "Unabhängige Datenpunkte"
            ],
            "correct_index": 1,
            "explanation": "Sequenzdaten bestehen aus aufeinanderfolgenden Datenpunkten, wie Texte oder Zeitreihen, bei denen die Reihenfolge der Daten eine wichtige Rolle spielt."
        },
        {
            "question": "Warum ist die Reihenfolge in Sequenzdaten wichtig?",
            "options": [
                "Weil sie die Trainingszeit verkürzt.",
                "Weil der Vorgänger den nachfolgenden Wert beeinflusst.",
                "Weil sie die Anzahl der Parameter reduziert.",
                "Weil sie die Klassifikationsgenauigkeit erhöht."
            ],
            "correct_index": 1,
            "explanation": "Bei Sequenzdaten beeinflussen frühere Werte spätere Werte, was besonders bei Aufgaben wie Sprachverarbeitung und Zeitserienanalyse entscheidend ist."
        },
        {
            "question": "Wie wird der state in einem RNN aktualisiert?",
            "options": [
                "Durch Multiplikation vom Input mit dem vorherigen State",
                "Durch Anwendung einer nichtlinearen Funktion auf Input und den vorherigen State",
                "Input und der vorangehende State werden skaliert und anschließend addiert",
                "Der skalierte Input wird mit dem bereits skalierten Output-State multipliziert"
            ],
            "correct_index": 1,
            "explanation": "Der Zustand eines RNN wird durch eine nichtlineare Transformation von Input und vorherigem State aktualisiert, um sequentielle Informationen zu erfassen."
        },
        {
            "question": "Wie verarbeiten RNNs Sequenzen?",
            "options": [
                "Durch parallele Verarbeitung aller Elemente gleichzeitig.",
                "Durch Iteration über die Sequenzelemente.",
                "Durch Zufallsauswahl der Elemente.",
                "Durch Verarbeitung aller Elemente in einem einzigen Schritt."
            ],
            "correct_index": 1,
            "explanation": "RNNs verarbeiten Sequenzdaten schrittweise, indem sie jedes Element nacheinander verarbeiten und frühere Informationen speichern."
        },
        {
            "question": "Was bewahrt ein RNN während der Verarbeitung einer Sequenz?",
            "options": [
                "Einen festen Wert.",
                "Einen Zustand, der Informationen über die bisher gesehenen Elemente enthält.",
                "Eine zufällige Zahl.",
                "Eine Konstante."
            ],
            "correct_index": 1,
            "explanation": "Das RNN bewahrt einen Zustand, der Informationen über frühere Elemente der Sequenz enthält und so den Kontext für spätere Vorhersagen bereitstellt."
        },
        {
            "question": "Wie wird der Zustand eines RNNs zwischen zwei unabhängigen Sequenzen behandelt?",
            "options": [
                "Er wird beibehalten.",
                "Er wird zurückgesetzt.",
                "Er wird zufällig initialisiert.",
                "Er wird verdoppelt."
            ],
            "correct_index": 1,
            "explanation": "Zwischen unabhängigen Sequenzen wird der Zustand eines RNN zurückgesetzt, damit es sich nicht an vorherige Sequenzen erinnert."
        },
        {
            "question": "Welche Form hat die Eingabe eines RNNs?",
            "options": [
                "Ein 1D-Tensor.",
                "Ein 2D-Tensor.",
                "Ein 3D-Tensor.",
                "Ein skalarer Wert."
            ],
            "correct_index": 2,
            "explanation": "RNNs verarbeiten Sequenzen, daher haben sie typischerweise 3D-Tensoren der Form (Batch, Sequenzlänge, Features)."
        },
        {
            "question": "Wofür steht die Abkürzung LSTM?",
            "options": [
                "Long Short-Term Memory",
                "Large Scale Training Model",
                "Linear Sequential Training Model",
                "Layered Sequential Training Model"
            ],
            "correct_index": 0,
            "explanation": "LSTM steht für Long Short-Term Memory und ist eine Art von RNN, die langfristige Abhängigkeiten besser speichert."
        },
        {
            "question": "Was ist das Ziel des Gradient Descent Algorithmus?",
            "options": [
                "Das Finden eines Minimums der Loss Function",
                "Die Erstellung neuer Testdaten",
                "Das Erhöhen der Batchgröße",
                "Die Änderung der Modellarchitektur"
            ],
            "correct_index": 0,
            "explanation": "Gradient Descent wird verwendet, um die Loss Function zu minimieren, indem die Gewichte des Modells in die Richtung des negativsten Gradienten angepasst werden."
        },
        {
            "question": "Warum sind rekurrente neuronale Netze (RNNs) besonders geeignet für Sequenzdaten?",
            "options": [
                "Weil sie keine Erinnerung haben.",
                "Weil sie Abhängigkeiten zwischen aufeinanderfolgenden Datenpunkten erfassen können.",
                "Weil sie schneller trainiert werden können.",
                "Weil sie weniger Parameter benötigen."
            ],
            "correct_index": 1,
            "explanation": "RNNs behalten Informationen aus früheren Zeitschritten und erfassen Abhängigkeiten zwischen Sequenzdaten wie Sprache oder Zeitreihen."
        },
        {
            "question": "Welche Art von Daten sind Beispiele für Sequenzdaten?",
            "options": [
                "Bilder",
                "Text und Zeitreihen",
                "Tabellen und Datenbanken",
                "Unabhängige Datenpunkte"
            ],
            "correct_index": 1,
            "explanation": "Sequenzdaten bestehen aus aufeinanderfolgenden Datenpunkten, wie Texte oder Zeitreihen, bei denen die Reihenfolge der Daten eine wichtige Rolle spielt."
        },
        {
            "question": "Warum ist die Reihenfolge in Sequenzdaten wichtig?",
            "options": [
                "Weil sie die Trainingszeit verkürzt.",
                "Weil der Vorgänger den nachfolgenden Wert beeinflusst.",
                "Weil sie die Anzahl der Parameter reduziert.",
                "Weil sie die Klassifikationsgenauigkeit erhöht."
            ],
            "correct_index": 1,
            "explanation": "Bei Sequenzdaten beeinflussen frühere Werte spätere Werte, was besonders bei Aufgaben wie Sprachverarbeitung und Zeitserienanalyse entscheidend ist."
        },
        {
            "question": "Wie wird der state in einem RNN aktualisiert?",
            "options": [
                "Durch Multiplikation vom Input mit dem vorherigen State",
                "Durch Anwendung einer nichtlinearen Funktion auf Input und den vorherigen State",
                "Input und der vorangehende State werden skaliert und anschließend addiert",
                "Der skalierte Input wird mit dem bereits skalierten Output-State multipliziert"
            ],
            "correct_index": 1,
            "explanation": "Der Zustand eines RNN wird durch eine nichtlineare Transformation von Input und vorherigem State aktualisiert, um sequentielle Informationen zu erfassen."
        },
        {
            "question": "Wie verarbeiten RNNs Sequenzen?",
            "options": [
                "Durch parallele Verarbeitung aller Elemente gleichzeitig.",
                "Durch Iteration über die Sequenzelemente.",
                "Durch Zufallsauswahl der Elemente.",
                "Durch Verarbeitung aller Elemente in einem einzigen Schritt."
            ],
            "correct_index": 1,
            "explanation": "RNNs verarbeiten Sequenzdaten schrittweise, indem sie jedes Element nacheinander verarbeiten und frühere Informationen speichern."
        },
        {
            "question": "Was bewahrt ein RNN während der Verarbeitung einer Sequenz?",
            "options": [
                "Einen festen Wert.",
                "Einen Zustand, der Informationen über die bisher gesehenen Elemente enthält.",
                "Eine zufällige Zahl.",
                "Eine Konstante."
            ],
            "correct_index": 1,
            "explanation": "Das RNN bewahrt einen Zustand, der Informationen über frühere Elemente der Sequenz enthält und so den Kontext für spätere Vorhersagen bereitstellt."
        },
        {
            "question": "Wie wird der Zustand eines RNNs zwischen zwei unabhängigen Sequenzen behandelt?",
            "options": [
                "Er wird beibehalten.",
                "Er wird zurückgesetzt.",
                "Er wird zufällig initialisiert.",
                "Er wird verdoppelt."
            ],
            "correct_index": 1,
            "explanation": "Zwischen unabhängigen Sequenzen wird der Zustand eines RNN zurückgesetzt, damit es sich nicht an vorherige Sequenzen erinnert."
        },
        {
            "question": "Welche Form hat die Eingabe eines RNNs?",
            "options": [
                "Ein 1D-Tensor.",
                "Ein 2D-Tensor.",
                "Ein 3D-Tensor.",
                "Ein skalarer Wert."
            ],
            "correct_index": 2,
            "explanation": "RNNs verarbeiten Sequenzen, daher haben sie typischerweise 3D-Tensoren der Form (Batch, Sequenzlänge, Features)."
        },
        {
            "question": "Wofür steht die Abkürzung LSTM?",
            "options": [
                "Long Short-Term Memory",
                "Large Scale Training Model",
                "Linear Sequential Training Model",
                "Layered Sequential Training Model"
            ],
            "correct_index": 0,
            "explanation": "LSTM steht für Long Short-Term Memory und ist eine Art von RNN, die langfristige Abhängigkeiten besser speichert."
        },
        {
            "question": "Welches Problem löst LSTM?",
            "options": [
                "Das Problem der Überanpassung.",
                "Das Problem des verschwindenden Gradienten.",
                "Das Problem der zu großen Parameteranzahl.",
                "Das Problem der langsamen Trainingszeit."
            ],
            "correct_index": 1,
            "explanation": "LSTMs wurden entwickelt, um das Problem des verschwindenden Gradienten in langen Sequenzen zu lösen, indem sie sich wichtige Informationen über längere Zeiträume merken."
        },
        {
            "question": "Was ist die Funktion des Carry states ct in einem LSTM?",
            "options": [
                "Er speichert zufällige Werte.",
                "Er trägt Informationen über Zeitschritte hinweg.",
                "Er initialisiert die Gewichte.",
                "Er berechnet die Ausgabe direkt."
            ],
            "correct_index": 1,
            "explanation": "Der Carry State speichert Langzeitinformationen in einem LSTM und hilft, den Einfluss vergangener Inputs auf aktuelle Berechnungen zu bewahren."
        },
        {
            "question": "Wie wird der nächste Carry state ct+1 in einem LSTM berechnet?",
            "options": [
                "Durch Addition der Eingabe und des vorherigen Zustands.",
                "Durch Addition von gewichteten neuen und gewichteten bestehenden irrelevanten Informationen.",
                "Durch Multiplikation mit einer Konstanten.",
                "Durch Anwendung einer Aktivierungsfunktion."
            ],
            "correct_index": 1,
            "explanation": "Der neue Carry State wird durch eine Kombination von neuen Eingaben und dem vorherigen Zustand berechnet, wobei nicht relevante Informationen gefiltert werden."
        },
        {
            "question": "Welche Komponenten (Gates) hat eine LSTM-Zelle?",
            "options": [
                "Eingabe-Gate, Ausgabe-Gate, Vergessens-Gate",
                "Aktivierungsfunktion, Verlustfunktion, Optimierer",
                "Hidden Layer, Output Layer, Input Layer",
                "Bias, Gewichte, Aktivierungsfunktion"
            ],
            "correct_index": 0,
            "explanation": "LSTM-Zellen enthalten drei Haupt-Gates: das Eingabe-Gate, das Ausgabe-Gate und das Vergessens-Gate, die zusammen die gespeicherten Informationen regulieren."
        },
        {
            "question": "Was ist die Hauptaufgabe des Carry-States in einem LSTM?",
            "options": [
                "Die Aktualisierung des versteckten Zustands.",
                "Die Steuerung, welche Informationen beibehalten oder vergessen werden.",
                "Die Berechnung der Ausgabe.",
                "Die Anwendung der Aktivierungsfunktion."
            ],
            "correct_index": 1,
            "explanation": "Der Carry State steuert, welche Informationen beibehalten oder verworfen werden, um langfristige Abhängigkeiten effektiv zu lernen."
        },
        {
            "question": "Was ist rekurrentes Dropout?",
            "options": [
                "Eine Methode zur Beschleunigung des Trainings, durch zufälliges Auslassen von Datenpunkten.",
                "Eine Methode zur Reduktion der Parameteranzahl durch Auslassen jedes n-ten Werts.",
                "Eine Methode zur Bekämpfung von Overfitting durch Anwendung einer konstanten Dropout-Maske über die Zeit.",
                "Eine Methode zur Erhöhung der Klassifikationsgenauigkeit durch Dropout irrelevanter Parameter."
            ],
            "correct_index": 2,
            "explanation": "Rekurrentes Dropout wird über die Zeit hinweg konstant angewendet, um die Robustheit von RNNs zu erhöhen und Overfitting zu reduzieren."
        },
        {
            "question": "Warum ist das Stapeln von rekurrenten Schichten nützlich?",
            "options": [
                "Es reduziert die Trainingszeit.",
                "Es erhöht die Repräsentationskraft des Netzwerks.",
                "Es verringert die Anzahl der Parameter.",
                "Es beschleunigt die Vorwärtspropagation."
            ],
            "correct_index": 1,
            "explanation": "Das Stapeln mehrerer rekurrenter Schichten ermöglicht es dem Modell, komplexere hierarchische Merkmale in den Sequenzdaten zu erfassen."
        },
        {
            "question": "Wie funktioniert ein bidirektionales RNN?",
            "options": [
                "Es verarbeitet die Eingabesequenz in einer zufälligen Reihenfolge.",
                "Es verarbeitet die Eingabesequenz in beiden Richtungen (chronologisch und antichronologisch).",
                "Es verarbeitet die Eingabesequenz nur in umgekehrter Reihenfolge.",
                "Es verarbeitet die Eingabesequenz parallel."
            ],
            "correct_index": 1,
            "explanation": "Ein bidirektionales RNN verarbeitet die Sequenz sowohl vorwärts als auch rückwärts, um Abhängigkeiten aus beiden Richtungen zu erfassen."
        },
        {
            "question": "Warum können bidirektionale RNNs die Leistung verbessern?",
            "options": [
                "Weil sie die Trainingszeit verkürzen.",
                "Weil sie unterschiedliche Repräsentationen der Daten nutzen.",
                "Weil sie die Anzahl der Parameter reduzieren.",
                "Weil sie die Klassifikationsgenauigkeit direkt erhöhen."
            ],
            "correct_index": 1,
            "explanation": "Bidirektionale RNNs lernen aus vergangenem und zukünftigem Kontext, wodurch sie komplexere Beziehungen in Sequenzdaten erfassen können."
        },
        {
            "question": "Warum ist es wichtig, zuerst einfache Modelle auszuprobieren?",
            "options": [
                "Weil sie schneller trainiert werden können.",
                "Weil sie eine Basis für die Erklärung der Nutzung eines komplexeren Modells bieten.",
                "Weil sie weniger Parameter haben.",
                "Weil sie immer die besten Ergebnisse liefern."
            ],
            "correct_index": 1,
            "explanation": "Einfache Modelle sind oft eine gute Grundlage für Experimente, um die Notwendigkeit komplexerer Architekturen zu verstehen."
        },
        {
            "question": "Welche Art von Dropout sollte in RNNs angewendet werden?",
            "options": [
                "Zufälliges Dropout",
                "Zeitlich konstantes Dropout",
                "Kein Dropout",
                "Nur Dropout auf die Eingabeschicht"
            ],
            "correct_index": 1,
            "explanation": "Zeitlich konstantes Dropout wird über mehrere Zeitschritte beibehalten, um die Stabilität und Robustheit der rekurrenten Schichten zu verbessern."
        },
        {
            "question": "Wann sind bidirektionale RNNs möglicherweise nicht geeignet?",
            "options": [
                "Wenn die jüngste Vergangenheit viel informativer ist als der Beginn der Sequenz",
                "Wenn man Voraussagen treffen möchte, basierend auf die Vergangenheit",
                "Wenn es sich um Textdaten handelt",
                "Wenn die Sequenz in umgekehrter Reihenfolge verarbeitet werden soll"
            ],
            "correct_index": 0,
            "explanation": "Bidirektionale RNNs sind nicht ideal, wenn die aktuellsten Informationen aus der Sequenz relevanter sind als der frühere Kontext."
        },
        {
            "question": "Was ist ein Tensor im Kontext von Deep Learning?",
            "options": [
                "Eine spezielle Aktivierungsfunktion",
                "Ein Container für numerische Daten",
                "Ein Optimierungsverfahren",
                "Ein neuronales Netz"
            ],
            "correct_index": 1,
            "explanation": "Ein Tensor ist eine Datenstruktur, die numerische Werte speichert und in neuronalen Netzwerken für Berechnungen verwendet wird."
        },
        {
            "question": "Wie nennt man einen Tensor mit nur einer Zahl?",
            "options": [
                "Vektor",
                "Matrix",
                "Skalar",
                "Tabelle"
            ],
            "correct_index": 2,
            "explanation": "Ein Skalar ist ein Tensor mit nur einer Zahl und stellt die einfachste Form eines Tensors dar."
        },
        {
            "question": "Woraus besteht ein 2D-Tensor typischerweise?",
            "options": [
                "Aus einer Liste von Skalaren",
                "Aus einer Liste von Matrizen",
                "Aus einem Array von Vektoren",
                "Aus einem Array von Bildern"
            ],
            "correct_index": 2,
            "explanation": "Ein 2D-Tensor ist eine Matrix aus Vektoren und wird oft zur Speicherung von Tabellendaten oder Bildpixeln verwendet."
        },
        {
            "question": "Welcher Begriff beschreibt die Anzahl der Achsen eines Tensors?",
            "options": [
                "Tiefe",
                "Breite",
                "Rang (Rank)",
                "Größe"
            ],
            "correct_index": 2,
            "explanation": "Der Rang eines Tensors beschreibt die Anzahl der Achsen oder Dimensionen, die er besitzt."
        },
        {
            "question": "Welcher dieser Tensors hat die Form eines Würfels aus Zahlen?",
            "options": [
                "1D-Tensor",
                "2D-Tensor",
                "3D-Tensor",
                "0D-Tensor"
            ],
            "correct_index": 2,
            "explanation": "Ein 3D-Tensor ist eine erweiterte Form einer Matrix und wird häufig zur Verarbeitung von Bildern oder zeitabhängigen Daten verwendet."
        },
        {
            "question": "Welches Datenformat wird typischerweise für Zeitreihendaten (Timeseries) verwendet?",
            "options": [
                "2D-Tensor mit (samples, features)",
                "3D-Tensor mit (samples, timesteps, features)",
                "4D-Tensor mit (samples, height, width, channels)",
                "5D-Tensor mit (samples, channels, timesteps, features)"
            ],
            "correct_index": 1,
            "explanation": "Zeitreihendaten benötigen eine Sequenzdarstellung, weshalb sie meist in einem 3D-Tensor mit (samples, timesteps, features) gespeichert werden."
        },
        {
            "question": "Wie ist die typische Struktur eines 4D-Tensors für Bilddaten?",
            "options": [
                "(samples, features, labels, channels)",
                "(samples, channels, height, width)",
                "(samples, timesteps, channels)",
                "(features, samples, height, width)"
            ],
            "correct_index": 1,
            "explanation": "Ein 4D-Tensor für Bilddaten speichert mehrere Bilder mit ihren Farbkanälen, Höhen- und Breiteninformationen."
        },
        {
            "question": "Welche Aussage über Vektordaten ist korrekt?",
            "options": [
                "Vektordaten werden immer als 1D-Tensoren gespeichert",
                "Vektordaten bestehen meist aus 3D-Tensoren",
                "Vektordaten sind in der Regel als 2D-Tensoren organisiert, mit (samples, features)",
                "Vektordaten enthalten nur Zeitangaben"
            ],
            "correct_index": 2,
            "explanation": "Vektordaten werden üblicherweise in 2D-Tensoren gespeichert, wobei jede Reihe einer Stichprobe und jede Spalte ein Feature repräsentiert."
        },
        {
            "question": "Was ist ein Hauptvorteil von 1D Convolutional Neural Networks gegenüber RNNs?",
            "options": [
                "Höhere Genauigkeit bei Sprachverarbeitung",
                "Geringerer Rechenaufwand",
                "Berücksichtigen Langzeitabhängigkeiten besser",
                "Können keine Sequenzen verarbeiten"
            ],
            "correct_index": 1,
            "explanation": "1D-CNNs sind effizienter als RNNs, da sie parallel verarbeitet werden können und weniger Rechenaufwand benötigen."
        },
        {
            "question": "Welche Aufgabe erfüllt ein 1D Convolutional Layer?",
            "options": [
                "Klassifiziert ganze Bilder",
                "Analysiert lokale Muster in Sequenzen",
                "Berechnet statistische Kennzahlen",
                "Sortiert Daten nach Zeit"
            ],
            "correct_index": 1,
            "explanation": "Ein 1D-CNN analysiert lokale Muster in sequenziellen Daten und kann beispielsweise für Sprachverarbeitung verwendet werden."
        },
        {
            "question": "Was beschreibt 'Translation Invariance' bei CNNs?",
            "options": [
                "Fähigkeit, Muster unabhängig von ihrer Position zu erkennen",
                "Fähigkeit, Wörter zwischen Sprachen zu übersetzen",
                "Anpassung der Lernrate über Zeit",
                "Reduktion der Trainingszeit"
            ],
            "correct_index": 0,
            "explanation": "Translation Invariance ermöglicht CNNs, Muster unabhängig von ihrer Position im Input zu erkennen."
        },
        {
            "question": "Was bewirkt eine Pooling-Schicht im Zusammenhang mit 1D CNNs?",
            "options": [
                "Verstärkt Signale",
                "Fügt Rauschen hinzu",
                "Reduziert die Sequenzlänge",
                "Wandelt Text in Zahlen um"
            ],
            "correct_index": 2,
            "explanation": "Pooling reduziert die Sequenzlänge, indem es die wichtigsten Informationen extrahiert und weniger relevante Daten verwirft."
        },
        {
            "question": "Was ist ein Nachteil von 1D CNNs im Vergleich zu RNNs?",
            "options": [
                "Höherer Speicherverbrauch",
                "Unfähigkeit, Reihenfolge global zu berücksichtigen",
                "Nur für Bilder geeignet",
                "Sehr langsam in der Verarbeitung"
            ],
            "correct_index": 1,
            "explanation": "1D-CNNs erfassen lokale Muster, sind aber nicht gut darin, globale Sequenzabhängigkeiten zu lernen wie RNNs."
        },
        {
            "question": "Welche Layer werden oft am Ende eines 1D CNN verwendet, um Klassifikation zu ermöglichen?",
            "options": [
                "Recurrent Layers",
                "Dense Layers",
                "Embedding Layers",
                "Batch-Normalization-Layers"
            ],
            "correct_index": 1,
            "explanation": "Dense Layers werden häufig am Ende eines 1D-CNNs genutzt, um die extrahierten Features für eine Klassifikation zu verwenden."
        },
        {
            "question": "Was beschreibt ein 'Window' bei einer 1D Convolution?",
            "options": [
                "Ein Modellparameter",
                "Ein Trainingsdatensatz",
                "Ein lokaler Abschnitt der Eingabesequenz",
                "Ein Visualisierungstool"
            ],
            "correct_index": 2,
            "explanation": "Ein 'Window' beschreibt den Bereich der Eingabe, den ein CNN-Filter auf einmal verarbeitet."
        },
        {
            "question": "Was passiert bei Max-Pooling in einer 1D Sequenz?",
            "options": [
                "Mittelwertbildung über alle Werte",
                "Auswahl des höchsten Werts in einem Patch",
                "Duplizieren von Sequenzteilen",
                "Addition aller Patches"
            ],
            "correct_index": 1,
            "explanation": "Max-Pooling wählt den höchsten Wert innerhalb eines festgelegten Bereichs aus, um die wichtigsten Merkmale zu erhalten."
        },
        {
            "question": "Welche Eigenschaft unterscheidet RNNs von 1D CNNs?",
            "options": [
                "RNNs sind translational invariant",
                "RNNs verarbeiten Daten ohne Reihenfolge",
                "RNNs sind auf die Reihenfolge der Eingaben sensitiv",
                "RNNs verwenden keine Gewichtungen"
            ],
            "correct_index": 2,
            "explanation": "RNNs sind auf die Reihenfolge der Eingaben sensitiv, während 1D-CNNs Muster unabhängig von ihrer Position analysieren."
        },
        {
            "question": "Was kann eine Kombination aus CNN und RNN ermöglichen?",
            "options": [
                "Schnelleres Training ohne Qualitätsverlust",
                "Gleichzeitige Text- und Bildverarbeitung",
                "Berücksichtigung von Reihenfolge bei langen Sequenzen",
                "Automatische Hyperparameterwahl"
            ],
            "correct_index": 2,
            "explanation": "Durch die Kombination von CNNs und RNNs kann sowohl lokale Mustererkennung als auch globale Sequenzabhängigkeiten genutzt werden."
        },
        {
            "question": "Welche Art von Daten eignet sich typischerweise NICHT für 1D CNNs?",
            "options": [
                "Tonaufnahmen",
                "Zeitreihen",
                "Texte",
                "Farbbilder"
            ],
            "correct_index": 3,
            "explanation": "1D CNNs sind für sequenzielle Daten gedacht und nicht für Farbbilder, die besser mit 2D- oder 3D-CNNs verarbeitet werden."
        },
        {
            "question": "Was ist eine wichtige Designentscheidung bei 1D CNNs?",
            "options": [
                "Anzahl der LSTM-Zellen",
                "Fenstergröße (Kernel size)",
                "Reihenfolge der Wörter",
                "Verwendung von Backpropagation"
            ],
            "correct_index": 1,
            "explanation": "Die Fenstergröße (Kernel size) bestimmt, welche Muster das 1D CNN lernen kann, indem sie die Größe der lokal betrachteten Eingabebereiche steuert."
        },
        {
            "question": "Warum nutzt man in der Praxis oft mehrere gestapelte Convolution- und Pooling-Schichten?",
            "options": [
                "Zur Visualisierung von Eingabedaten",
                "Um Speicherplatz zu sparen",
                "Um komplexere und längerfristige Muster zu erkennen",
                "Um die Lernrate konstant zu halten"
            ],
            "correct_index": 2,
            "explanation": "Mehrere Schichten erlauben es dem Netzwerk, von einfachen zu komplexen Mustern zu lernen und hierarchische Informationen zu erfassen."
        },
        {
            "question": "Was ist das Grundprinzip eines Multi-Input Modells?",
            "options": [
                "Nutzung eines einzelnen Datentyps",
                "Kombination verschiedener Eingangsdaten in einem Modell",
                "Verwendung eines einzigen Neurons",
                "Reduktion des Speichers"
            ],
            "correct_index": 1,
            "explanation": "Multi-Input-Modelle kombinieren mehrere Eingabedatenströme, um aus verschiedenen Quellen Informationen zu lernen."
        },
        {
            "question": "Welche Technik wird verwendet, um unterschiedliche Input-Datenströme zusammenzuführen?",
            "options": [
                "Dropout",
                "Add oder Concatenate Layer",
                "Batch Normalization",
                "Activation Layer"
            ],
            "correct_index": 1,
            "explanation": "Add oder Concatenate Layer ermöglichen das Zusammenführen von mehreren Eingabequellen in einem neuronalen Netzwerk."
        },
        {
            "question": "Was ermöglicht ein Multi-Input Modell?",
            "options": [
                "Einsatz von nur einem Datentyp",
                "Nutzung mehrerer unabhängiger Datenquellen",
                "Reduktion der Modellgröße",
                "Entfernen von Bias"
            ],
            "correct_index": 1,
            "explanation": "Multi-Input Modelle erlauben die Verarbeitung verschiedener Datenformate gleichzeitig und verbessern so die Vorhersagegenauigkeit."
        },
        {
            "question": "Wie funktioniert die naive Methode zur Kombination multimodaler Inputs?",
            "options": [
                "Ignorieren einzelner Datenquellen",
                "Training separater Modelle mit anschließender Mittelung der Vorhersagen",
                "Reduktion der Anzahl der Inputs",
                "Verstärkung einzelner Features"
            ],
            "correct_index": 1,
            "explanation": "Die naive Methode trainiert separate Modelle für unterschiedliche Inputs und kombiniert anschließend die Ergebnisse."
        },
        {
            "question": "Warum gilt das naive Verfahren bei Multi-Input Modellen als nachteilig?",
            "options": [
                "Es benötigt zu viele Daten",
                "Es erkennt keine Korrelationen zwischen den Eingaben",
                "Es verhindert Training",
                "Es nutzt zu viele Layer"
            ],
            "correct_index": 1,
            "explanation": "Beim naiven Verfahren gehen Beziehungen zwischen den Eingaben verloren, da sie separat trainiert werden."
        },
        {
            "question": "Was zeichnet Multi-Output Modelle aus?",
            "options": [
                "Sie erzeugen nur eine einzelne Vorhersage",
                "Sie können mehrere Zielattribute gleichzeitig vorhersagen",
                "Sie arbeiten nur mit Bildern",
                "Sie sind auf Audio beschränkt"
            ],
            "correct_index": 1,
            "explanation": "Multi-Output Modelle erlauben die gleichzeitige Vorhersage mehrerer Ziele in einer einzigen Modellarchitektur."
        },
        {
            "question": "Warum kann ein Multi-Output Modell Vorteile gegenüber mehreren Einzelmodellen haben?",
            "options": [
                "Geringere Trainingsdaten",
                "Gemeinsames Lernen von Zusammenhängen zwischen den Zielattributen",
                "Komplettes Vermeiden von Dropout",
                "Reduzierung der Anzahl an GPUs"
            ],
            "correct_index": 1,
            "explanation": "Ein Multi-Output Modell kann Beziehungen zwischen mehreren Zielvariablen gemeinsam lernen, wodurch es effizienter wird."
        },
        {
            "question": "Wie werden Verluste in einem Multi-Output Modell behandelt?",
            "options": [
                "Sie werden einzeln pro Zielattribut berechnet",
                "Es wird ein Gesamtverlust über alle Ausgaben gebildet",
                "Es wird eine gewichtete Gesamtverlust als Summe über alle Verlustfunktionen der einzelnen Zielattribute",
                "Nur der größte Verlust zählt"
            ],
            "correct_index": 2,
            "explanation": "Bei Multi-Output Modellen werden die Verluste der einzelnen Ziele summiert und gewichtet, um eine gemeinsame Optimierung zu ermöglichen."
        },
        {
            "question": "Welche Herausforderung besteht bei Multi-Input Modellen?",
            "options": [
                "Die Daten müssen die gleiche Form haben",
                "Unterschiedliche Eingabestrukturen müssen sinnvoll integriert werden",
                "Nur Bilddaten sind erlaubt",
                "Keine"
            ],
            "correct_index": 1,
            "explanation": "Multi-Input Modelle müssen verschiedene Datenformate verarbeiten und kombinieren, was eine sinnvolle Architektur erfordert."
        },
        {
            "question": "Was ist ein Vorteil von Multi-Input Modellen im Vergleich zu klassischen Modellen?",
            "options": [
                "Sie reduzieren die Anzahl der Epochen",
                "Sie ermöglichen die gleichzeitige Verarbeitung verschiedener Datenformate",
                "Sie verhindern alle Fehler",
                "Sie benötigen keine Labels"
            ],
            "correct_index": 1,
            "explanation": "Multi-Input Modelle können Daten aus verschiedenen Quellen gleichzeitig verarbeiten, was die Vorhersagen verbessert."
        },
        {
            "question": "Welche Aussage ist korrekt für ein Multi-Output Modell?",
            "options": [
                "Alle Ausgaben sind unabhängig",
                "Korrelationen zwischen Zielattributen können genutzt werden",
                "Nur ein Zielattribut wird gleichzeitig vorhergesagt",
                "Modelle sind auf Textdaten beschränkt"
            ],
            "correct_index": 1,
            "explanation": "Multi-Output Modelle können Abhängigkeiten zwischen den verschiedenen Zielwerten nutzen, um genauere Vorhersagen zu treffen."
        },
        {
            "question": "Wofür stehen die Begriffe 'Multiple Inputs' und 'Multiple Outputs'?",
            "options": [
                "Für sequentielle Daten",
                "Für kombinierte Nutzung mehrerer Eingaben und Vorhersage mehrerer Ziele",
                "Für Zufallsergebnisse",
                "Für Layer-Normalisierung"
            ],
            "correct_index": 1,
            "explanation": "Diese Begriffe beschreiben Modelle, die mehrere Eingabequellen oder mehrere Zielvariablen gleichzeitig verarbeiten."
        },
        {
            "question": "Was passiert, wenn mehrere Modelle in der naiven Multi-Input Methode trainiert werden?",
            "options": [
                "Jedes Modell wird separat trainiert und das Ergebnis gemittelt",
                "Es wird nur ein Modell trainiert",
                "Die Modelle verhindern sich gegenseitig",
                "Das Training wird abgebrochen"
            ],
            "correct_index": 0,
            "explanation": "Beim naiven Ansatz werden verschiedene Modelle separat trainiert, und ihre Vorhersagen werden am Ende kombiniert."
        },
        {
            "question": "Welche Aussage trifft auf Multi-Input Modelle zu?",
            "options": [
                "Sie nutzen immer nur eine einzige Datenquelle",
                "Sie erfordern zwingend Bilddaten",
                "Sie ermöglichen die Verarbeitung verschiedener Datenquellen im gleichen Modell",
                "Sie ersetzen vollständig CNNs"
            ],
            "correct_index": 2,
            "explanation": "Multi-Input Modelle kombinieren unterschiedliche Eingabequellen, wodurch sie flexibler als klassische Modelle sind."
        },
        {
            "question": "Eine Residualverbindung besteht darin, frühere Darstellungen in den nachgelagerten Datenfluss wieder einzuspeisen, sodass die Ausgabe ...",
            "options": [
                "nur die ursprüngliche Eingabe enthält",
                "nur die Transformation durch die Schicht enthält",
                "sowohl die ursprüngliche Eingabe als auch die Transformation durch die Schicht enthält",
                "entweder die ursprüngliche Eingabe oder die Transformation durch die Schicht enthält"
            ],
            "correct_index": 2,
            "explanation": "Residualverbindungen ermöglichen es, die ursprünglichen Eingaben direkt an spätere Schichten weiterzugeben, wodurch das Lernen erleichtert wird."
        },
        {
            "question": "Was ist die Hauptidee hinter dem Attention-Mechanismus?",
            "options": [
                "Alle Input-Teile gleichmäßig zu gewichten",
                "Bestimmten Teilen des Inputs mehr Bedeutung beizumessen als anderen",
                "Die Input-Sequenz zu verkürzen",
                "Die Dimensionalität der Input-Daten zu erhöhen"
            ],
            "correct_index": 1,
            "explanation": "Der Attention-Mechanismus konzentriert sich gezielt auf relevante Teile der Eingabe, um komplexe Muster besser zu erfassen."
        },
        {
            "question": "Was ermöglicht der Attention-Mechanismus einem Modell in Bezug auf die Input Features?",
            "options": [
                "Nur das erste Feature der Sequence zu berücksichtigen",
                "Features kontextbewusst zu interpretieren",
                "Die Anzahl der Features zu reduzieren",
                "Alle Features zufällig zu gewichten"
            ],
            "correct_index": 1,
            "explanation": "Mit Attention kann das Modell relevante Features stärker gewichten und kontextabhängige Beziehungen besser lernen."
        },
        {
            "question": "Wozu dient der erste Schritt im Self-Attention Mechanismus, wenn man beispielsweise das Wort 'station' in einem Satz betrachtet?",
            "options": [
                "Die grammatikalische Rolle von 'station' zu bestimmen",
                "Die Relevancy Scores zwischen 'station' und jedem anderen Wort im Satz zu berechnen",
                "Die häufigsten Wörter neben 'station' zu finden",
                "'station' durch ein Synonym zu ersetzen"
            ],
            "correct_index": 1,
            "explanation": "Der Self-Attention Mechanismus berechnet die Relevanz jedes Wortes relativ zu anderen Wörtern, um kontextabhängige Beziehungen zu erfassen."
        },
        {
            "question": "Was repräsentiert der resultierende Vektor nach Anwendung von Self-Attention auf ein Wort?",
            "options": [
                "Eine isolierte Darstellung des Wortes",
                "Eine kontextualisierte Darstellung des Wortes unter Berücksichtigung seines Surrounding Contexts",
                "Die semantische Ähnlichkeit zu einem festen Ankerwort",
                "Die Frequenz des Wortes im gesamten Dataset"
            ],
            "correct_index": 1,
            "explanation": "Nach der Anwendung von Self-Attention enthält der resultierende Vektor kontextuelle Informationen über das Wort."
        },
        {
            "question": "Was bedeutet der Begriff 'Multi-Head' im Kontext von Multi-Head Attention?",
            "options": [
                "Das Modell hat mehrere Output Layers",
                "Der Self-Attention Layer operiert auf mehreren unabhängigen Repräsentationen (Sub-Spaces) gleichzeitig",
                "Es werden mehrere verschiedene Attention-Mechanismen kombiniert",
                "Das Modell kann mehrere Sprachen gleichzeitig verarbeiten"
            ],
            "correct_index": 1,
            "explanation": "Multi-Head Attention ermöglicht parallele Berechnungen in verschiedenen Sub-Spaces, um vielfältige Beziehungen zu erfassen."
        },
        {
            "question": "Welchen Vorteil hat die Verwendung von unabhängigen 'Heads' in Multi-Head Attention?",
            "options": [
                "Jeder Head lernt, die gleiche Art von Features zu erkennen, um die Robustheit zu erhöhen",
                "Es hilft dem Layer, verschiedene Gruppen von Features oder Beziehungen für jedes Token zu lernen",
                "Es reduziert den Speicherbedarf des Modells",
                "Es vereinfacht die mathematische Formulierung der Attention"
            ],
            "correct_index": 1,
            "explanation": "Unabhängige 'Heads' erlauben es, verschiedene Beziehungen oder Aspekte eines Tokens gleichzeitig zu erfassen."
        },
        {
            "question": "Was ermöglicht es einem Transformer, die Beziehung zwischen Wörtern zu verstehen, die weit voneinander entfernt in einem Satz stehen?",
            "options": [
                "Die rekursive Struktur des Modells",
                "Der Self-Attention Mechanismus, der alle Wortpaare direkt vergleicht",
                "Ein fester Context Window Ansatz",
                "Die Verwendung von Convolutional Layers"
            ],
            "correct_index": 1,
            "explanation": "Durch Self-Attention kann ein Transformer die Beziehung zwischen Wörtern unabhängig von ihrer Position analysieren."
        },
        {
            "question": "Was ist der Hauptzweck des Transformer-Encoders?",
            "options": [
                "Text in Sprache umzuwandeln",
                "Eine Eingabesequenz in eine kontextbewusste Repräsentation zu überführen",
                "Zufällige Textgenerierung",
                "Bilderkennung"
            ],
            "correct_index": 1,
            "explanation": "Ein Transformer-Encoder verarbeitet eine Sequenz und erzeugt eine kontextbewusste Repräsentation, die später von einem Decoder genutzt wird."
        },
        {
            "question": "Was ist eine Residual Connection im Transformer-Encoder?",
            "options": [
                "Eine Technik zur Optimierung von Verlustfunktionen",
                "Eine Methode zur Rechenzeitverkürzung",
                "Eine Verbindung, die den ursprünglichen Input beibehält und addiert",
                "Eine Art von Dropout-Verfahren"
            ],
            "correct_index": 2,
            "explanation": "Residual Connections helfen, Informationen direkt über Layer hinweg zu erhalten und erleichtern das Lernen tiefer Netzwerke."
        },
        {
            "question": "Was macht die Multi-Head Attention im Transformer-Encoder?",
            "options": [
                "Rechnet nur den Mittelwert von Eingabewerten",
                "Erzeugt eine einfache gewichtete Summe",
                "Führt mehrere parallele Selbstaufmerksamkeiten durch",
                "Führt eine lineare Transformation durch"
            ],
            "correct_index": 2,
            "explanation": "Multi-Head Attention berechnet mehrere parallele Aufmerksamkeitsscores, um vielfältige Beziehungen im Input zu erfassen."
        },
        {
            "question": "Wozu dient Positional Encoding in einem Transformer?",
            "options": [
                "Um die Länge einer Sequenz zu erhöhen",
                "Um Wortbedeutungen zu normalisieren",
                "Um Positionsinformationen in die Eingabedaten zu integrieren",
                "Um Stoppwörter zu entfernen"
            ],
            "correct_index": 2,
            "explanation": "Positional Encoding sorgt dafür, dass der Transformer Reihenfolgeinformationen beibehält, da er keine rekurrente Struktur hat."
        },
        {
            "question": "Was passiert, wenn Positional Encoding weggelassen wird?",
            "options": [
                "Das Modell kann Reihenfolgeinformationen nicht berücksichtigen",
                "Das Modell funktioniert besser",
                "Der Speicherbedarf sinkt",
                "Der Output ist immer zufällig"
            ],
            "correct_index": 0,
            "explanation": "Ohne Positional Encoding verliert ein Transformer die Fähigkeit, Reihenfolgeinformationen sinnvoll zu nutzen."
        },
        {
            "question": "Wofür wurden Transformer ursprünglich entwickelt?",
            "options": [
                "Textklassifikation",
                "Bildverarbeitung",
                "Maschinelle Übersetzung",
                "Clustering"
            ],
            "correct_index": 2,
            "explanation": "Transformer wurden ursprünglich für maschinelle Übersetzung entwickelt, um effiziente und kontextuelle Textverarbeitung zu ermöglichen."
        },
        {
            "question": "Welche beiden Hauptkomponenten hat ein Transformer-Modell?",
            "options": [
                "Attention-Modul und CNN",
                "Input-Schicht und LSTM",
                "Encoder und Decoder",
                "Klassifikator und Regulator"
            ],
            "correct_index": 2,
            "explanation": "Ein Transformer besteht aus einem Encoder, der Eingaben verarbeitet, und einem Decoder, der Vorhersagen generiert."
        },
        {
            "question": "Was geschieht während der Inferenzphase eines Seq2Seq-Modells?",
            "options": [
                "Die Ausgabe wird direkt aus dem Zieltext gelesen",
                "Die Zielsequenz wird komplett vorausgeladen",
                "Die Ausgabe wird Schritt für Schritt generiert",
                "Die Decoder-Schicht wird übersprungen"
            ],
            "correct_index": 2,
            "explanation": "Während der Inferenz generiert der Decoder Wort für Wort basierend auf bisherigen Outputs, anstatt die ganze Sequenz auf einmal vorherzusagen."
        },
        {
            "question": "Welche Rolle spielt der Decoder im Transformer-Modell?",
            "options": [
                "Kodiert den Quelltext",
                "Normalisiert die Positionsembeddings",
                "Generiert neue Tokens auf Basis von Eingabesequenz und bisherigen Tokens",
                "Extrahiert Schlüsselwörter"
            ],
            "correct_index": 2,
            "explanation": "Der Decoder erstellt die Ausgabe, indem er auf bereits generierte Tokens und die Encoder-Daten zugreift."
        },
        {
            "question": "Was versucht der Decoder vorherzusagen?",
            "options": [
                "Alle Tokens gleichzeitig",
                "Vorheriges Token",
                "Token N+1 basierend auf Tokens 0 bis N",
                "Ein zufälliges Token"
            ],
            "correct_index": 2,
            "explanation": "Der Decoder generiert das nächste Token Schritt für Schritt basierend auf den bisherigen Tokens und den Encoder-Daten."
        },
        {
            "question": "Was wäre die Folge, wenn der Decoder während des Trainings vollen Zugriff auf die gesamte Zielsequenz hätte?",
            "options": [
                "Schnellere Konvergenz",
                "Overfitting",
                "Perfekte Trainingsgenauigkeit, aber nutzlose Inferenz",
                "Underfitting"
            ],
            "correct_index": 2,
            "explanation": "Wenn der Decoder Zugriff auf die gesamte Zielsequenz hätte, würde er lernen, sich darauf zu verlassen, anstatt die Sequenz selbst zu generieren."
        },
        {
            "question": "Welcher Mechanismus verwendet der Transformer-Encoder, um den Kontext zu berechnen?",
            "options": [
                "Rekurrentes Gedächtnis",
                "Self-Attention",
                "Convolutional-Filter",
                "Pooling"
            ],
            "correct_index": 1,
            "explanation": "Self-Attention ist der Hauptmechanismus des Transformer-Encoders, mit dem er relevante Teile des Inputs effizient identifiziert."
        },
        {
            "question": "Warum ermöglichen Transformer eine parallele Verarbeitung?",
            "options": [
                "Weil sie rekurrente Strukturen nutzen",
                "Weil sie keine Sequenzen explizit speichern müssen",
                "Weil sie durch Self-Attention keine Wort-für-Wort Verarbeitung benötigen",
                "Weil sie die Lernrate konstant halten"
            ],
            "correct_index": 2,
            "explanation": "Dank Self-Attention können Transformer die gesamte Sequenz parallel verarbeiten, anstatt sie Schritt für Schritt zu durchlaufen."
        }
    ]


















# Lern-App starten
if __name__ == "__main__":
    app = LernApp(fragen)
    app.start()
