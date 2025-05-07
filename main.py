from Functions import *
from Functions.Fibonacci import fibonacci
from Functions.Zufallsgroeße import tabelle_random_var

if __name__ == '__main__':
    print("┌─────┬───┐ Welcome ShellGebra. \n"
          "│     │   │ Your Personal Math Assistant in your shell.\n"
          "│     ├─┬─┤ Type help to find a menu with introductions.\n"
          "└─────┴─┴─┘")

    while True:
        user_input = input(">> ")

        if user_input == "":
            pass

        elif user_input.lower() == "exit":
            exit()

        elif user_input.lower() == "help":
            help_and_descriptions()


        elif user_input.startswith("do "):
            try:
                print(eval(str(user_input[3:])))
            except SyntaxError:
                print("Your input was not a valid equation")
            except NameError:
                print("Your input was not a valid equation")

        elif user_input.startswith("is prime "):
            try:
                print(is_prime_number(int(user_input[9:])))
            except ValueError:
                print("Your input was not a valid integer")


        elif user_input == "prime range":
            start = input("start of range ")
            end = input ("end of range ")
            try:
                print(prime_range(int(start), int(end)))
            except ValueError:
                print("Your input was not a valid integer")


        elif user_input.startswith("fib "):
            try:
                print(fibonacci(int(user_input[4:])))
            except ValueError:
                print("Your input was not a valid integer")


        elif user_input == "binom dis":
            name = input ("Name of the Experiment: ")
            n = input("The n: ")
            p = input("The p: ")
            try:
                tabelle_binom(name, int(n), float(p))
            except ValueError:
                print("Your input was not a valid integer")
            except OverflowError:
                print("Sry but the programm has an overflow error")



        else:
            print("Sorry that's not a valid command")