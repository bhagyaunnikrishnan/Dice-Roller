while True:
    import random
    print("This is a Dice rolling game.")
    print("1.To roll dice\n2.Exit from game")
    print("Let's begin!!!!")
    choice = int(input("Make your selection[1/2]:"))
    if choice == 1:
        number = random.randint(1, 6)
        if number == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        if number == 2:
            print("[-----]")
            print("[0    ]")
            print("[     ]")
            print("[    0]")
            print("[-----]")
        if number == 3:
            print("[-----]")
            print("[    0]")
            print("[  0  ]")
            print("[0    ]")
            print("[-----]")
        if number == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        if number == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        if number == 6:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
    elif choice == 2:
        print("Game ended")
        break
    else:
        print("Wrong selection,do it again")
            
