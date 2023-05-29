import re

# Definir los patrones de expresiones regulares para los tokens
patrones_tokens = [
    ('REAL', r'-?(\d+)?\.(\d+([eE](-?(\d+)?)?)?)?'),  # Números reales
    ('ENTERO', r'\d+'),  # Números enteros
    ('COMENTARIO', r'//[^\n]*'),  # Comentarios
    ('VARIABLE', r'\w+(_\d\w)*'),  # Identificadores
    ('SUMA', r'\+'),  # Operador de suma
    ('RESTA', r'-'),  # Operador de resta
    ('MULTIPLICACION', r'\*'),  # Operador de multiplicación
    ('DIVISION', r'/'),  # Operador de división
    ('POTENCIA', r'\^'),
    ('ASIGNACION', r'='),  # Operador de asignación
    ('PARENTESIS QUE ABRE', r'\('),
    ('PARENTESIS QUE CIERRA', r'\)'),
]

# Función para realizar el análisis léxico
def lexor(codigo):
    tokens = []
    posicion = 0

    while posicion < len(codigo):
        match = None

        for nombre_token, patron in patrones_tokens:
            expresion_regular = re.compile(patron)
            match = expresion_regular.match(codigo, posicion)

            if match:
                valor = match.group(0)
                if nombre_token == 'COMENTARIO':
                    valor = valor.strip()  # Obtener el contenido del comentario sin espacios al inicio y final
                    tokens.append((valor, nombre_token))  # Agregar el comentario como un token
                else:
                    tokens.append((valor, nombre_token))
                posicion = match.end(0)
                break

        if not match:
            # Omitir espacios en blanco
            if not codigo[posicion].isspace() and codigo[posicion] != '\n':
                tokens.append((codigo[posicion], "TOKEN NO RECONOCIDO"))  # Agregar el token no reconocido
            posicion += 1

    return tokens

# Función para verificar los tipos de los tokens
def verificar_tipos(tokens):
    if tokens is None:
        return
    for token, tipo in tokens:
        if tipo == 'ENTERO':
            # Verificar si el token es un número válido
            if not token.isdigit():
                raise Exception(f"Token '{token}' no es un número válido")
        elif tipo == 'VARIABLE':
            # Verificar si el token es un identificador válido
            if not token.isidentifier():
                raise Exception(f"Token '{token}' no es un identificador válido")
        # Agregar más condiciones de verificación de tipos según tus necesidades

# Realizamos lectura de datos
archivo = open("datos.txt","r")
contenido=archivo.read()
archivo.close()


# Ejemplo de uso
tokens = lexor(contenido)

try: 
    verificar_tipos(tokens)
    
    # Imprimir los tokens generados
    for token, tipo in tokens:
        print(f"Token: {token}, Tipo: {tipo}")

except Exception as e:
    print("Error:", str(e))