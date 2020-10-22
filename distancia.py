
import pandas as pd
rutas = [('Morelia',50,60,10),('sonora',10,90,5),('Acapulco',5,4,80,6),('CDMX',5,70,8)]

def calcula_distancias(rutas):
    '''
    # Problema 1.1: Crea lista de tuplas (ruta, distancia)
    que asocie a cada ruta la distancia total calculada como la suma
    de las distancias de sus tramos

    Parameters
    ----------
    rutas : diccionario de python
        llaves : 'nombre de ruta'
        elementos: lista de tuplas ('nombre de tramo', distancia)
    Returns
    -------
    rutas_distancia: lista de tuplas ('nombre de ruta', distancia)
        donde distancia es la suma de las rutas de sus tramos

    '''
#Creo la lista
    ruta_distancia = []

    for i in range(len(rutas)):
        nombre = rutas[i][0]
        viajes = len(rutas[i])
        total=0
        for lc in range(1,viajes):
            total += rutas[i][lc]
        ruta_distancia += [(nombre,total)]

    return (ruta_distancia)

rutaa= calcula_distancias(rutas)


def ordena_rutas(rutaa):
    '''
    # Problema 1.2: Ordena rutas de acuerdo a distancias
    Parameters
    ----------
     rutas: lista de tuplas ('nombre de ruta', distancia)
    Returns
    -------
     rutas_ordenadas: lista de tuplas ('nombre de ruta', distancia)
         ordenada por distancia (de menor a mayor)

    '''
    rutas = sorted(rutaa, key=lambda distancia:distancia[1])
    return (rutas)
rutas_vehi=(ordena_rutas(rutaa))

transportes= ['carro',100,80,'helicoptero',250,200,'triciclo',50,30,'moto',50,20]

def vehiculos_tupla_a_lista(vehiculos):
    '''
    # Problema 2.1: Crea lista de tuplas (vehiculo, alcance, alcance_disponible) a partir de vehiculos
    Parameters
    ----------
    vehiculos : diccionario de vehiculos
        llave: 'nombre de vehiculo'
        datos: diccionario de datos {'alcance': valor_alcance, 'alcance_disponible': valor_alcance_disponible}
    Returns
    -------
    vehiculos_lista : lista de tuplas ('nombre de vehiculo', valor_alcance, valor_alcance_disponible)
'''
    transporte = []
    tam = int(len(transportes)/3)
    for i in range(0,tam):
        nombre = vehiculos[i*3]
        alcance = vehiculos[i*3+1]
        alcance_disp = vehiculos[i*3+2]
        transporte += [(nombre, alcance, alcance_disp)]
    return transporte
trans= (vehiculos_tupla_a_lista(transportes))


def ordena_vehiculos(vehiculos):
    '''
    # Problema 2.2: Ordena lista de vehiculos de acuerdo a alcance

    Parameters
    ----------
    vehiculos : lista de tuplas ('nombre de vehiculo', valor_alcance, valor_alcance_disponible.

    Returns
    -------
    vehiculos_ordenados : lista de tuplas ('nombre de vehiculo', valor_alcance, valor_alcance_disponible)
        ordenada de acuerdo a valor_alcance (de menor a mayor)
    '''
    lista_vehiculos = sorted(vehiculos, key=lambda alcance:alcance[1])
    return (lista_vehiculos)
vehiculo = ordena_vehiculos(trans)

