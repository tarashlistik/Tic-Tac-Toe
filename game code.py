import random

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return False if self.value else True




class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def __check(self, value):
        if type(value) != tuple or len(value) != 2:
            raise IndexError('некорректно указанные индексы')

        if any(not (0 <= i < 3) for i in value if type(i) != slice):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check(key)
        r, c = key
        self.pole[r][c].value = value

    def init(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0

    def show(self):
        print("_____")
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=" ")
            print()
        print("_____")

    def human_go(self):
        while True:
            i, j = input("введідь координати клітки через пробіл (наприклад, '1 2'):" ).split()
            i, j = int(i), int(j)
            if not (0 <= i < 3) or not (0 <= j < 3):
                print("спобуйте ще раз")
                continue
            if self.pole[i][j].value != self.FREE_CELL:
                continue
            self.pole[i][j].value = self.HUMAN_X
            break

    def computer_go(self):
        while True:
            i, j = random.randint(0, 2), random.randint(0, 2)
            if self.pole[i][j].value != self.FREE_CELL:
                continue
            self.pole[i][j].value = self.COMPUTER_O
            break

    def __wins(self, value):
        for i in range(3):
            if self.pole[i][0].value == value and \
                    self.pole[i][1].value == value and \
                    self.pole[i][2].value == value:
                return True
            if self.pole[0][i].value == value and \
                    self.pole[1][i].value == value and \
                    self.pole[2][i].value == value:
                return True
        if self.pole[0][0].value == value and \
                self.pole[1][1].value == value and \
                self.pole[2][2].value == value:
            return True
        if self.pole[0][2].value == value and \
                self.pole[1][1].value == value and \
                self.pole[2][0].value == value:
            return True
        return False

    @property
    def is_human_win(self):
        return self.__wins(self.HUMAN_X)

    @property
    def is_computer_win(self):
        return self.__wins(self.COMPUTER_O)

    @property
    def is_draw(self):
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == self.FREE_CELL:
                    return False
        return self.is_computer_win == False and self.is_human_win == False

    def __bool__(self):
        return not (self.is_computer_win or self.is_human_win or self.is_draw)


game = TicTacToe()
game.init()
step_game = 0

while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
