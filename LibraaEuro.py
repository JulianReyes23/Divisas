def conversion():
    print('Bienvenido al sistema de converion de Libras a Euros')
    vl=float(input('Ingrese el valor en Libras que desea convertir'))
    ve=vl*1.20
    print(f'{vl} eqivalen a ${ve}Dolares')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit