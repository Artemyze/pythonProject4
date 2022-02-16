from exception import *
from dot import *
from random import randint


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    previous_turn1 = Dot
    previous_turn2 = Dot
    touches = 0
    turn = Dot

    def ask(self):
        near = [
            (-1, 0), (1, 0), (0, 1),
            (0, -1)
        ]
        while True:
            if self.enemy.killed:
                self.touches = 0
                self.rand_dot()
                break
            else:
                if self.enemy.touched:
                    self.previous_turn2 = self.previous_turn1
                    for dx, dy in near:
                        if self.enemy.field[self.previous_turn1.x + dx][self.previous_turn1.y + dy] != ".":
                            if not 0 <= self.previous_turn1.x + dx <= 6 or not 0 <= self.previous_turn1.y + dy <= 6:
                                while True:
                                    if not self.enemy.out(Dot(self.previous_turn1.x - dx, self.previous_turn1.y - dy)):
                                        dx += 1
                                        dy += 1
                                    else:
                                        break
                            self.turn = Dot(self.previous_turn1.x + dx, self.previous_turn1.y + dy)
                            self.previous_turn1 = Dot(self.previous_turn1.x + dx, self.previous_turn1.y + dy)
                            break
                    break
                else:
                    self.previous_turn1 = self.previous_turn2
                    self.enemy.touched = True
        print(f"Ход компьютера: {self.turn.x + 1} {self.turn.y + 1}")
        return self.turn

    def rand_dot(self):
        while True:
            self.turn = Dot(randint(0, 5), randint(0, 5))
            if self.turn not in self.enemy.busy:
                self.previous_turn1 = self.turn
                self.previous_turn2 = self.turn
                break


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)
