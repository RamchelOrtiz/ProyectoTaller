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
registroReportes=["Reporte 1","Reporte 2","Reporte 3"]
#-------------------------------------------------------------------------------------------------------------------------
#Sección de agenda---------------------------------------------------------------------------------------------------------
def agregarParticipantes():
    """ Esta función permite agregar particiapantes, lo hace preguntando cada vez si desea agregar otro, debe indicarse con si o no, no importa la 
        manera en la que se escriban, mediante unicode y lower siempre lo considerará un ingreso válido, también si agrega un número únicamente, no lo
        permitirá ya que un usuario no puede ser un número. No posee ni argumentos ni return.
    
    """
    print("\n Se procede a realizar el registro de participantes\n") 
    seguirPreguntando=1
    #Se realiza para que exista al menos un paticipante
    while True:
        participante = input("Agrege un participante al registro por favor: ")
        if not participante.isnumeric():
            registroParcicipantes.append(participante)
            break
        else:
            print("Por favor, ingrese un participante, no un número.\n")      
    #Si se desean agregar más participante         
    while seguirPreguntando==1:
        while True:
            respuesta = input('¿Desea ingresar otro participante? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            #Si se desean agregar más participantes.
            if unidecode(respuesta.lower()) == "si":
                while True:
                    participante = input("Agrege otro participante por favor: ")
                    if not participante.isnumeric():
                        registroParcicipantes.append(participante)
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

def agregarCodigoapartado(apartado:list):
    """_Esta función genera un código para el apartado, este código es un número en formato str. Se genera una lista de la 
        siguiente manera ["1",Apartado], el siguiente ["2",Apartado]. Todo esto se agrega a registroApartadoFinal.
    Args:
        apartado (list): Es el apartado al que se le desea agregar el código.
    Returns:
        str: retorna el código del aparatado deseado.
    """
    global codigo
    for i in apartado:
        codigoStr = str(codigo)
        registroApartadosFinal.append([codigoStr, i])
        codigo += 1
    return codigoStr

def agregarApartados():
    """ Esta función permite agregar el nombre de un apartado. No tiene argumentos ni return.
        Si el apartado es un número, no permite ingresarlo, ya que el apartado debe tener texto. 
    """
    #Agrega apartado
    while True:
        apartado = input("Agrege un apartado por favor: ")
        if not apartado.isnumeric():
            registroApartados.append(apartado)
            break
        else:
            print("Por favor, ingrese un apartado, no un número.\n")
    
def agregarPuntos(codigo:str):
    """ Esta función es la encargada de agregar los puntos a cada apartado, el primer punto es agregado de manera obligatoria,
        los demás se realizan mediante un ciclo, tiene que ingresar si o no para seguir agregando puntos, no importa de la manera
        en la que ingresen, si es si o no el programa lo reconocerá como tal.
    Args:
        codigo (str): Es el código del apartado en los que van los puntos, ya que deben estar asociados.
    """
    seguirPreguntando=1
    codigoPunto=1
    #Agrega un único punto.
    while True:
        punto = input("Agrege un punto al apartado por favor: ")
        if not punto.isnumeric():
            registroPuntos.append([str(codigoPunto),punto,codigo])
            codigoPunto+=1
            break
        else:
            print("Por favor, ingrese un punto que no sea solo un número.\n")
            
    #Permite agregar más puntos.      
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
    """Esta función realiza la pregunta de si agregar más apartados, el usuario debe digitar si o no, no importa en la manera 
        que lo haga, el programa lo reconocerá. Si digita si se agregará otro apartado, si digita no no se
    """
    while True:
            respuesta = input('¿Desea ingresar otro apartado? Digite "si" si desea hacerlo digite "no" si no lo desea hacer: ')
            if unidecode(respuesta.lower()) == "si":
                registroApartados.clear()
                agregarApartados()
                agregarPuntos(agregarCodigoapartado(registroApartados))
        
            elif unidecode(respuesta.lower()) == "no":
                print("\nEntendido no se agregarán más apartados.")
                print("\n El registo de agenda ha terminado.")
                break
            else:
                print("Por favor, responda con 'si' o 'no'.\n")           
#-------------------------------------------------------------------------------------------------------------------------
 #Sección de reconociminto de voz----------------------------------------------------------------------------------------
def apartadoDeseado():
    """ Esta función imprime los apartados enumerados, el usuario debe escoger el apartado, digitando el índice correspondiente
        si no existe el índice o escribe texto, no lo permitirá y pedirá que lo vuelva a ingresar.No tiene argumentos o return.
    Returns:
        _str_: Es el apartado al que se ingresó.
    """
    for i, apartado in enumerate(registroApartadosFinal):
        print(str(i) + ": " + apartado[1])
    
    while True:
        try:
            indice=int(input("Ingrese el índice correspondiente al apartado al que desea ingresar: "))
            print("\n")
            apartadoQuerido = registroApartadosFinal[indice][1]
            return apartadoQuerido
                
        except:
            print("El índice indicado no es válido.")
                
def retornarClaveApartado(apartado:str):
    """Esta función retorna el código del apartado al que se ingresó previamente.
    Args:
        apartado (str): Es el apartado al que se desea obtener el código/clave.
    Returns:
        _str_: Es el código/clave del apartado.
    """
    for i in registroApartadosFinal:
        if i[1] == apartado:
            return i[0]
          
def puntodoDeseado(apartado:str):
    """ Esta función enumera los puntos del apartado al que se ingresó previamente. Posee la función que solo permita ingresar
        índice válidos.
    Args:
        apartado (str): Es la código/clave del apartado.
    Returns:
        _tuple_: retorna una tupla con el punto y la clave del apartado.
    """
    for i, sublista in enumerate(registroPuntos):
        if sublista[2] == apartado:
            print(f"{i}-{sublista[1]}")
            
    while True:
        try:
            indice=int(input("Ingrese el índice correspondiente al apartado al que desea ingresar: "))
            punto = registroPuntos[indice][1]
            return punto,apartado
                    
        except:
            print("El índice indicado no es válido.")
         
def retornarClavePunto(punto:str,apartado:str):
    """Permite retorna el código/clave del punto deseado.
    Args:
        punto (str): El punto.
        apartado (str): El código/clave del apartado.
    Returns:
        _str_: Código/clave del punto.
    """
    for i in registroPuntos:
        if i[1]==punto and i[2]==apartado:
            return i[0],apartado

def generarClaves():
    """Esta función es la que permite obtener las códigos/claves del apartado y el punto deseado.
    Returns:
        _tuple_: Ambos códigos/claves del apartado y del punto.
    """
    apartado=retornarClaveApartado(apartadoDeseado())
    Punto,Apartado=puntodoDeseado(apartado)
    clavePunto,claveApartado=retornarClavePunto(Punto,Apartado)
    return clavePunto ,claveApartado

def obtenerParticipante():
    """ Esta función permite obtener el participante mediante un menú desplegable enumerado.
        Solo permite ínidices válidos.
        
        Returns:
        _str_: El participante.
    """
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
    """Esta función genera la hora en formato %H:%M:%S.
    Returns:
        _str_: Hora actual.
    """
    now = datetime.datetime.now()
    horaActual = now.strftime("%H:%M:%S")
    return horaActual      

def hablar():
    """Esta función utiliza speech_recognition para guardar lo que se dice mediante el micrófono.  
    Returns:
        _str_: Lo que se dijo en texto.
    """
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
    """ Esta función combina diferentes funciones, permite guardar lo dicho por un usuario en una hora, además de 
        vincularlo mediante código/clave al partado y punto deseado. También numera cada uno de estos reconocimientos.
        Esto lo agrega en registroVoz.
        Un ejemplo como: [["1","Usuario","ClaveApartado","ClavePunto","Lo dicho por esa persona","fecha"],[...]]
    
    Returns:
    _tuple_: El código/clave de tanto del apartado como del punto, también el participante.
    """
    global codigoVoz
    clavePunto,claveApartado=generarClaves()  
    participante=obtenerParticipante()
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1
    return(clavePunto,claveApartado,participante)
    
def reconocimientoSinAgenda(clavePunto:str,claveApartado:str):
    """Esta función permite agregar texto dicho por un particpante pero a un apartado y punto ya establecido.No posee return.
    Args:
        clavePunto (str): Código/clave del punto donde se va a agregar el texto
        claveApartado (str): Código/clave del apartado donde se va a agregar el texto
    """
    global codigoVoz
    participante=obtenerParticipante()
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1
 
def reconocimientoSinParticipanteAgenda(clavePunto:str,claveApartado:str,participante:str):
    """Esta función permite agregar texto dicho por un mismo particpante pero a un apartado y punto ya establecido.No posee return.
    Args:
        clavePunto (str): Código/clave del punto donde se va a agregar el texto.
        claveApartado (str): Código/clave del apartado donde se va a agregar el texto.
        participante (str): participante al que se le desea agregar el texto.
    """
    global codigoVoz
    fecha=registroFecha()
    texto=hablar()
    registroVoz.append([str(codigoVoz),participante,claveApartado,clavePunto,texto,fecha])
    codigoVoz+=1

def siguienteAccion(claves:tuple):
    """ Esta función se utiliza para saber cuál acción se realiza a continuación, las cuales son: 
        Sigue hablando la misma persona, Otro miembro toma la palabra, Entendido, este punto de la agenda ha sido discutido
        esto se realiza mediante un menú desplegable numerado, el cual solo permite ínidices válidos. No posee return.
    Args:
        claves (tuple): Necesita las claves para poder utilizar las funciones dependiendo de la opción elegida.
    Raises:
        ValueError: Se utiliza para un caso en que el índice no sea válido.
    """
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
    """ Esta función permite continuar realizando reconocimiento, se debe indicar mediante si o no, no importa la manera en la que estas
        respuestas sean escritas, el programa las detectará de manera válida. Si se digita que sí se termina el reconocimiento.
    Raises:
        ValueError: Se utliza para el casi que no se digite si o no.
    """
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
    """Esta función genera un menú desplegable enumera con índices, el cual contiene las opciones de los reportes. No contiene return.
    Raises:
        ValueError: Se utiliza en caso de que el índice indicado no se válido.
    """
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
    """ Esta función pregunta al usuario si desea seguir imprimiendo reportes, mediante la escritura de si o no, no importa la forma en 
        la que se digiten estos, el programa lo reconocerá como válido. Si se digita que no se termina el programa. No contiene return.
    Raises:
        ValueError: Se utiliza si no se digita si o no.
    """
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
def imprimirVoz(apartados:list, puntos:list,voz:list):
    """Esta función permite imprimir lo dicho por cada participante en cada punto y en cada apartado. No contiene return.
    Args:
        apartados (list): Es la lista con los apartados y códigos/claves
        puntos (list): Es la lista con los puntos y códigos/claves.
        voz (list): La lista donde se contiene la información de participante, dicho, fecha, Apartado y punto
    """
    for apartado in apartados:
        print(apartado[1] + ":")
        for punto in puntos:
            if punto[2] == apartado[0]:
                print("\t" + punto[1] + ":")
                for v in voz:
                    if v[2] == apartado[0] and v[3] == punto[0]:
                        print("\t\t" + v[1] + " " + v[5]+ ": "  + " " + v[4])

def primerReporte():
    """Imprime el reporte con los argumentos necesarios.
    """
    imprimirVoz(registroApartadosFinal,registroPuntos,registroVoz)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Segundo reporte--------------------------------------------------------------------------------------------------------------------------------------------
def obtenerRecuentoPalabras(personas:list, registro:list):
    """Esta función obtiene la cantidad de palabras que cada persona dijo durante todo elvreconocimiento.
    Args:
        personas (list): La lista de usuarios
        registro (list): La lista donde se contiene la información de participante, dicho, fecha, Apartado y punto
    Returns:
        _list_: Lista con sublista para cada usuario que contiene la cantidad de palabaras dichas por cada persona y la persona.
    """
    global recuento
    for persona in personas:
        palabrasDichas = 0
        for registroPersona in registro:
            if registroPersona[1] == persona:
                palabrasDichas += len(registroPersona[4].split())
        # Buscamos si ya existe un elemento en recuento que corresponda a esta persona
        existePersona = False
        for i in range(len(recuento)):
            if recuento[i][0] == persona:
                recuento[i][1] += palabrasDichas
                existePersona = True
                break
        # Si no encontramos la persona en recuento, la agregamos como un nuevo elemento
        if not existePersona:
            recuento.append([persona, palabrasDichas])
    return recuento

def ordenarListaDescendiente(lista:list):
    """Esta función ordena la de mayor a menor con la cantidad de palabras dicha por cada persona.
    Args:
        lista(list): Lista con sublista para cada usuario que contiene la cantidad de palabaras dichas por cada persona y la persona.
    Returns:
        _list_: La lista ordenada.
    """
    cantidadLista = len(lista)
    while cantidadLista > 1:
        for i in range(cantidadLista-1):
            if lista[i][1] < lista[i+1][1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        cantidadLista -= 1
    return lista

def segundoReporte():
    """Esta función imprime la lista ordena. De manera: 'Persona x palabras'
    """
    listaOrdenada=ordenarListaDescendiente(obtenerRecuentoPalabras(registroParcicipantes,registroVoz))
    print("A continuación se mostrará de orden descendente las personas de más palabras dijeron: \n")
    for elemento in listaOrdenada:
        print(elemento[0], "con", elemento[1],"palabras")
        print("\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#Tercer reporte
def contarHablado(apartados:list, puntos:list, usuarios:list, voz:list):
    """Cuenta la cantidad de veces que cada usuario habló en cada punto.
    Args:
        apartados (list): Lista con los apartados
        puntos (list): Lista con los puntos
        usuarios (list): Lista con los usuarios
        voz (list): La lista donde se contiene la información de participante, dicho, fecha, Apartado y punto
    """
    for apartado in apartados:
        print(apartado[1] + ": \n")
        for punto in puntos:
            if punto[2] == apartado[0]:
                print("\t" +punto[1] + ": \n")
                for usuario in usuarios:
                    contador = 0
                    for voz_item in voz:
                        if (voz_item[1] == usuario and voz_item[2] == apartado[0] 
                                and voz_item[3] == punto[0]):
                            contador += 1
                    if contador > 0:
                        print(f"{usuario}: Intervino {contador} vez/veces")
def tercerReporte():
    """Realiza el reporte con los argumentos necesarios.
    """
    contarHablado(registroApartadosFinal,registroPuntos,registroParcicipantes,registroVoz)
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def ejecuciónPrograma():
    """Aquí se encuentran las funciones en el orden necesario para ejecutar el programa.
    """
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