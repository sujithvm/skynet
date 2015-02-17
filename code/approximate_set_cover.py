__author__ = 'Archana V Menon, Sujith V'


def approximate_set_cover(sets):

    """
    Find approximate set cover for a list of sets

    :param sets: list of sets
    :return: set cover
    :raise ValueError: when list of sets is null
    """

    if not sets:
        raise ValueError("Error : Empty list of sets")

    # find universe
    universe = set()
    for s in sets:
        universe.update(s)

    # set cover list
    set_cover = []

    # while U != 0
    while len(universe) != 0:

        # find set S that maximizes |S intersection U|
        S = set()
        for s in sets:
            if len(universe.intersection(s)) > len(S):
                S = s

        # U = U - S
        universe.difference_update(S)

        # set_cover = set_cover union S
        set_cover.append(S)

    # return
    return set_cover


if __name__ == "__main__":

    sets = [set([1, 2, 4, 9]),
     set([3, 8, 10]),
     set([9, 1]),
     set([1]),
     set([2, 3, 12]),
     set([4, 5]),
     set([5, 7, 1, 2]),
     set([5, 6, 10, 3, 4]),
     set([4, 7, 9]),
     set([6]),
     set([8, 9, 1, 4])]


    print approximate_set_cover(sets)
