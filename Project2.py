# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def module2():
    name = input("Please tell me your name: ")
    print("Hi", name, end='!\n')
    num = int(input("Please enter your favorite number: "))
    print("Your number of", num , "multiplied by itsself is:", num * num)
    word = input("Please enter a word of your choice: ")
    print("The length of your word", '"{}"'.format(word), "is:", len(word))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 2.')
    module2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/