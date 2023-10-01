from colorama import Fore
from util.util import get_input, colored_array_print
from conversions import from_decimal, to_decimal

def main(*args, **kwargs):
    choice: int

    while True:
        getting_input = True
        print_menu()

        while getting_input:
            try:
                choice = int(input('Enter choice: '))
            except:
                print("Enter a valid input...")
                continue

            if choice in range(20):
                getting_input = False

        



def print_menu():
    print('\n*********************************************************************')
    colored_array_print("NUMBER SYSTEMS CONVERTER", Fore.GREEN, False) 

    print('''

    [0] EXIT
    [1] INSERTION SORT
    [2] MERGE SORT
    [3] QUICK SORT
    [4] SELECTION SORT
    [5] SHELL SORT
    [6] BUCKET SORT
    [7] BUBBLE SORT
    [8] COMB SORT
    [9] RADIX SORT
    [10] MAX HEAP SORT
    [11] MIN HEAP SORT
    [12] TREE SORT
    [13] TOURNAMENT SORT
    ''')

    print()
    colored_array_print("SEARCHING ALGORITHMS", Fore.RED, False)

    print('''

    [14] LINEAR SEARCH
    [15] BINARY SEARCH
    [16] JUMP SEARCH
    [17] INTERPOLATION SEARCH
    [18] TERNARY SEARCH 
    [19] EXPONENTIAL SEARCH
    ''')


if __name__ == '__main__':
    main()
