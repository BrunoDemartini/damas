class Event(object):
    def __init__(self, type, data):
        self.type = type
        self.data = data

class Damas(object):
    SIZE = 10
    SKINS = ["o", "x"]
    valid_moves = []
    moves = None
    c = None
    s = None
    vez = 1
    jogador = None
    cor = None
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
        # print('casa selecionada: ', i, j)
        # print(dirty_moves)

        for x, y in dirty_moves:
            if 0 <= x < Damas.SIZE and 0 <= y < Damas.SIZE:
                # print('movimentos sujos',dirty_moves)
                # if dirty_moves[0] != None or dirty_moves[1] != None:
                #     print('da pra ir')
                if not self.__tab[x][y]:
                    self.valid_moves.append((x, y))

        # print('movimentos validos são: ', self.valid_moves)

        return self.valid_moves

    def handle_click(self, i, j):
        if self.vez % 2 == 0 :
            self.jogador = 'o'
            self.cor = 'red'
        else:
            self.jogador = 'x'
            self.cor = 'blue'
        events = []
        moviment = []
        dirty_moves = self.dirty_moves(i, j, self.__tab[i][j])
        if self.valid_moves == [] and self.__tab[i][j] == self.jogador:
            self.c = i
            self.s = j
            for x, y in dirty_moves:
                if 0 <= x < Damas.SIZE and 0 <= y < Damas.SIZE:
                    if self.__tab[x][y] == None:
                        events.append(Event('seleciona peca', {"data": {"i": i, "j": j}}))
                        self.moves = self.simple_moves(i, j, self.__tab[i][j])
            for m in self.moves:
                events.append(Event('seleciona casa', {"data": {"i": m[0], "j": m[1]}}))
        elif self.valid_moves != [] and self.__tab[i][j] == self.jogador or self.__tab[i][j] == None:
            self.vez = self.vez + 1
            moviment.append((i, j))
            if moviment[0] == self.valid_moves[0] or moviment[0] == self.valid_moves[1]:
                self.valid_moves = []
                for m in self.moves:
                    events.append(Event('restaura casa', {"data": {"i": m[0], "j": m[1]}}))
                events.append(Event('restaura casa', {"data": {"i": self.c, "j": self.s}}))
                events.append(Event('desenha peca', {"data": {"i": i, "j": j, "cor": self.cor}}))
                self.__tab[i][j] = self.jogador
                self.__tab[self.c][self.s] = None
        return events
