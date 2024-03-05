class Tokens:
    tokens = [
        "LLAVE_ABRE",
        "LLAVE_CIERRA",
        "COMA",
        "DOS_PUNTOS",
        "NUMERO",
        "CADENA_COMILLAS",
        "CADENA_NO_COMILLAS",
        # "TRUE",
        # "FALSE",
        # "NULO",
        "IGUAL",
        "MAYOR",
        "MENOR",
        "MAYOR_IGUAL",
        "MENOR_IGUAL"
        # "ENTERO",
        # "DECIMAL",
        # "CIENTIFICO",
        # "BINARIO",
        # "OCTAL",
        # "HEXADECIMAL"
    ]

    reserved = {
        "tr": "TRUE",
        "fl": "FALSE",
        "null": "NULO",
        "TR": "TRUE",
        "FL": "FALSE",
        "NULL": "NULO"
    }