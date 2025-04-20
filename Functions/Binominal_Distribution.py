from Functions import *

def wahrscheinlichkeitsverteilung(n,p):
    k = 0
    Pxi = []
    while k <= n:
        binom = (factorial(n)) / ((factorial(k)) * (factorial(n - k)))
        P = binom * (p ** k) * ((1 - p) ** (n - k))
        Pxi.append(round(P, 4))
        k = k + 1
    return Pxi

def kumulative_verteilungsfunktion(n,p):
    Pxi = wahrscheinlichkeitsverteilung(n,p)
    Sum = 0
    kWF = []
    for element in Pxi:
        Sum = Sum + element
        kWF.append(Sum)
    return kWF


def erwartungswert(n,p):
    return n * p


def varianz(n,p):
    return round(n * p * (1 - p), 4)


def standardabweichung(n,p):
    return sqrt(round(varianz(n,p), 4))



def tabelle_binom(name,n,p):
    table = PrettyTable()
    table.align = "l" #aling everything to the right
    x = []
    i = 0
    while i <= n:
        x.append(i)
        i = i + 1

    table.field_names = ["What", "Values"]
    table.add_row(["xi", x])
    table.add_row(["P(" + name + "= xi)", wahrscheinlichkeitsverteilung(n,p)])
    table.add_row(["P(" + name + " <= xi)", kumulative_verteilungsfunktion(n,p)])
    table.add_row(["E(" + name + ")", erwartungswert(n,p)])
    table.add_row(["Var(" + name + ")", varianz(n,p)])
    table.add_row(["{sigma}", standardabweichung(n,p)])

    print("Tabelle für die Zufallsgröße " + name)
    print(table)


