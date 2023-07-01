import json

from genanki import Deck, Model

from src.word import Word

USDDeck = Deck(
    1725059179,
    "Slovak::[Shared] Ultimate Slovak Declension"
)

front_card = open("static/front.html", "r")
back_card = open("static/back.html", "r")
styles = open("static/styles.css", "r")

USDModel = Model(
    1683163907,
    "Ultimate Slovak Declension",
    fields=[
        {"name": "UUID"},
        {"name": "Prompt"},
        {"name": "Similar"},
        {"name": "Notes"}
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": front_card.read(),
            "afmt": back_card.read()
        }
    ],
    css=styles.read(),
    model_type=Model.CLOZE,
    sort_field_index=1
)

front_card.close()
back_card.close()
styles.close()


def get_nouns() -> list[Word]:
    with open("static/Slovak Declension.json", "r", encoding="utf8") as file:
        nouns = [Word(data) for data in json.loads(file.read())["Nouns (ex)"]]
        return nouns


def get_adjectives() -> list[Word]:
    with open("static/Slovak Declension.json", "r", encoding="utf8") as file:
        adjectives = [Word(data) for data in json.loads(file.read())["Adjectives (ex)"]]
        return adjectives


def get_pronouns() -> list[Word]:
    with open("static/Slovak Declension.json", "r", encoding="utf8") as file:
        pronouns = [Word(data) for data in json.loads(file.read())["Pronouns (ex)"]]
        return pronouns


def get_numerals() -> list[Word]:
    with open("static/Slovak Declension.json", "r", encoding="utf8") as file:
        numerals = [Word(data) for data in json.loads(file.read())["Numerals (ex)"]]
        return numerals


def get_similar(word: Word, gender: str, number: str) -> list[Word]:
    with open("static/Slovak Declension.json", "r", encoding="utf8") as file:
        similar = [Word(data) for data in json.loads(file.read())["Similar (ex)"]]

        result: list[Word] = []

        _ = [result.append(i) for i in similar if i.word in word.similar and i.gender == gender and i.number == number]

        return result
