import speech_recognition as sr
from unidecode import unidecode

personas = {}  # Diccionario para almacenar lo que se dice por cada persona
nombres = ['Ana', 'Pedro', 'María']  # Lista de nombres


def hablar(indice: int):
    nombre = nombres[indice]
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    try:
        print("inicia el reconocimiento...\n")
        texto = r.recognize_google(audio, language='es-ES')
        print("Has dicho: " + texto)
        if nombre in personas:
            personas[nombre].append(texto)
            return(indice)
        else:
            personas[nombre] = [texto]  
            return(indice)
    except:
        print("Lo siento, no he entendido lo que has dicho.") 


def quienHabla():
    for i, nombre in enumerate(nombres):
                print(str(i) + ": " + nombre) 
    while True:
        try:
            indice=int(input("Indica tu nombre mediante el índice: "))   
            nombre = nombres[indice]     
        except:
            print("El índice indicado no es válido.")
        
        return(indice)

def maximoIntervenciones():
    indice=intervenciones
    numeroElementos=len(personas[indice])
    
    if numeroElementos==4:
        return("Puede")
    else:
        return("No puede")


def siguePersona(i):  
    indice=i
    
    while True:
        respuesta = input('¿Va a hablar la misma persona? Digite "si" si es así,  digite "no" si no lo es: ')
        if unidecode(respuesta.lower()) == "si": 
            if maximoIntervenciones()=="Puede":
                hablar(indice)
                break
            elif maximoIntervenciones()=="No puede":
                print("No puede intervenir más de dos veces")
                break
        
        elif unidecode(respuesta.lower()) == "no":
            print("Entendido, va a hablar otra persona\n")
            hablar(quienHabla())
            break
        
        else:
            print("Por favor, responda con 'si' o 'no'.\n")  

hablar(quienHabla())
intervenciones=quienHabla()
siguePersona()


print(personas)


