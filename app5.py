try:
    class Person :
        def __init__(self, age):
            self.age=age


    print('''
             to fine out age of each person,
             type his name only :::....:::
             
             ''')

    name = input('name: ').lower()

    john = Person(25)
    hadi = Person(21)
    mosh = Person(32)

    print(vars()[name].age)

except KeyError :
    print('input name with letters only !')
