def Lriichi(t, discards, exact_matches):
    if t in discards:
        return 0


def Lnext(t, discards, exact_matches):
    pass


def Lnormal(discards, exact_matches):
    return 1 / (1 + 2 * exact_matches)


def defLoss(t, wallamt):
    end = 1
    p1_discards = []
    p2_discards = []
    p3_discards = []
    exact_matches = p1_discards.count(t) + p2_discards.count(t) + p3_discards.count(t)

    if p1_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnext(t, p1_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p1_discards, exact_matches)

    if p2_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnormal(p2_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p2_discards, exact_matches)

    if p3_discards:  # Should actually check if player is in riichi
        end *= 1 - Lnormal(p3_discards, exact_matches)
    else:
        end *= 1 - Lriichi(t, p3_discards, exact_matches)

    return 1 - (1 - (wallamt / 70)) * end
