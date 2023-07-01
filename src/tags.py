from enum import StrEnum


class WordClass(StrEnum):
    Noun = "noun"
    Adjective = "adjective"
    Pronoun = "pronoun"
    Numeral = "numeral"


class Gender(StrEnum):
    Masculine = "masculine"
    Feminine = "feminine"
    Neuter = "neuter"
    Genderless = "genderless"


class Category(StrEnum):
    People = "people"
    Animals = "animals"
    Things = "things"
    Plants = "plants"
    Possessive = "possessive"
    Qualitative = "qualitative"
    Relational = "relational"
    Basic = "basic"
    Personal = "personal"
    Reflexive = "reflexive"
    Demonstrative = "demonstrative"
    Interrogative = "interrogative"
    Cardinal = "cardinal"


class Case(StrEnum):
    Nominative = "nominative"
    Genitive = "genitive"
    Dative = "dative"
    Accusative = "accusative"
    Locative = "locative"
    Instrumental = "instrumental"


class Number(StrEnum):
    Singular = "singular"
    Plural = "plural"
