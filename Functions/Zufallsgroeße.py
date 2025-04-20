from Functions import *


def erwartungswert(xi, Pxi):
    E = 0
    i = 0
    while i <  len(xi):
        E = E + xi[i] * Pxi[i]
        i = i+1

    return E


def varianz(xi, Pxi):
    E = erwartungswert(xi, Pxi)
    i = 0
    V = 0
    while i < len(xi):
        V = V + (xi[i] - E)**2 * Pxi[i]
        i = i +1

    return V


def standardabweichung(xi, Pxi):
    return sqrt(varianz(xi, Pxi))


def tabelle_random_var(name, xi, Pxi):
    table = PrettyTable()
    table.align ="r"

    table.field_names = ["Was","Werte"]
    table.add_row(["xi", xi])
    table.add_row(["P("+name+"= xi)", Pxi])
    table.add_row(["E("+name +")", erwartungswert(xi, Pxi)])
    table.add_row(["Var("+ name +")", varianz(xi, Pxi)])
    table.add_row(["{sigma}", standardabweichung(xi, Pxi)])

    print("Tabelle für die Zufallsgröße "+ name)
    print(table)