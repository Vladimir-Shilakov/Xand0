field = [["-"] * 3 for i in range(3)]


def rules():
    print(" -------------------- ")
    print(" Игра:Крестики-Нолики ")
    print(" -------------------- ")
    print("  Формат ввода: x, y  ")
    print("  x - номер строки    ")
    print("  y - номер стоблца   ")
    print(" -------------------- ")
    print()


def show_field():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")


def user_input():
    while True:
        coordinates = input("Ваш ход: ").split()
        if len(coordinates) != 2:
            print("Введите 2 координаты! ")
            continue

        x, y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue

        x, y = int(x), int(y)

        if 0 > x > 2 or 0 > y > 2:
            print("Неверный диапозон!")
            continue

        if field[x][y] != "-":
            print("Клетка занята!")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


count = 0


rules()
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = user_input()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Ничья!")
        break
