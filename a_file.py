students = []

while True:

    print("FOOD:\n" +
          "1) Start\n" +
          "2) Exit\n")

    option = input("\n> ")

    if option == "1":
        print('a) taco bell:\n' +
              'b) Burger King\n' +
              'c)Arbys\n')
        resopt = input("Choose the restaurant: ")

        if resopt =="a":
            print('a) soft\n' +
                  'b) hard\n'  +
                  'c) nacho\n')
            taco = input('type of taco: ')
            if taco == 'a':
                print ('ya got diarrhea')
            if taco == 'b':
                print ('ya got diarrhea')
            if taco == 'c':
                print('your toilet survived')

                break





