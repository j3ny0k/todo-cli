help = ('add', 'show', 'done', 'delete', 'exit', 'help')

tasks = []

def input_num():
    while True:
        try:
            num_str = input('\ntask num: ')
            if not num_str:
                print('input is empty')
                continue
            num = int(num_str)
        except ValueError:
            print('only integers allowed')
            continue
        break

    if not tasks:
        print('no tasks')
        return

    if num < 1 or num > len(tasks):
        print('invalid task number')
        return
    
    return num

def add():
    while True:
        title = input('\ntask: ')
        if not title:
            print('input is empty')
            continue
        break

    tasks.append({
        'title': title,
        'done': False
    })

def show():
    if not tasks:
        print('no tasks')
        return

    num = 1
    for task in tasks:
        if task['done']:
            done = '[x]'
        else:
            done = '[ ]'
        print(str(num) + '.', done, task['title'])
        num += 1

def done():
    num = input_num()

    if num is None:
        return

    tasks[num-1]['done'] = True

    print('task marked as done')

def delete():
    num = input_num()

    if num is None:
        return

    del tasks[num-1]

    print('task deleted')

print('type "help" to show commands')

while True:
    command = input('\ncommand: ')

    if not command:
        print('input is empty')
        continue

    elif command == 'help':
        print('allowed commands:', ', '.join(help))

    elif command not in help:
        print('invalid command:', command)
        print('available:', ', '.join(help))

    if command == 'exit':
        break

    elif command == 'add':
        add()

    elif command == 'show':
        show()

    elif command == 'done':
        done()

    elif command == 'delete':
        delete()