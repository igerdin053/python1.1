import random

def module2():
    name = input("Please tell me your name: ")
    print("Hi", name, end='!\n')
    num = int(input("Please enter your favorite number: "))
    print("Your number of", num , "multiplied by itsself is:", num * num)
    word = input("Please enter a word of your choice: ")
    print("The length of your word", '"{}"'.format(word), "is:", len(word))

def coinflip():
    headORtales = 0
    while headORtales != -1:
        headORtales = int(input("Please enter 1 to choose heads, enter 0 to choose tails, or enter -1 to quit: "))
        x = random.randint(0, 1)
        if headORtales == -1:
            break
        elif headORtales == x:
            print("Congratulations! you beat me")
        else:
            if headORtales > 1:
                print("Invalid Number")
            else:
                print("Looks like I win!")

def myArt():
    array = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]
    print("Here is my text art!")
    for x in range(len(array[0])):
        for y in range(len(array)):
            print(array[y][x], end="")
        print()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 3.')
    choice = 0
    while choice != -1:
        choice = int(input("Please enter 1 if you would like to coinflip, enter 2 to see my art!, or enter -1 to exit "))
        if choice == 1:
            coinflip()
        elif choice == 2:
            myArt()
        elif choice == -1:
            break
        else:
            print("That was an invalid choice! Please try again")
            continue

    #module2()


