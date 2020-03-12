
print('''guide:
enter (l) to convert to kilograms 
or enter (k) to convert to pounds 
and 'quit' for exiting ,
press empty enter to let the program get started again ...''')

command=''
while command == '' :
    weight = float(input('weight: '))
    l_or_k = input('(L)bs or (K)g ? ').lower()

    if l_or_k == 'l':
        weight *= 0.45
        print(f'your weight {weight} kilograms')

    elif l_or_k == 'k':
        weight /= 0.45
        print(f'your weight {weight} pounds')

    else:
        print('something were wrong...')

    command = input('> ').lower()
    if command == 'quit':
        break
    elif command != '':
        i=1
        while i<=3 and command != '':
            print(' its wrong input !!')
            command = input('> ').lower()
            i+=1

