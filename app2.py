count = 0
was_started = False

while count<10 :
    command = input('> ')
    comman = command.lower()
    if command == 'help' :
        print('''
        start --> to start the car 
        stop --> to stop the car 
        quit --> to exit the game
        ''')
    elif command == 'start' and not was_started :
         print('car started .')
         was_started = True
    elif command == 'start' and  was_started:
        print('car already started!')
    elif command == 'stop' and was_started :
        print('car stopped .')
        was_started = False
    elif command == 'stop' and not was_started:
        print('car already stopped!')
    if command == 'quit' :
        break
