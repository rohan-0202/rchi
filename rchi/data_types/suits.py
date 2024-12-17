from enum import Enum
from typing import NamedTuple


class SuitName(NamedTuple):
    """
    A named tuple for the suit of riichi mahjong in different languages.
    """

    english: str
    japanese: str
    chinese: str


class Suit(Enum):
    """
    An enum for the suit of riichi mahjong.
    """

    CHARACTERS = SuitName("Characters", "Manzu", "Wànzǐ")
    CIRCLES = SuitName("Circles", "Pinzu", "Bǐnzǐ")
    BAMBOO = SuitName("Bamboo", "Souzu", "Suōzǐ")
    WINDS = SuitName("Winds", "Kazehai", "Fēngpái")
    DRAGONS = SuitName("Dragons", "Sangenpai", "Sānyuánpái")

    def __str__(self):
        return f"{self.value.english}/{self.value.japanese}/{self.value.chinese}"
