from collections import namedtuple
from Expresiones import *
from Expresiones.aritmeticas import ExpresionAritmetica
from Expresiones.trigonometricas import ExpresionTrigonometrica
from Graficas.Arbol import *

from Error import Error
import json

# Estructura de token:
Token = namedtuple("Token", ["value", "line", "col"])
# numero de linea
line = 1
# numero de columna
col = 1
tokens = []
# array de errores
errores = []
# Guarda las configuraciones
configuracion = {
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}

# formar un string
def tokenize_string(input_str, i):
    token = ""
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("Error: string no cerrado")


# formar un numero
def tokenize_number(input_str, i):
    token = ""
    isDecimal = False
    for char in input_str:
        if char.isdigit():
            token += char
            i += 1
        elif char == "." and not isDecimal:
            token += char
            i += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(token), i]
    return [int(token), i]


# formar los tokens
def tokenize_input(input_str):
    # referenciar las variables globales
    global line, col, tokens
    line = 0
    col = 0
    # iterar sobre cada caracter del input
    i = 0
    # mientras no se llegue al final del input
    while i < len(input_str):
        # obtener el caracter actual
        char = input_str[i]
        #char2 =ord(input_str[i])
        if char.isspace():
            # si es un salto de linea
            if char == "\n":
                # print({"char": char, "line": line, "col": col, "i": i})
                # tokens.append("EOL")
                line += 1
                col = 1
            # si es un tabulador
            elif char == "\t":
                col += 4
            # si es un espacio
            else:
                col += 1
            # incrementar el indice
            i += 1
        # si es un string formar el token
        elif char == '"':
            string, pos = tokenize_string(input_str[i + 1 :], i)
            col += len(string) + 1
            i = pos + 2
            token = Token(string, line, col)
            tokens.append(token)
        elif char in ["{", "}", "[", "]", ",", ":"]:
            #print({"char": char, "line": line, "col": col, "i": i})
            col += 1
            i += 1
            token = Token(char, line, col)
            tokens.append(token)
        elif char.isdigit():
            number, pos = tokenize_number(input_str[i:], i)
            col += pos - i
            i = pos
            token = Token(number, line, col)
            tokens.append(token) 
        #-------------Este error se deve de ingresar al json de salida-----------------     
        else:
            # se almacena el error utilizando la clase Error
            errores.append(Error(char, 'Error Lexico', col + 1, line+1))
            i += 1
            col += 1
    # Se recorren los errores de entrada para verlos
    # for error in errores:
    #     print(error)

# crear las instrucciones a partir de los tokens
def get_instruccion():
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        #print("VALUE: ", token)
        try:
            if token.value == "operacion":
                # eliminar el :
                tokens.pop(0)
                operacion = tokens.pop(0).value
            elif token.value == "valor1":
                # eliminar el :
                tokens.pop(0)
                value1 = tokens.pop(0).value
                if value1 == "[":
                    value1 = get_instruccion()
            elif token.value == "valor2":
                # eliminar el :
                tokens.pop(0)
                value2 = tokens.pop(0).value
                if value2 == "[":
                    value2 = get_instruccion()
            elif token.value in ["texto", "fondo", "fuente", "forma"]:
                tokens.pop(0)
                configuracion[token.value] = tokens.pop(0).value
            # else:
            #     print("\033[1;31;40m Error: token desconocido:", token, "\033[0m")
            temporal = str(operacion).lower()

            if temporal and value1 and value2:
                return ExpresionAritmetica(temporal, value1, value2, 0, 0)
            
            #----agregar el coseno, tangente:------
            if temporal and temporal in ["seno", "coseno", "tangente", "inverso"] and value1:
                return ExpresionTrigonometrica(temporal, value1, 0, 0)
        except Exception as e:
            print()
            #print("Error: en la funcion get_instruccion.")
            continue
    return None

def create_instructions():
    global tokens
    global arbol
    instrucciones = []
    while tokens:
        instruccion = get_instruccion()
        if instruccion:
            instrucciones.append(instruccion)
    arbol.agregarConfiguracion(configuracion)
    return instrucciones


def analizar(entrada):
    errores.clear()
    tokenize_input(entrada)
    arbol.dot.clear()
    arbol.agregarConfiguracion(configuracion)
    instrucciones = create_instructions()
    for i in instrucciones:
        i.interpretar()
        #print("RESULTADO INSTRUCCION: ", i.interpretar())
    #archivoDeSalida()
    return arbol


def archivoDeSalida():
    # Lista para almacenar los objetos JSON de errores individuales
    errores_json = []

    # Convierte cada error en un diccionario JSON y agrégalo a la lista
    for i, error in enumerate(errores, start=1):
        error_dict = {
            "No": i,
            "descripcion": {
                "lexema": error.lexema,
                "tipo": error.tipo,
                "columna": error.columna,
                "fila": error.fila,
            },
        }
        errores_json.append(error_dict)

    # Crea el diccionario JSON final
    resultado_json = {"errores": errores_json}

    # Nombre del archivo de salida JSON
    nombre_archivo = "RESULTADOS_202101927.json"

    # Escribe el diccionario JSON en el archivo
    with open(nombre_archivo, "w") as archivo_json:
        json.dump(resultado_json, archivo_json, indent=4)

    # Mensaje de salida
    #print(f"Archivo JSON '{nombre_archivo}' creado con éxito.")