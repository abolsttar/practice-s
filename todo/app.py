from datetime import datetime, timedelta
import json
import os

tasks = []
STATES = dict(
    pending= '. ', 
    done= '✔ ',
    canceled= '✘ ',
    postpone= '➼ ',
)


def isu(text):
    for task in tasks:
        if task['text'] == text:
            return False
    return True

def add(text):
    text = text or input('Task title: ') or 'untitled task!'
    if isu(text):
        tasks.append(dict( 
            text=text,
            state='pending',
            date=datetime.now().date().isoformat(),
        ))
        save()
    else:
        return f'task "{text}"already exists!'

def find(arg):
    for task in tasks:
        if task['text'] == arg:
             return task
    for task in tasks:
        if task['text'] .startswith(arg):
            return task

def edit(text):
    task = find(text)
    if task:
        text = input('now Task title : ') or task['text']
        if isu(text) or text ==  task['text']:
            task.update(text=text)
            save()
        else:
            return f'task "{text}"already exists!'
    else:
            return f'There is no task"{text}"!'
    
def postpone(text):
    task = find(text)
    if task :
          task.update(
            state='postpone',
            date=(datetime.now()+timedelta(days=1)).date().isoformat(),
        )
          
def mark(text, state):
    task = find(text) 
    if task:
        task.update(state=state)
        save()

def transfer():
    global tasks
    date = lambda task: datetime.strptime(task['date'], '%Y-%m-%d').date()
    today = datetime.now().date()
    for task in tasks:
        if date(task) < today:
            if task['state'] in ['pending', 'postponed']:
                task.update(
                    date=today.isoformat(),
                    state='pending'
                )
            elif task['state'] in ['done', 'canceled']:
                task.update(state='delete')
    tasks=[task for task in tasks if task['state']!='delete']
    save()

def show(message):
    os.system('cls||clear')
    print('    '+datetime.now().date().isoformat()+'/n')
    tasks.sort(key=lambda t: t['text'].lower())
    taskslist = [t for t in tasks if t['state']=='pending']
    taskslist += [t for t in tasks if t['state']=='done']
    taskslist += [t for t in tasks if t['state']=='canceled']
    taskslist += [t for t in tasks if t['state']=='postpone']
    for task in taskslist:
        print(
            '',
            STATES[task['state']],
            task['text']
        )
    print()
    if message:
        print(message)

def save():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)
        
def load():
    global tasks
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except:
        pass

def manual():
    print('''
    a, add                       to add a now task
    e, edit                      to edit a task
    d, done                      to mark a task as done
    c, cancel                    to mark a task as canceled
    u, undone, pending           to mark a task as pending
    p, postpone                  to postpone a task
    h, help, manual              to see this manual
    q, quit, x, exit             to quit the program      
''')
    input('press Enter to return to the menu')

def menu():
    message = None
    while True:
        transfer()
        show(message)
        
        cmd, arg = [*input('--> ').split(' ', 1), ''][:2]
        match cmd:
            case 'a' | 'add':
                message = add(arg)
            case 'e' |'edit':
                message = edit(arg)
            case 'd' | 'done':
                message = mark(arg, 'done')
            case 'c' | 'cancel':
                message = mark(arg, 'canceled')
            case 'u' | 'undone':
                message = mark(arg, 'pending')
            case 'p' | 'postpone' :
                message = postpone(arg)
            case 'h' | 'help' | 'manu':
                message = manual()
            case 'q' | 'x' | 'quit' | 'exit':
                exit()
            case _:
                message = 'wrong command! Enter "h" to see the manual. '
                
if __name__ == '__main__':
    load()
    menu()