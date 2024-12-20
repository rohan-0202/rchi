from data_types.tile import Tile


class PovPlayer:
    def verifyhand(self, hand):
        pass

    def __init__(
        self,
        seatwind,
        gamewind,
        hand: list[Tile],
        discards: list[Tile],
        melds: list[list[Tile]],
    ):
        self.wind = seatwind
        self.hand = hand
        self.discards = discards
        self.melds = melds

        # Checking Open or Closed hand
        if len(melds) == 0:
            self.closedstatus = True
        else:
            self.closedstatus = False

        # Checks if dealer
        if seatwind == gamewind:
            self.dealerstatus = True

        # Should check furiten. Probably need function for this
        for i in discards:
            if self.verifyhand(hand + i):
                self.furiten = True

    # Determine the number of steps needed for this player to win
    def n(self, hand):
        pass


class OtherPlayer:
    def __init__(
        self,
        seatwind,
        gamewind,
        discards: list[Tile],
        melds: list[list[Tile]],
        riichistatus: bool,
    ):
        self.wind = seatwind
        self.discards = discards
        self.melds = melds
        self.riichistatus = riichistatus

        # Checking Open or Closed hand
        if len(melds) == 0:
            self.closedstatus = True
        else:
            self.closedstatus = False

        # Checks if dealer
        if seatwind == gamewind:
            self.dealerstatus = True


class Game:
    def __init__(self, gamewind, dora: list[Tile], povwind, povhand):
        self.remaining_tiles = 70
        self.dora = dora
        self.players = []

        for i in [(0, "East"), (1, "South"), (2, "West"), (3, "North")]:
            if i[1] == povwind:
                self.players.append(
                    PovPlayer(
                        povwind,
                        gamewind,
                        povhand,
                        [],
                        [],
                    )
                )
            else:
                self.players.append(OtherPlayer(i[1], gamewind, [], [], False))

        self.kans = 0
