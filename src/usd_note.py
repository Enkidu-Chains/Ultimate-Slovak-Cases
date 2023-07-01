from genanki import Note

from src.common import USDModel


class USDNote(Note):
    @staticmethod
    def create(uuid: str, prompt: str, similar: str, notes: str, tags: list[str]) -> 'USDNote':
        return USDNote(model=USDModel, fields=[uuid, prompt, similar, notes], tags=tags, guid=uuid)
