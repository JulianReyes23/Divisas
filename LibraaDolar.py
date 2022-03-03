def conversion():
    print('Bienvenido al sistema de converion de Libra Esterlina a Dolar')
    vl=float(input('Ingrese el valor en libras que desea convertir'))
    vd=vl*1.34
    print(f'{vl} eqivalen a ${vd}Dolares')
    op=int(input('''Que desea realizar?
    1. Realizar una nueva conversion
    2. Terminar'''))
    if op==1:
        return conversion
    elif op==2:
        exit