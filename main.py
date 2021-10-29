import re

def method1(str):
    sentence = str.split()
    for i in range(len(sentence)):
        print(sentence[i])

def method2(str):
    new = re.findall(r'\S+', str)
    for i in range(len(new)):
        print(new[i])

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 6.')
    str = str(input("Please enter a string: "))
    method1(str)
    method2(str)






