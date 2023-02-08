from functions import * 

#funcion pricipal
def main():
    # '''Toma de datos del usuario'''
    bienvenida = '''Bienvenido a la empresa TELEPYTHON comunicaciones, a continuacion 
    se le pediran los datos personales para su registro'''
    print(bienvenida)
    i = 0
    while i == 0: 
        data = data_adq()
        i += 1
    
    nombre = data[0]
    apellido = data[1]
    edad = data[2]
    email = data[3]
    direccion = data[4]
    cedula = data[5]

    cod_pais = ''' Seleccione una de las opciones para asignar el codigo del pais:
    [1] No desea asignar
    [2] Generarlo aleatorio
    [3] Ingresarlo
    Seleccione una de las anteriores opciones: '''

    '''opcion 1'''
    opcion_1 = input(cod_pais)
    while opcion_1 not in ['1','2','3']:
        if opcion_1 not in ['1','2','3']:
            print('\nPor favor seleccione una opción valida\n')
            opcion_1 = input(cod_pais)
    if opcion_1 == '1':
        c_p = -1
    elif opcion_1 == '2':
        c_p = randint(1, 1000)
    else:
        c_p = verificar_numero()
        while c_p < 0 or c_p > 1000:
            print('Ingrese un codigo de pais valido...')
            c_p = verificar_numero()
    print('Codigo pais: ', c_p)

    '''opcion 2'''
    numero_dig = '''Ingrese la cantidad de digitos que desea que conformen su numero celular,
    la cantidad de digitos aceptada esta entre 7 y 10: '''
    print(numero_dig)
    opcion_2 = verificar_numero()
    while opcion_2 < 6 or opcion_2 > 10:
        if opcion_2 < 6 or opcion_2 > 10:
            print('Digito incorrecto, intente de nuevo...Ingrese una cantidad entre 7 y 10:')
            opcion_2 = verificar_numero()

    '''Opcion 3'''
    separador = '''Como desea visualizar el numero?
    [T] Con separador (-)
    [F] Sin separador
    Elija una opcion: '''
    sep_tot = 0
    opcion_3 = input(separador)
    while opcion_3 not in ['T', 'F', 'f', 't']:
        if opcion_3 not in ['T', 'F', 'f', 't']:
            print('\nPor favor seleccione una opción valida\n')
            opcion_3 = input(separador)
    if opcion_3 == 't':
        opcion_3 = 'T'
    '''opcion 3.1'''
    print('-'*60)
    if opcion_3 == 'T':
        sep_mensaje = ('''Tiene la posibilidad de separarlo con 1 o 2 guiones,
        elija una opcion
        [1] 1 guion
        [2] 2 guiones
        Escriba una opcion:  ''')
        sep = input(sep_mensaje)
        while sep not in ['1', '2']:
            print('\nPor favor seleccione una opción valida\n')
            sep= input(sep_mensaje)
        if sep == '1':
            sep_tot = 1
        else:
            sep_tot = 2
    '''opcion 4'''
    num_alt = '''Puede generar entre 2 y 10 numeros aleatorios, el ultimo 
    generado le sera asignado, ingrese la cantidad de numero que desea generar: '''
    print(num_alt)
    opcion_4 = verificar_numero()
    while opcion_4 < 2 or opcion_4 > 10:
        if opcion_4 < 2 or opcion_4 > 10:
            print('Ingrese una cantidad entre 2 y 10: ')
            opcion_4 = verificar_numero()

    '''generar la cantidad de numeros deseados'''
    list_num = generador_num(opcion_4)
    
    '''Imprimir lista de numero, con las caracteristicas especificadas'''
    formato_aleat(sep_tot, list_num, c_p)

    '''Imprimir los datos del usuario'''
    mensaje = '''Su registro ha sido exitoso, a continuacion se mostraran 
    todos sus datos, le deseamos un buen servicio'''
    print(mensaje)
    print('.'*60)
    print('| Nombre: ', nombre, apellido)
    print('| Edad: ', edad)
    print('| Numero de cedula: cc', cedula)
    print('| Direccion de correo electronico: ', email)
    print('| Direccion de residencia: ', direccion)
    print('| Numero telefonico asignado: ', str(list_num[-1]))
    print('.'*60)

    '''compresion del numero telefonico del usuario'''
    compresion(str(list_num[-1]))  

if __name__ == '__main__':
    main()