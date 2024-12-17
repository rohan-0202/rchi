from enum import Enum
from typing import NamedTuple


class DragonName(NamedTuple):
    """
    A named tuple for the dragon of riichi mahjong in different languages.
    """

    english: str
    japanese: str
    chinese: str


class Dragon(Enum):
    """
    An enum for the dragon of riichi mahjong.
    """

    WHITE = DragonName("White", "Haku", "Bái")
    GREEN = DragonName("Green", "Hatsu", "Fā")
    RED = DragonName("Red", "Chun", "Zhōng")

    def __str__(self):
        return f"{self.value.english}/{self.value.japanese}/{self.value.chinese}"
