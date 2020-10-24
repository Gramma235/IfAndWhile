flag = True
dest = int(input('Введите направление: '))
while flag == True:
    if dest == 11:
        turn = int(input('Введите направление поворота: '))
        if turn == 1:
            dest = 12
            print('Запад')
        elif turn == 0:
            dest = 11
            print('Север')
        elif turn == -1:
            dest = 14
            print('Восток')
        else:
            print('Число не верно, бан')
            flag = False
    elif dest == 12:
        turn = int(input('Введите направление: '))
        if turn == 1:
            dest = 13
            print('Юг')
        elif turn == 0:
            dest = 12
            print('Запад')
        elif turn == -1:
            dest = 11
            print('Север')
        else:
            print('Число не верно,бан')
            flag = False
    elif dest == 13:
        turn = int(input('Введите направление: '))
        if turn == 1:
            dest = 14
            print('Восток')
        elif turn == 0:
            dest = 13
            print('Юг')
        elif turn == -1:
            dest = 12
            print('Запад')
        else:
            print('Число не верно,бан')
            flag = False
    elif dest == 14:
        turn = int(input('Введите направление: '))
        if turn == 1:
            dest = 11
            print('Север')
        elif turn == 0:
            dest = 14
            print('Восток')
        elif turn == -1:
            dest = 13
            print('Юг')
        else:
            print('Число не верно,бан')
            flag = False
    else:
        print('Число не верно, бан')
        flag = False

