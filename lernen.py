import json
import random
import os

# ---- Konfiguration ----
DATA_FILE = "mc_questions_with_ids.json"
STATE_FILE = "lernstand.json"
MAX_WIDTH = 80


def load_questions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_wrong_ids": []}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def ask_question(q):
    print(f"\nFrage {q['id']}: {q['question']}")
    for i, opt in enumerate(q["options"]):
        print(f"  {i+1}. {opt}")
    try:
        answer = int(input("Deine Antwort (1–4): ")) - 1
    except:
        answer = -1

    correct = q["correct_index"]
    if answer == correct:
        print("✅ Richtig!")
        return True
    else:
        print(f"❌ Falsch! Richtige Antwort: {q['options'][correct]}")
        return False
    print()


def print_explanation(q):
    print("\n📘 Erklärung:")
    lines = wrap_text(q["explanation"], MAX_WIDTH)
    for line in lines:
        print("  " + line)
    print()


def wrap_text(text, width):
    import textwrap
    return textwrap.wrap(text, width)


def select_questions(questions, mode, count, last_wrong_ids):
    if mode == "1":
        return random.sample(questions, count)
    elif mode == "2":
        filtered = [q for q in questions if q["id"] in last_wrong_ids]
        if not filtered:
            print("⚠️ Keine falschen Fragen vorhanden. Zufallsmodus wird verwendet.")
            return random.sample(questions, count)
        return random.sample(filtered, min(count, len(filtered)))
    else:
        print("Ungültiger Modus. Standard: Zufällig")
        return random.sample(questions, count)


def main():
    questions = load_questions()
    state = load_state()

    print("\n🧠 Willkommen zum Lernmodus Deep Learning\n")
    print("1 = Zufällige Fragen")
    print("2 = Nur zuletzt falsch beantwortete Fragen")
    mode = input("Modus wählen (1/2): ").strip()
    try:
        n = int(input("Wie viele Fragen möchtest du bearbeiten? "))
    except:
        n = 5

    quiz = select_questions(questions, mode, n, state.get("last_wrong_ids", []))
    correct = 0
    wrong_ids = []

    counter = 1
    for q in quiz:
        print(f'\n\n==================== Frage {counter} von {len(quiz)} ====================')
        is_correct = ask_question(q)
        print_explanation(q)
        if is_correct:
            correct += 1
        else:
            wrong_ids.append(q["id"])
        print(f'Zwischenstand: {correct} / {counter}')
        counter += 1

    print(f"\n🏁 Runde beendet: {correct} von {len(quiz)} richtig.")
    if wrong_ids:
        print("❗ Du hast folgende Fragen falsch beantwortet:", wrong_ids)
        again = input("Möchtest du diese sofort nochmal üben? (j/n) ").strip().lower()
        if again == "j":
            print("\n🔁 Wiederholung der falschen Fragen:")
            for q in [q for q in questions if q["id"] in wrong_ids]:
                ask_question(q)
                print_explanation(q)

    # Speichern der neuen Fehlerliste
    # 1. Vorherige falsche
    prev_wrong = set(state.get("last_wrong_ids", []))

    # 2. Neue richtige = aus dem Quiz, aber nicht falsch
    now_correct = {q["id"] for q in quiz if q["id"] not in wrong_ids}

    # 3. Neue Fehlerliste: vorherige Fehler, minus korrekt beantwortete + neue falsche
    updated_wrong = (prev_wrong - now_correct).union(wrong_ids)

    state["last_wrong_ids"] = list(updated_wrong)
    save_state(state)


if __name__ == "__main__":
    main()
