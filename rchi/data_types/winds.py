from enum import Enum
from typing import NamedTuple


class WindName(NamedTuple):
    """
    A named tuple for the wind of riichi mahjong in different languages.
    """

    english: str
    japanese: str
    chinese: str


class Wind(Enum):
    """
    An enum for the wind of riichi mahjong.
    """

    EAST = WindName("East", "Ton", "Dōng")
    SOUTH = WindName("South", "Nan", "Nán")
    WEST = WindName("West", "Shaa", "Xī")
    NORTH = WindName("North", "Pei", "Běi")

    def __str__(self):
        return f"{self.value.english}/{self.value.japanese}/{self.value.chinese}"
