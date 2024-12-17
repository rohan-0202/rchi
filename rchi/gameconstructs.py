class Tile:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value  # 123456789 if man/pin/sou, ESWN if wind, rwg if dragon


class PovPlayer:
    def __init__(
        self,
        wind,
        hand: list[Tile],
        discards: list[Tile],
        melds: [[Tile]],
        riichistatus,
    ):
        self.wind = wind
        self.hand = hand
        self.discards = discards
        self.melds = melds
        self.riichistatus = riichistatus


class OtherPlayer:
    def __init__(self, wind, discards: list[Tile], melds: [[Tile]], riichistatus):
        self.wind = wind
        self.discards = discards
        self.melds = melds
        self.riichistatus = riichistatus


class Game:
    def __init__(
        self, wind, dora: list[Tile], player: PovPlayer, opponents: [OtherPlayer]
    ):
        self.wind = wind
        self.dora = dora
        self.player = player
        self.opponents = opponents
