pos = 1.1
travel = "(N)orth."
no_print = True

def check_victory(p):
    if p == 3.1:
        print("Victory!")
        quit()

def east(p, printing):
    if p == 1.1 or p == 2.1 or p == 2.2 or p == 3.1 or p == 3.2 or p == 3.3:
        print("Not a valud direction!")
        printing = False
    else:
        p += 1.0
        printing = True
    return p, printing

def west(p, printing):
    if p == 1.1 or p == 1.2 or p == 2.1 or p == 1.3 or p == 3.2 or p == 3.1:
        print("Not a valid direction!")
        printing = False
    else:
        p -= 1.0
        printing = True
    return p, printing

def north(p, printing):
    if p == 1.3 or p == 2.3 or p == 3.3 or p == 2.2:
        print("Not a valid direction!")
        printing = False
    else:
        p += 0.1
        printing = True
    return p, printing

def south(p, printing):
    if p == 1.1 or p == 2.1 or p == 2.3 or p == 3.1:
        print("Not a valid direction!")
        printing = False
    else:
        p -= 0.1
        printing = True
    return p, printing

def check_direction(d, p, q):
    if d == "n":
        return north(p, q)
    elif d == "s":
        return south(p, q)
    elif d == "w":
        return west(p, q)
    elif d == "e":
        return east(p, q)
    else:
        print("Not a valid direction!")

def check_possible_directions(t):
    if round_pos == 1.1:
        t = "(N)orth."
    elif round_pos == 1.2:
        t = "(N)orth or (E)ast or (S)outh."
    elif round_pos == 2.2:
        t = "(S)outh or (W)est."
    elif round_pos == 2.1:
        t = "(N)orth."
    elif round_pos == 1.3:
        t = "(E)ast or (S)outh."
    elif round_pos == 2.3:
        t = "(E)ast or (W)est."
    elif round_pos == 3.3:
        t = "(S)outh or (W)est."
    elif round_pos == 3.2:
        t = "(N)orth or (S)outh."
    return t

while True:
    round_pos = round(pos, 1)

    check_victory(round_pos)

    travel = check_possible_directions(travel)

    if no_print:
        print("You can travel:", travel)

    direction = input("Direction: ").lower()

    pos, no_print = check_direction(direction, round_pos, no_print)
