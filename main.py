#main
#====

import Archimed as ac #import zd5
import pyramid as pd #import zd4

if __name__ == '__main__':
    usr = input('Введите 1 если вы хотите проверить плавает ли объект\nи 2 если хотите найти площадь учечённой пирамиды:\n')
    if usr == '1': #ans in first sit
        ac.main()
    elif usr == '2': #ans in second sit
        pd.main()
    else:
        print(f'Эй, чурчхела просили же нормальный ввод 1, 2 и 3, а это - {usr}, что такое') #output in case of incorrect input
