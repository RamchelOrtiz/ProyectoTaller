
#Importación de lbrerias
from unidecode import unidecode
import datetime
import speech_recognition as sr
from os import system

#Variables Globales---------------------------------------------------------------------------------------------------------

registroParcicipantes=[]
registroApartados=[]
registroApartadosFinal=[]
registroPuntos=[]
registroVoz=[]
codigo=1
codigoVoz=1
opciones=["La misma persona continua hablando","Otro miembro toma la palabra","El punto de la agenda a terminado"]
recuento=[]
registroReportes=["Reporte1","Reporte2","Reporte3"]
#-------------------------------------------------------------------------------------------------------------------------

#Sección de agenda---------------------------------------------------------------------------------------------------------
def agregarParticipantes():
    """_summary_
    
    """
    print("\n Se procede a realizar el registro de participantes\n")
    
    seguirPreguntando=1
    posicionDondeAgregar=0
    
    #Se realiza para que exista al menos un paticipante
    while True:
        participante = input("Agrege un participante al registro por favor: ")
        if not participante.isnumeric():
            registroParcicipantes.insert(posicionDondeAgregar, participante)
            posicionDondeAgregar+=1
            break
        else:
            print("Por favor, ingrese un participante, no un número.\n")
            
    #Si se desean agregar más participante         
    while seguirPreguntando==1:
        while True:
            respuesta = input('¿Desea ingresar otro punto? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            
            #Si se desean agregar más participantes.
            if unidecode(respuesta.lower()) == "si":
                while True:
                    participante = input("Agrege otro participante por favor: ")
                    if not participante.isnumeric():
                        registroParcicipantes.insert(posicionDondeAgregar, participante)
                        posicionDondeAgregar+=1
                        break
                    else:
                        print("Por favor, ingrese un participante, no un número.\n") 
                        
            #Si no se desea agregar más participantes, no se agregarán.
            elif respuesta.lower() == "no":
                print("\nEntendido no se agregarán más participantes al registro. La agendá terminó\n")
                seguirPreguntando+=1
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n")             


def agregarCodigoapartado(apartados:list):
    global codigo
    for i in apartados:
        codigoStr = str(codigo)
        registroApartadosFinal.append([codigoStr, i])
        codigo += 1
    return codigoStr

def agregarApartados():
    #Agrega apartado
    while True:
        apartado = input("Agrege un apartado por favor: ")
        if not apartado.isnumeric():
            registroApartados.append(apartado)
            break
        else:
            print("Por favor, ingrese un apartado, no un número.\n")
    return registroApartados
    

def agregarPuntos(codigo:str):
    seguirPreguntando=1
    codigoPunto=1
    while True:
        punto = input("Agrege un punto al apartado por favor: ")
        if not punto.isnumeric():
            registroPuntos.append([str(codigoPunto),punto,codigo])
            codigoPunto+=1
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
                        registroPuntos.append([str(codigoPunto),punto,codigo])
                        codigoPunto+=1
                        break
                    else:
                        print("Por favor, ingrese un punto que no sea solo un número.\n") 
        
            elif unidecode(respuesta.lower()) == "no":
                print("\nEntendido no se agregarán más puntos a este apartado\n")
                seguirPreguntando+=1
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n") 

def masApartados():
    while True:
            respuesta = input('¿Desea ingresar otro apartado? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            if unidecode(respuesta.lower()) == "si":
                registroApartados.clear()
                agregarApartados()
                agregarPuntos(agregarCodigoapartado(registroApartados))
        
            elif unidecode(respuesta.lower()) == "no":
                print("\nEntendido no se agregarán más puntos a este apartado")
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n") 
#-------------------------------------------------------------------------------------------------------------------------

 #Sección de reconociminto de voz----------------------------------------------------------------------------------------
 
def apartadoDeseado():
    for i, apartado in enumerate(registroApartadosFinal):
        print(str(i) + ": " + apartado[1])
    
    while True:
        try:
            indice=int(input("Ingrese el índice correspondiente al apartado al que desea ingresar: "))
            print("\n")
            nombre = registroApartadosFinal[indice][1]
            return nombre
                
        except:
            print("El índice indicado no es válido.")
                
def retornarClaveApartado(apartado:str):
    for i in registroApartadosFinal:
        if i[1] == apartado:
            return i[0]
        
        
def puntodoDeseado(apartado:str):
    for i, sublista in enumerate(registroPuntos):
        if sublista[2] == apartado:
            print(f"{i}-{sublista[1]}")
            
    while True:
        try:
            indice=int(input("Ingrese el índice correspondiente al apartado al que desea ingresar: "))
            nombre = registroPuntos[indice][1]
            return nombre,apartado
                    
        except:
            print("El índice indicado no es válido.")
      

        
def retornarClavePunto(punto:str,apartado:str):
    for i in registroPuntos:
        if i[1]==punto and i[2]==apartado:
            return i[0],apartado


def generarClaves():
    apartado=retornarClaveApartado(apartadoDeseado())
    Punto,Apartado=puntodoDeseado(apartado)
    clavePunto,claveApartado=retornarClavePunto(Punto,Apartado)
    return clavePunto ,claveApartado


def obtenerParticipante():
    print("\n")
    for i, participante in enumerate(registroParcicipantes):
        print(str(i) + ": " + participante)
        
    while True:
        try:
            indice = int(input("Indica quien participantes escribiendo tu índice correspondiente: "))
            participante = registroParcicipantes[indice]
            break
        except:
            print("El índice indicado no es válido.")
    return(participante)

def registroFecha():
    now = datetime.datetime.now()
    horaActual = now.strftime("%H:%M:%S")
    return horaActual      

def hablar():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Di algo...")
            audio = r.listen(source)
        try:
            print("inicia el reconocimiento...\n")
            texto = r.recognize_google(audio, language='es-ES')
            print("Has dicho: " + texto)
            break
        except:
            print("Lo siento, no he entendido lo que has dicho. Repítelo por favor")      

    return(texto)

def reconocimiento():
    global codigoVoz
    clavePunto,claveApartado=generarClaves()  
    participante=obtenerParticipante()
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1
    return(clavePunto,claveApartado,participante)
    
def reconocimientoSinAgenda(clavePunto,claveApartado):
    global codigoVoz
    participante=obtenerParticipante()
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1
 
def reconocimientoSinParticipanteAgenda(clavePunto,claveApartado,participante):
    global codigoVoz
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1

def siguienteAccion(claves):
        clavePunto=claves[0]
        claveApartado=claves[1]
        participante=claves[2]
        siguePreguntando=1
        while siguePreguntando==1:   
            while True:
                print("\n Opciones: \n")
                for i, opcion in enumerate(opciones):
                    print(str(i) + ": " + opcion)
                try:
                    respuesta= int(input("\nIndica la acción que desea realizar mediante el índice corespondiente: "))                  
                    if respuesta==0: #Signica que "Sigue hablando la misma persona" 
                        reconocimientoSinParticipanteAgenda(clavePunto,claveApartado,participante)
                        break
                    elif respuesta==1:  #Significa que Otro miembro toma la palabra
                        reconocimientoSinAgenda(clavePunto,claveApartado)
                        break
                    elif respuesta==2: #Significa que "El punto de la agenda a terminado"
                        print("\nEntendido, este punto de la agenda ha sido discutido.\n")
                        siguePreguntando+=1
                        break
                    else:
                        raise ValueError
                except:
                    print("El índice indicado no es válido.") 
                    
def seguirReconociendo():
    seguirPreguntando=1
    while seguirPreguntando==1:
        while True:
            try:
                respuesta = input('¿Desea terminar el reconocimiento? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
                if unidecode(respuesta.lower()) == "si":
                    print("\nEntendido, el reconocimiento ha terminado\n")
                    seguirPreguntando+=1
                    break                
                elif unidecode(respuesta.lower()) == "no":
                    siguienteAccion(reconocimiento())
                    break
                else:
                    raise ValueError 
            except:
                print('Responda con "si" o "no" únicamente')

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sección de reportes-----------------------------------------------------------------------------------------------------------------------------------------

#Menú reportes:
def menuReportes():
        print("\n")
        for i, opcion in enumerate(registroReportes):
            print(f"{i+1}: {opcion}")
                
        while True:
            try:
                indice=int(input("\nIngrese el índice correspondiente al reporte que desea realizar: "))
                if indice==1:
                    print("\n Se realizará el reporte 1\n")
                    primerReporte()
                    break
                elif indice==2:
                    print("\n Se realizará el reporte 2\n")
                    segundoReporte()
                    break
                elif indice==3:
                    print("\n Se realizará el reporte 3\n")
                    tercerReporte()
                    break
                else:
                    raise ValueError
            except:
                print("El índice indicado no es válido.")    
        
def seguirReportes():
    seguirPreguntando=1
    while seguirPreguntando==1:
        while True:
                try:
                    respuesta = input('¿Desea terminar de imprimir reportes? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
                    if unidecode(respuesta.lower()) == "si":
                        print("\nEntendido, no se imprimen más reportes\n")
                        seguirPreguntando+=1
                        break                
                    elif unidecode(respuesta.lower()) == "no":
                        menuReportes()
                    else:
                        raise ValueError 
                except:
                    print('Responda con "si" o "no" únicamente')
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Primer reporte

def imprimir_voz(apartados, puntos,voz):
    for apartado in apartados:
        print(apartado[1] + ":")
        for punto in puntos:
            if punto[2] == apartado[0]:
                print("\t" + punto[1] + ":")
                for v in voz:
                    if v[2] == apartado[0] and v[3] == punto[0]:
                        print("\t\t" + v[1] + " " + v[5]+ ": "  + " " + v[4])

def primerReporte():
    imprimir_voz(registroApartadosFinal,registroPuntos,registroVoz)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Segundo reporte--------------------------------------------------------------------------------------------------------------------------------------------
def obtenerRecuentoPalabras(personas, registro):
    global recuento
    for persona in personas:
        palabras_dichas = 0
        for registro_persona in registro:
            if registro_persona[1] == persona:
                palabras_dichas += len(registro_persona[4].split())
        # Buscamos si ya existe un elemento en recuento que corresponda a esta persona
        existe_persona = False
        for i in range(len(recuento)):
            if recuento[i][0] == persona:
                recuento[i][1] += palabras_dichas
                existe_persona = True
                break
        # Si no encontramos la persona en recuento, la agregamos como un nuevo elemento
        if not existe_persona:
            recuento.append([persona, palabras_dichas])
    return recuento

def ordenarListaDescendiente(lista):
    n = len(lista)
    while n > 1:
        for i in range(n-1):
            if lista[i][1] < lista[i+1][1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        n -= 1
    return lista

def segundoReporte():
    listaOrdenada=ordenarListaDescendiente(obtenerRecuentoPalabras(registroParcicipantes,registroVoz))
    print("A continuación se mostrará de orden descendente las personas de más palabras dijeron: \n")
    for elemento in listaOrdenada:
        print(elemento[0], "con", elemento[1],"palabras")
        print("\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Tercer reporte

def tercerReporte():
    
    
    return



#------------------------------------------------------------------------------------------------------------------------------------------------------------

def ejecuciónPrograma():
    system("cls")
    print("TextToSpeech para Sesiones de Órganos Colegiados\n")
    print("Se procede a realizar el registro de Agenda\n")
    agregarApartados()
    agregarPuntos(agregarCodigoapartado(registroApartados))
    masApartados()
    agregarParticipantes()
    print("Apartados: \n")
    siguienteAccion(reconocimiento())
    seguirReconociendo()
    print("Se proceden a realizar los reportes")
    menuReportes()
    seguirReportes()
    print("\n El programa a finalizado su ejecución")

#Se ejecuta el programa
ejecuciónPrograma()