def asocia_rutas_vehiculos(rutas_distancia, vehiculos_alcance):
    '''
    # Problema 3: Asigna las rutas a vehiculos en el orden definido

    Parameters
    ----------
    vehiculos_alcance : lista de tuplas ('nombre de vehiculo', valor_alcance, valor_alcance_disponible)
        ordenada de acuerdo a valor_alcance (de menor a mayor)
    rutas_distancia : lista de tuplas ('nombre de ruta', distancia)
         ordenada por distancia (de menor a mayor)

    Returns
    -------
    rutas_vehiculos : lista de tuplas de la siguiente forma:
        (('nombre de ruta', distancia), 'nombre de vehiculo', accion, alcance_inicial, alcance_final)
        donde :
        ('nombre de ruta') : copiado de rutas_distancia
        'nombre de vehiculo' : copiado de vehiculos_alcance
        accion: 'cargar' cuando valor_alcance_disponible no es suficiente para recorrer la distancia
                'no_cargar' cuando valor_alcance_disponible es suficiente para recorrer la distancia
        alcance_inicial: el alcance del vehiculo al iniciar el recorrido
            su valor depende de si:
                - se cargó combustible (valor_alcance_disponible) o
                - no se cargó combustible (valor_alcance)
        alcance_final: es la diferencia entre el alcance_inicial i la distancia de la ruta

    '''
    tabla = pd.DataFrame(rutas_distancia, vehiculos_alcance)
    rutas_vehiculos = []
    for i in range(len(tabla)):
        valores = tabla[i]
        if (valores[3] < valores[1]):
            edo_carga =('se realiza carga')
            carga = valores[4]
        else:
            edo_carga=('no')
            carga = valores[4]
    alcance_final =valores[4]-valores[3]
    rutas_vehiculos += [edo_carga,carga, alcance_final]
    print(rutas_vehiculos)
    return rutas_vehiculos


def asigna_rutas(rutas, vehiculos):
    '''
    Problema 4: Integración. Usa las funciones previamente definidas
        para asignar rutas a vehiculos

    Parameters
    ----------
     rutas : diccionario de python
        llaves : 'nombre de ruta'
        elementos: lista de tuplas ('nombre de tramo', distancia)
    vehiculos : diccionario de vehiculos
        llave: 'nombre de vehiculo'
        datos: diccionario de datos {'alcance': valor_alcance, 'alcance_disponible': valor_alcance_disponible}

    Returns
    -------
    rutas_asignadas : lista de tuplas de la siguiente forma:
        (('nombre de ruta', distancia), 'nombre de vehiculo', accion, alcance_inicial, alcance_final)
        donde :
        ('nombre de ruta') : copiado de rutas_distancia
        'nombre de vehiculo' : copiado de vehiculos_alcance
        accion: 'cargar' cuando valor_alcance_disponible no es suficiente para recorrer la distancia
                'no_cargar' cuando valor_alcance_disponible es suficiente para recorrer la distancia
        alcance_inicial: el alcance del vehiculo al iniciar el recorrido
            su valor depende de si:
                - se cargo combustible (valor_alcance_disponible) o
                - no se cargó combustible (valor_alcance)
        alcance_final: es la diferencia entre el alcance_inicial i la distancia de la ruta

    '''

    rutas_distancia = calcula_distancias(rutas)
    # Principio de tu solución
    for rutTup in rutas_distancia:

    # Fin de tu solución
    rutas_asignadas = asocia_rutas_vehiculos(rutas_distancia, vehiculos_alcance)

    return rutas_asignadas


def imprime(rutas_asignadas):
    print("Rutas Asignadas:")
    for ruta in rutas_asignadas:
        print(ruta)


if __name__ == '__main__':
    # assumption, both dictionaries are of the same size
    rutas = {'ruta_1': [('tramo_1', 200), ('tramo_2', 400), ('tramo_3', 100)],
             'ruta_2': [('tramo_1', 50), ('tramo_2', 20), ('tramo_3', 100)],
             'ruta_3': [('tramo_1', 600), ('tramo_2', 650)],
             }
    vehiculos = {'helicóptero': {'alcance': 800, 'alcance_disponible': 30},
                 'avión': {'alcance': 2000, 'alcance_disponible': 600},
                 'coche': {'alcance': 400, 'alcance_disponible': 300},
                 }

    solucion_correcta = [(('ruta_2', 170), 'coche', 'no_cargar', 300, 130),
                         (('ruta_1', 700), 'helicóptero', 'cargar', 800, 100),
                         (('ruta_3', 1250), 'avión', 'cargar', 2000, 750)]
    solucion = asigna_rutas(rutas, vehiculos)
    assert (solucion == solucion_correcta), "Error"
    imprime(solucion)