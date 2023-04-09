from unidecode import unidecode

registroParcicipantes=[]
registroApartados=[]
registroApartadosFinal=[]
registroPuntos=[]

def agregarParticipantes():
    print("Se procede a realizar el registro de participantes\n")
    
    seguirPreguntando=1
    posicionDondeAgregar=0
    
    #Se realiza para que exista al menos un paticipante
    while True:
        participante = input("Agrege un participanta al registro por favor: ")
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
    

#menuParticipantes()
agregarApartados()
agregarPuntos(agregarCodigoapartado(registroApartados))
masApartados()
print(registroPuntos)

#print(accederApartado())
