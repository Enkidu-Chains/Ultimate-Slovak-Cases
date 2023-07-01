from enum import StrEnum


class NumberCue(StrEnum):
    Singular = "¦"
    Plural = "¦¦"


class CaseQuestion(StrEnum):
    Nominative = " kto? čo?"
    Genitive = "koho? čoho?"
    Dative = "komu? čomu?"
    Accusative = "koho? čo?"
    Locative = "(o) kom? čom?"
    Instrumental = "kým? čím?"
