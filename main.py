import secrets

secretsGenerator = secrets.SystemRandom()
secure_rand_num = secretsGenerator.randint(0, 100)


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Professor! here is programming assignment 5, using secrets module.')
    print(secure_rand_num)





