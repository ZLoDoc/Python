flag = True
while flag:
    try:
        a = input()
        if not (a.isdigit() and a.startswith('8') and len(a) == 11):
            raise TypeError('Номер телефона некорректный')
    except ValueError as e:
        print('Ошибка.', e)
    except TypeError as e:
        print(f'Ошибка. {e}')
    else:
        flag = False
    finally:
        print('Конец блока try')