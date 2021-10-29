def pigConvert(prePigString):
    clusterList = ["ch", "gr"]
    splitSentence = prePigString.split()
    for i in range(len(splitSentence)):
        x = splitSentence[i]
        if x[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            splitSentence[i] = x + 'yay'
        elif clusters(x) in clusterList:
            splitSentence[i] = x[2:] + x[:2] + 'ay'
        elif x.isalpha() == False:
            splitSentence[i] = x
        else:
            splitSentence[i] = x[1:] + x[0] + 'ay'
    print(' '.join(splitSentence))


def clusters(str):
    return str[0] + str[1]

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 6.')
    prePigString = str(input("Please enter a sentence to turn into pig latin! "))
    pigConvert(prePigString)





