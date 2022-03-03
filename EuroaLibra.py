def conversion():
    print('Bienvenido al sistema de converion de Euro a Libra Esterlina')
    ve=float(input('Ingrese el valor en euros que desea convertir'))
    vl=ve*0.83
    print(f'{ve} eqivalen a ${vl}Libras')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit