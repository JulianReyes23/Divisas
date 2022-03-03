
def centro_juegos():
    print('Bienvenido al centro de juegos')
    print('''Que desea hacer?
            1. registrar la entrada de personas
            2. iniciar el juego de la rana
            ''')
    opcion=int(input('Ingrese la opcion: '))
    if opcion==1:
        from agenda1 import agenda
        
    if opcion==2:
        from rana1 import jugar
        centro_juegos()
centro_juegos()
