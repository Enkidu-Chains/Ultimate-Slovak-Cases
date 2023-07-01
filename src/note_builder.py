import re
from uuid import UUID, uuid5, NAMESPACE_DNS

from src.enums import CaseQuestion, NumberCue
from src.tags import Case
from src.templates import *
from src.usd_note import USDNote
from src.word import Word


class NoteBuilder:
    word: Word
    case: Case
    similar: list[Word]

    def __init__(self, word: Word, case: Case, similar: list[Word]) -> None:
        self.word = word
        self.case = case
        self.similar = similar

    def build(self) -> USDNote:
        return USDNote.create(str(self.__uuid()), self.__prompt(), self.__similar(), self.__notes(), self.__tags())

    def __uuid(self) -> UUID:
        return uuid5(NAMESPACE_DNS, f"{self.word.word}{self.word.gender}{self.case}{self.word.number}")

    def __prompt(self) -> str:
        case = self.case.capitalize()
        number = self.word.number
        case_questions = self.__case_question()
        number_cue = self.__number_cue()
        cloze_text = self.__formatable_context().capitalize().format(cloze=self.__cloze())

        return prompt(case=case, number=number, case_questions=case_questions,
                      number_cue=number_cue, cloze_text=cloze_text)

    def __similar(self) -> str:
        result = ""
        if self.case == Case.Nominative:
            for word in self.similar:
                result = result + similar_without_declension(word=word.word)
        else:
            for word in self.similar:
                result = result + similar_with_declension(word=word.nominative, declension=self.__declension(word))

        return result

    def __notes(self) -> str:
        word = self.word.word
        word_class = self.word.word_class
        gender = self.word.gender
        category = ", ".join(self.word.category)
        general_note = self.word.general_note
        card_note = self.__card_note()

        if self.__card_note() is not None:
            return notes_with_card_note(word=word, word_class=word_class, gender=gender, category=category,
                                        general_note=general_note, card_note=card_note)

        return notes_without_card_note(word=word, word_class=word_class, gender=gender, category=category,
                                       general_note=general_note)

    def __tags(self) -> list[str]:
        result: list[str] = [self.word.word, self.word.word_class, self.case, self.word.gender]

        if ", " in self.word.number:
            numbers: list[str] = self.word.number.split(", ")
            [result.append(number) for number in numbers]

        [result.append(category) for category in self.word.category]

        return result

    def __cloze(self) -> str:
        if self.case == Case.Nominative:
            return cloze(cloze=self.__declension(self.word), hint=self.word.word)

        return cloze(cloze=self.__declension(self.word), hint=self.word.nominative)

    def __context(self) -> str:
        match self.case:
            case Case.Nominative:
                return self.word.nominative_context
            case Case.Genitive:
                return self.word.genitive_context
            case Case.Dative:
                return self.word.dative_context
            case Case.Accusative:
                return self.word.accusative_context
            case Case.Locative:
                return self.word.locative_context
            case Case.Instrumental:
                return self.word.instrumental_context

    def __formatable_context(self) -> str:
        return re.sub(r"_+", "{cloze}", self.__context())

    def __declension(self, word: Word) -> str:
        match self.case:
            case Case.Nominative:
                return word.nominative
            case Case.Genitive:
                return word.genitive
            case Case.Dative:
                return word.dative
            case Case.Accusative:
                return word.accusative
            case Case.Locative:
                return word.locative
            case Case.Instrumental:
                return word.instrumental

    def __card_note(self) -> str | None:
        match self.case:
            case Case.Nominative:
                return self.word.nominative_note
            case Case.Genitive:
                return self.word.genitive_note
            case Case.Dative:
                return self.word.dative_note
            case Case.Accusative:
                return self.word.accusative_note
            case Case.Locative:
                return self.word.locative_note
            case Case.Instrumental:
                return self.word.instrumental_note

    def __case_question(self) -> CaseQuestion:
        match self.case:
            case Case.Nominative:
                return CaseQuestion.Nominative
            case Case.Genitive:
                return CaseQuestion.Genitive
            case Case.Dative:
                return CaseQuestion.Dative
            case Case.Accusative:
                return CaseQuestion.Accusative
            case Case.Locative:
                return CaseQuestion.Locative
            case Case.Instrumental:
                return CaseQuestion.Instrumental

    def __number_cue(self) -> NumberCue:
        match self.word.number.lower():
            case "singular":
                return NumberCue.Singular
            case "plural":
                return NumberCue.Plural
