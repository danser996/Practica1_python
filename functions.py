from random import randint
'''Empresa de comunicaciones TELEPYTHON ----- Trabajo 1 ----- Lenguaje de Programacion 2'''
'''Funciones'''
def verificacion_nom():
    '''Esta funcion pide el nombre del usuario y lo verifica,
     que no tenga caracteres numericos, de lo contrario retornara un 0'''
    cadena = input('Ingrese su nombre: ')
    verificacion = cadena.replace(' ', '', 100)
    if verificacion.isalpha() == True:
        print('-'*60)
        return cadena.upper()
    else:
        print('Nombre no valido, vuelva a intentarlo...')
        return 0

def verificacion_apel():
    '''Esta funcion pide el apellido del usuario y lo verifica que no tenga 
    caracteres numero si cumple retorna la el apellido y si no retorna un 0'''
    cadena = input('Ingrese su apellido: ')
    verificacion = cadena.replace(' ', '', 100)
    if verificacion.isalpha() == True:
        print('-'*60)
        return cadena.upper()
    else:
        print('Apellido no valido, vuelva a intentarlo...')
        return 0

def verificar_edad():
    '''Esta funcion pide la edad y la verifica, tiene que ser un numero, no permite 
    edades menores de 0 ni mayores de 100'''
    edad = input('Ingrese su edad: ') # recibe la edad como str
    if not edad.isnumeric() == True: # si el str no es solo numerico alerta de error
        print('Edad no valida, vuelva a intentarlo...')
        return 0
    else:
        edad = int(edad)    #convierte a entero la edad
        if edad > 100 or edad < 5: # edades fuera de rango
            print('Edad no valida, vuelva a intentarlo...')
            return 0
        else: 
            print('-'*60)
            return edad # retorna la edad en caso de que cumpla todas las condiciones

def verificar_cedula():
    '''Esta funcion pide la cedula y la verifica, esta debe ser un numero
    de entre 7 y 10 digitos, si no es asi retorna un 0 y sera invalida '''
    cedula = input('Ingrese su numero de cedula: ') # recibe la edad como str
    if cedula.isnumeric() == False: # si el str no es solo numerico alerta de error
            print('Numero de identificacion no valido, vuelva a intentarlo...')
            return 0
    else:
        cedula = int(cedula)    #convierte a entero la cedula
        if cedula > 9999999999 or cedula < 1000000: # cedula fuera de rango
            print('Numero de identificacion no valido, vuelva a intentarlo...')
            return 0
        else: 
            print('-'*60)
            return cedula  # retorna la edad en caso de que cumpla todas las condiciones

def verificar_email(): 
    '''Este funcion verifica que la direccion de correo electronico sea correcta 
    y la retorna siempre y cuando la direccion contenga @ y dominio (.com o .es)
    la posicion del arroba tiene que ser menor que la posicion del dominio, de no
    ser asi no sera correcta y retornara un 0'''
    cadena = input('Escriba su direccion de correo electronico: ')
    pos_arroba = cadena.find('@') #busca el caracter dentro del string, si no lo encuentra devuelve -1 y si lo encuentra devuelve la posicion en la q se encuentra el caracter
    dominio_com = cadena.find('.com') # retirna el valor de la pociones del dominio
    dominio_es = cadena.find('.es')
    if pos_arroba < 0: 
        print('Direccion de correo electronica no valida, vuelva a intentarlo...')
        return 0
    elif dominio_com < 0 and dominio_es < 0:
        print('Direccion de correo electronica no valida, vuelva a intentarlo...')
        return 0
    else:
        dominio = max(dominio_es, dominio_com)
        if pos_arroba < dominio:
            print('-'*60)
            return cadena
        else: 
            print('Direccion de correo electronica no valida, vuelva a intentarlo...')
            return 0

