class PrintBoard:
    def __init__(self, board_p1, board_p2):
        self.board_p1 = board_p1
        self.board_p2 = board_p2

    def __str__(self):
        res = ""
        indent = " " * 10
        numbers = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        res = "Доска компьютера:"
        res += " "*(len(numbers)-len(res)) + indent + "Доска игрока:\n" + numbers + indent + numbers
        for i, row in enumerate(self.board_p1.field):
            temp = f"\n{i + 1} | " + " | ".join(row) + " |"
            temp = temp.replace("■", "O")
            res += temp + indent + f"{i + 1} | " + " | ".join(self.board_p2.field[i]) + " |"
        return str(res)
