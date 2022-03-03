def conversion():
    print('Bienvenido al sistema de converion de Euro a Dolar')
    ve=float(input('Ingrese el valor en Euros que desea convertir'))
    vd=ve*1.11
    print(f'{ve} eqivalen a ${vd}Dolares')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit