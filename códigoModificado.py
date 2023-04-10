
#Importación de lbrerias
from unidecode import unidecode
import datetime
import speech_recognition as sr

#Variables Globales---------------------------------------------------------------------------------------------------------

registroParcicipantes=[]
registroApartados=[]
registroApartadosFinal=[]
registroPuntos=[]
registroVoz=[]
codigoVoz=1
opciones=["La misma persona continua hablando","Otro miembro toma la palabra","El punto de la agenda a terminado"]
#-------------------------------------------------------------------------------------------------------------------------


#Sección de agenda---------------------------------------------------------------------------------------------------------
def agregarParticipantes():
    print("Se procede a realizar el registro de participantes\n")
    
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
    
    return(print(registroParcicipantes))


def agregarCodigoapartado(apartados:list):
    codigo = 1
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
                print("\nEntendido no se agregaán más puntos a este apartado")
                seguirPreguntando+=1
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n") 

def masApartados():
    while True:
            respuesta = input('¿Desea ingresar otro apartado? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            if unidecode(respuesta.lower()) == "si":
                agregarApartados()
                agregarPuntos(agregarCodigoapartado(registroApartados))
        
            elif unidecode(respuesta.lower()) == "no":
                print("\nEntendido no se agregaán más puntos a este apartado")
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n") 
#-------------------------------------------------------------------------------------------------------------------------

 #Sección de reconociminto de voz----------------------------------------------------------------------------------------
 
def apartadoDeseado():
    for i, apartado in enumerate(registroApartados):
        print(str(i) + ": " + apartado)
    
    while True:
        try:
            indice=int(input("Ingrese el índice correspondiente al apartado al que desea ingresar o -1 si no desea ingresar más: "))
            if indice == -1:
                break#Eliminar este -1, simpre tiene que existir 
            nombre = registroApartados[indice]
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
    for i, participante in enumerate(registroParcicipantes):
        print(str(i) + ": " + participante)
        
    while True:
        try:
            indice = int(input("Indica quien participantes escribiendo tu ínidice correspondiente: "))
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

def maximoIntervenciones(clavePunto,claveApartado,participante):
    valor=True
    contador=0
    for i in registroVoz:
      if [1]==participante and [2]==claveApartado and [3]==clavePunto:
          contador+=1
    if contador == 2:
        valor=False
        return valor 

def siguienteAccion(claves):
        clavePunto=claves[0]
        claveApartado=claves[1]
        participante=claves[2]
        siguePreguntando=1
        while siguePreguntando==1:   
            while True:
                print("\n")
                for i, opcion in enumerate(opciones):
                    print(str(i) + ": " + opcion)
                try:
                    respuesta= int(input("Indica la acción que desea realizar mediante el índice corespondiente: "))                  
                    if respuesta==0: #Signica que "Sigue hablando la misma persona" 
                        reconocimientoSinParticipanteAgenda(clavePunto,claveApartado,participante)
                        break
                    elif respuesta==1:  #Significa que Otro miembro toma la palabra
                        reconocimientoSinAgenda(clavePunto,claveApartado,participante)
                        break
                    elif respuesta==2: #Significa que "El punto de la agenda a terminado"
                        print("Entendido, este punto de la agenda ha sido discutido, favor indicar nuevo punto\n")
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
                    print("Entendido, el reconocimiento ha terminado\n")
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------

agregarApartados()
agregarPuntos(agregarCodigoapartado(registroApartados))
masApartados()
agregarParticipantes()
siguienteAccion(reconocimiento())
seguirReconociendo()

print(registroVoz)


