students = []


def menu():
    print('FOOD:\n'+
          '1) start\n'+
          '2) exit\n'
         )


while True:

    menu()

    option = input("\n> ")

    if option == "1":
        print('a) taco bell:\n' +
              'b) Burger King\n' +
              'c) Arbys\n')
        resopt = input("Choose the restaurant: ")
        if resopt == 'c':
            print(
                'a) Gyro\n'+
                'b) roast beef\n'+
                'c) vegan sandwich\n')
            meat = input('what ya want: ')

            if meat == 'a':
                print('FAIL idk im not greek')
            if meat == 'b':
                print('WIN you came to the right place my guy')
            if meat == 'c':
                print('FAIL why are you here we have the meats')

        if resopt == "b":
            print('a) salad\n'+
                  'b) chicken sandwich\n'+
                  'c) whopper\n')
            burger = input('what you want: ')
            if burger == "a":
                print('FAIL You got foot lettuce')
            if burger == "b":
                print('FAIL The burger KING... blasts out from the back to roundhouse you in the face')
            if burger == "c":
                print('YOU WIN You have a exquisite lunch')

        if resopt == "a":
            print('a) soft\n' +
                  'b) hard\n'  +
                  'c) nacho\n')
            taco = input('type of taco: ')
            if taco == 'a':
                print('FAIL ya got diarrhea')
            if taco == 'b':
                print('FAIL ya got diarrhea')
            if taco == 'c':
                print('YOU WIN your toilet survived')

                break





