class Event(object):
    def __init__(self, type, data):
        self.type = type
        self.data = data

class Damas(object):
    SIZE = 10
    SKINS = ["o", "x"]
    valid_moves = None
    print('movimentos validos são: ', valid_moves)

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

    def dirty_moves(self, i, j, skin):

        dirty_moves = None
        if skin == Damas.SKINS[0]:
            dirty_moves = [(i - 1, j + 1), (i - 1, j - 1)]
        elif skin == Damas.SKINS[1]:
            dirty_moves = [(i + 1, j - 1), (i + 1, j + 1)]

        return dirty_moves

    def simple_moves(self, i, j, skin):
        # dirty_moves = None
        # if skin == Damas.SKINS[0]:
        #     dirty_moves = [(i - 1, j + 1), (i - 1, j - 1)]
        # elif skin == Damas.SKINS[1]:
        #     dirty_moves = [(i + 1, j - 1), (i + 1, j + 1)]
        dirty_moves = self.dirty_moves(i, j, skin)

        print(i, j)
        print(dirty_moves)
        valid_moves = []
        for x, y in dirty_moves:
            if 0 <= x < Damas.SIZE and 0 <= y < Damas.SIZE:
                print('movimentos sujos',dirty_moves)
                # if dirty_moves[0] != None or dirty_moves[1] != None:
                #     print('da pra ir')
                if not self.__tab[x][y]:
                    valid_moves.append((x, y))

        return valid_moves

    def handle_click(self, i, j):
        events = []
        dirty_moves = self.dirty_moves(i, j, self.__tab[i][j])
        for x, y in dirty_moves:
            if 0 <= x < Damas.SIZE and 0 <= y < Damas.SIZE:
                print('valor com not',not self.__tab[x][y])
                print('valor sem not',  self.__tab[x][y])
                if self.__tab[x][y] == None:
                    events.append(Event('seleciona peca', {"data": {"i": i, "j": j}}))
                    moves = self.simple_moves(i, j, self.__tab[i][j])
                    print('Movimentos: ', moves)

        for m in moves:
            events.append(Event('seleciona casa', {"data": {"i": m[0], "j": m[1]}}))
        return events
