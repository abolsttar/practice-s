def add():
    print(add)

def edit():
    pass

def postpone():
    pass

def mark():
    pass

def show():
    pass

def save():
    pass

def load():
    pass

def manual():
    pass

def menu():
    while True:
        cmd, arg = input('--> ').split(' ', 1)
    match cmd:
        case 'a':
            add()
        case 'e':
            edit()
        case 'd':
            mark()
        case 'c':
            mark()
        case 'p':
            postpone()
        case 'h':
            manual()
        case 'q':
            exit()
        case _:
            print('wring command!')
            
if __name__ == '__main__':
    load()
    menu()