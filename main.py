import sys

def sortedStringList():
    print("\nArguments passed:", end=" ")
    n = len(sys.argv)
    strList = []
    for i in range(1, n):
        strList.append(sys.argv[i])
    strList.sort()
    print(strList)

def reverseString():
    n = len(sys.argv)
    argvString = ''
    for i in range(1, n):
        argvString += sys.argv[i] + " "
    sentenceWords = argvString.split(" ")
    reverse = ' '.join(reversed(sentenceWords))
    print(reverse)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 6.')
    sortedStringList()
    reverseString()





