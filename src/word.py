class Word:
    word: str
    nominative: str
    genitive: str
    dative: str
    accusative: str
    locative: str
    instrumental: str
    word_class: str
    gender: str
    category: list[str]
    number: str
    similar: list[str]
    general_note: str
    nominative_note: str
    genitive_note: str
    dative_note: str
    accusative_note: str
    locative_note: str
    instrumental_note: str
    nominative_context: str
    genitive_context: str
    dative_context: str
    accusative_context: str
    locative_context: str
    instrumental_context: str

    def __init__(self, data: dict):
        self.__dict__ = data
