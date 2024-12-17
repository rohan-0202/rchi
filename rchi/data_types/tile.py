from dataclasses import dataclass
from typing import Optional

from rich import print

from rchi.data_types.dragons import Dragon
from rchi.data_types.suits import Suit
from rchi.data_types.winds import Wind


@dataclass
class Tile:
    """
    A dataclass for a tile in riichi mahjong.
    """

    index: int  # 0-33
    suit: Suit
    number: Optional[int] = None  # 1-9 for numbered suits, None for honors
    wind: Optional[Wind] = None  # Only for wind tiles
    dragon: Optional[Dragon] = None  # Only for dragon tiles

    def __post_init__(self):
        # Validation
        if not 0 <= self.index <= 33:
            raise ValueError(f"Index must be between 0 and 33, got {self.index}")

        # For numbered suits
        if self.suit in [Suit.CHARACTERS, Suit.CIRCLES, Suit.BAMBOO]:
            if self.number is None or not 1 <= self.number <= 9:
                raise ValueError(
                    f"Number tiles must have a value 1-9, got {self.number}"
                )
            if self.wind is not None or self.dragon is not None:
                raise ValueError("Number tiles cannot have wind or dragon values")

        # For wind tiles
        elif self.suit == Suit.WINDS:
            if self.wind is None:
                raise ValueError("Wind tiles must have a wind value")
            if self.number is not None or self.dragon is not None:
                raise ValueError("Wind tiles cannot have number or dragon values")

        # For dragon tiles
        elif self.suit == Suit.DRAGONS:
            if self.dragon is None:
                raise ValueError("Dragon tiles must have a dragon value")
            if self.number is not None or self.wind is not None:
                raise ValueError("Dragon tiles cannot have number or wind values")

    def __str__(self):
        if self.number:
            return f"{self.number} of {self.suit}"
        elif self.wind:
            return f"{self.wind} Wind"
        else:
            return f"{self.dragon} Dragon"


# Create the mapping dictionary
TILES = {
    # Characters (0-8)
    **{i: Tile(i, Suit.CHARACTERS, number=i + 1) for i in range(9)},
    # Circles (9-17)
    **{i: Tile(i, Suit.CIRCLES, number=i - 8) for i in range(9, 18)},
    # Bamboo (18-26)
    **{i: Tile(i, Suit.BAMBOO, number=i - 17) for i in range(18, 27)},
    # Winds (27-30)
    27: Tile(27, Suit.WINDS, wind=Wind.EAST),
    28: Tile(28, Suit.WINDS, wind=Wind.SOUTH),
    29: Tile(29, Suit.WINDS, wind=Wind.WEST),
    30: Tile(30, Suit.WINDS, wind=Wind.NORTH),
    # Dragons (31-33)
    31: Tile(31, Suit.DRAGONS, dragon=Dragon.WHITE),
    32: Tile(32, Suit.DRAGONS, dragon=Dragon.GREEN),
    33: Tile(33, Suit.DRAGONS, dragon=Dragon.RED),
}

if __name__ == "__main__":
    print(TILES)
