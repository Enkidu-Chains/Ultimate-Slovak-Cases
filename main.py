from src.common import *
from src.note_builder import NoteBuilder
from src.tags import Case
from src.word import Word

if __name__ == '__main__':
    words: list[Word] = []
    cases: list[Case] = [Case.Nominative, Case.Genitive, Case.Dative, Case.Accusative, Case.Locative, Case.Instrumental]

    [words.append(word) for word in get_nouns()]
    [words.append(word) for word in get_adjectives()]
    [words.append(word) for word in get_pronouns()]
    [words.append(word) for word in get_numerals()]

    for word in words:
        for case in cases:
            USDDeck.add_note(
                NoteBuilder(word=word, case=case, similar=get_similar(word, gender=word.gender, number=word.number))
                .build()
            )

    USDDeck.write_to_file("./out/Ultimate Slovak Declension.apkg")

    _words: list[str] = []

    [_words.append(_word.word) for _word in words if _word.word not in _words]

    for _word in _words:
        number_of_card: int = 0
        for word in words:
            if word.word == _word:
                number_of_card += 6
        print(f"{str(_words.index(_word) + 1).zfill(2)}. {_word.capitalize()}: {number_of_card} cards")
