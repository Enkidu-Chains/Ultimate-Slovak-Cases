def cloze(cloze: str, hint: str) -> str:
    with open("./static/templates/cloze.html", "r", encoding="utf8") as template:
        return template.read().format(cloze=cloze, hint=hint)


def notes_with_card_note(word: str, word_class: str, gender: str, category: str, general_note: str,
                         card_note: str) -> str:
    with open("./static/templates/notes with card note.html", "r", encoding="utf8") as template:
        return template.read().format(word=word, word_class=word_class, gender=gender, category=category,
                                      general_note=general_note, card_note=card_note)


def notes_without_card_note(word: str, word_class: str, gender: str, category: str, general_note: str) -> str:
    with open("./static/templates/notes without card note.html", "r", encoding="utf8") as template:
        return template.read().format(word=word, word_class=word_class, gender=gender, category=category,
                                      general_note=general_note)


def prompt(case: str, number: str, case_questions: str, number_cue: str, cloze_text: str) -> str:
    with open("./static/templates/prompt.html", "r", encoding="utf8") as template:
        return template.read().format(case=case, number=number, case_questions=case_questions,
                                      number_cue=number_cue, cloze_text=cloze_text)


def similar_with_declension(declension: str, word: str) -> str:
    with open("./static/templates/similar with declension.html", "r", encoding="utf8") as template:
        return template.read().format(declension=declension, word=word)


def similar_without_declension(word: str) -> str:
    with open("./static/templates/similar without declension.html", "r", encoding="utf8") as template:
        return template.read().format(word=word)
