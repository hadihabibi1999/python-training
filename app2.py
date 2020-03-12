command = ''
was_started = False

while command.lower()!='quit' :
    command = input('> ').lower()
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
    else:
        print("don't understand that !..")