def verificar_direccion():
    '''Esta funcion pide la direccion y la verifica,
    es correcta si esta contiene el numeroa y av o cra de lo contrario 
    retorna un 0'''
    cadena = input('Escriba su direccion: ')
    pos_numeral = cadena.find('#') #busca el caracter dentro del string, si no lo encuentra devuelve -1 y si lo encuentra devuelve la posicion en la q se encuentra el caracter
    pos_cra = cadena.find('ra') # retirna el valor de la pociones de 'ra'
    pos_av = cadena.find('av')
    if pos_numeral < 0:
        print('Direccion de residencia no valida, vuelva a intentarlo...')
        return 0
    else:
        if pos_numeral >= 0:
            if pos_cra > 0 or pos_av > 0:
                print('-'*60)
                return cadena
            else:
                print('Direccion de residencia no valida, vuelva a intentarlo...')
                return 0

def data_adq():
    '''esta funcion hace la adquisicion de datos empleando otras funciones,
    retorna una lista con los datos ingresador'''
    nombre = verificacion_nom()
    while nombre == 0:
        nombre = verificacion_nom()

    apellido = verificacion_apel()
    while apellido == 0:
        apellido = verificacion_apel()

    edad = verificar_edad()
    while edad== 0:
        edad = verificar_edad()

    email = verificar_email()
    while email == 0:
        email = verificar_email()

    direccion = verificar_direccion()
    while direccion == 0:
        direccion = verificar_direccion()

    cedula = verificar_cedula()
    while cedula == 0:
        cedula = verificar_cedula()

    return nombre, apellido, edad, email, direccion, cedula

def verificar_numero():
    '''Esta funcion pide y verifica el codigo del pais, tiene que se un
    numero y debe estar en 0 y 999, y lo retornara, si no cumple retornara un 0'''
    num = input('Ingrese el numero: ')
    if not num.isnumeric() == True:
        return 0
    else:
        num = int(num)
        return num

def formato_aleat(cant, list_num, num_tel):
    '''Esta funcion tiene como parametro de entrada la cantidad de separadores que 
    se desea, el codigo del pais y la lista de numeros generados, imprime en pantalla
    el codigo del pais entre parentesis, seguido de los numeros generados y con 
    los separadores que deseo el usuario'''
    list_str = []
    sep_tot = cant
    for i in list_num:
        list_str.append(str(i))
    #print(list_str)

    for j in list_str:
        arr = j
        aux = []
        cont = 0
        long_1 = round(len(j) / 2)
        long_2 = round(len(j) / 3)
        long_3 = round(len(j) / 1.5) + 1
        for k in arr:
            aux.append(k)
            cont += 1
            if sep_tot == 1:
                if cont == long_1:
                    aux.insert(cont, '-')
                aux_2 = ''.join(aux)
            elif sep_tot == 2:
                if cont == long_2:
                    aux.insert(cont, '-')
                elif cont == long_3:
                    aux.insert(cont, '-')
                aux_2 = ''.join(aux)
            else:
                aux_2 = ''.join(aux)
        #print(aux)
        if num_tel > 0:
            print(f'({num_tel})', end='')
            print(aux_2)
        else: 
            print(aux_2)


def compresion(cadena):
    '''Esta funcion recibe el numero asignado al usuario y hace el algoritmo de compresion
    y lo imprime en pantalla'''
    cad = cadena + '00000'
    x = []
    caracter = []
    cont = 0
    cont2 = 0
    aux = 0 
    for i in cad:
        x = cad[aux]
        if x == i:
            cont += 1
        else:
            cont2 += cont
            aux = cont2
            caracter.append((x, str(cont)))
            cont = 1

    #print(caracter)
    union = []
    for k in caracter:
        union.append(''.join(k))

    for l in union:
        print(l, end='_')
    print('\n')
    print('-'*60)

def generador_num(opcion_4):
    '''Esta funcion genera numero aleatorios entre ciertos valores, dependiendo
    de la cantidad de digitos que desee el usuario'''
    list_num = []
    for i in range(opcion_4):
        if opcion_4 == 7:
            num = randint(1000000, 9999999)
        elif opcion_4 == 8:
            num = randint(10000000, 99999999)
        elif opcion_4 == 9:
            num = randint(100000000, 999999099)
        else:
            num = randint(100000000, 999999999)
        list_num.append(num)
    return list_num
    #print(list_num)