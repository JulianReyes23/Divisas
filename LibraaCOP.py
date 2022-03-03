def conversion():
    print('Bienvenido al sistema de converion de Libras Esterlinas a Peso Colombiano')
    vl=float(input('Ingrese el valor en Libras que desea convertir'))
    vp=vl*5238
    print(f'{vl} eqivalen a ${vp}Pesos')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit