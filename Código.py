"""Se debe intalar la libreria unicode, con el proposito de utilizar la función unicode para convertir textos a textos sin tíldes """
#Hola
from unidecode import unidecode

registroAgenda=[]

def agregarApartados():
    listaApartados= []
       
    while True:
        apartado = input("Agrege un apartado de la agenda por favor: ")
        if not apartado.isnumeric():
            listaApartados.append(apartado)
            registroAgenda.append(listaApartados)
            break
        else:
            print("Por favor, ingrese un texto que no sea solo un número.\n")
     
def agregarPuntos():
    posicionEnRegistroAgendaAgregar= len(registroAgenda)-1
    posicionDondeAgregar=1
    seguirPreguntando=1
    
    while True:
        punto = input("Agrege un punto de la agenda por favor: ")
        if not punto.isnumeric():
            registroAgenda[posicionEnRegistroAgendaAgregar].insert(posicionDondeAgregar, punto)
            posicionDondeAgregar+=1
            break
        else:
            print("Por favor, ingrese un punto que no sea solo un número.\n")
            
    while seguirPreguntando==1:
        while True:
            respuesta = input('¿Desea ingresar otro punto? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            if unidecode(respuesta.lower()) == "si":
                while True:
                    punto = input("Agrege un punto de la agenda por favor: ")
                    if not punto.isnumeric():
                        registroAgenda[posicionEnRegistroAgendaAgregar].insert(posicionDondeAgregar, punto)
                        posicionDondeAgregar+=1
                        break
                    else:
                        print("Por favor, ingrese un punto que no sea solo un número.\n") 
        
            elif respuesta.lower() == "no":
                print("\nEntendido no se agregaán más puntos a este apartado")
                seguirPreguntando+=1
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n")             
    
def continuarApartados():
    saberSiContinuar=1
    while saberSiContinuar==1: 
        while True:
            respuesta = input('¿Desea ingresar otro apartado? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            if unidecode(respuesta.lower()) == "si":
                agregarApartados()
                agregarPuntos()
                break
            elif unidecode(respuesta.lower()) == "no":
                print("\nEntendido no se agregán más apartados, la agenda terminó")
                saberSiContinuar+=1
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n")  

def imprimirAgenda():
    print("La agenda se encuntra compuesta por: ")
    for i in registroAgenda:  
        print("\n")
        print("El apartado "+i[0]+" posee los puntos: \n")  
        for elemento in i[1:]:
            print(elemento)
                   
def menuAgenda():
    print("Se procede a realizar el registro de agenda\n")
    agregarApartados()
    agregarPuntos()
    continuarApartados()
    print("\n")
    return(imprimirAgenda())


"""---------------------------------------------------------------------------------------------------------------------"""
"""Aquí empieza a ejecutarse el programa"""
print("\n")
print("Bienvenido a TextToSpeech para Sesiones de Órganos Colegiados\n")
menuAgenda()

    
    