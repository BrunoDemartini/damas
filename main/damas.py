class Event(object):
    def __init__(self, type, data):
        self.type = type
        self.data = data

class Damas(object):
    SIZE = 10
    SKINS = ["o", "x"]

    def __init__(self):
        self.__tab = [[None, 'x', None, 'x', None, 'x', None, 'x', None, 'x'],
                      ['x', None, 'x', None, 'x', None, 'x', None, 'x', None],
                      [None, 'x', None, 'x', None, 'x', None, 'x',None, 'x'],
                      ['x', None, 'x', None, 'x', None, 'x', None, 'x', None],
                      [None, None, None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None, None, None],
                      [None, 'o', None, 'o', None, 'o', None, 'o', None, 'o'],
                      ['o', None, 'o', None, 'o', None, 'o', None, 'o', None],
                      [None, 'o', None, 'o', None, 'o', None, 'o', None, 'o'],
                      ['o', None, 'o', None, 'o', None, 'o', None, 'o', None]]
        self.__vez = Damas.SKINS[0]
        self.__selected = None

    def simple_moves(self, i, j, skin):
        dirty_moves = [(i - 1, j + 1), (i - 1, j - 1)] \
            if skin == Damas.SKINS[0] else [(i + 1, j - 1), (i + 1, j + 1)]
        print(i, j)
        print(dirty_moves)
        valid_moves = []
        for x, y in dirty_moves:
            if 0 <= x < Damas.SIZE and 0 <= y < Damas.SIZE:
                print(not self.__tab[x][y])
                if not self.__tab[x][y]:
                    valid_moves.append((x, y))
        return valid_moves

    def handle_click(self, i, j):
        events = []
        events.append(Event('seleciona peca', {"data": {"i": i, "j": j}}))
        moves = self.simple_moves(i, j, self.__tab[i][j])
        print(moves)
        for m in moves:
            events.append(Event('seleciona casa', {"data": {"i": m[0], "j": m[1]}}))
        return events
