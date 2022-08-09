def suma(num1: int,num2: int) -> int:
    """Esta función suma dos números enteros

    Args:
        num1 (int): numero a sumar
        num2 (int):numero a sumar

    Returns:
        int: suma de los dos numeros
    """
    resultado = num1 + num2
    return resultado

resp = suma('santiago',' Echeverri')
print(resp)

def multiplicacion(num1,num2):
    """Función que calcula la multiplicación de dos números

    Args:
        num1 (int, float,str): Numero a multiplicar
        num2 (int, float,str): numero a multiplicar

    Returns:
        int, float,str: multiplicar
    """
    resultado = num1 * num2
    return resultado

def division(num1,num2):
    try:
        respuesta = num1/num2
        return respuesta
    except Exception  as e:
        raise f'Se está dividiendo por 0, por favor cambie los argumentos: {e}'

resp = division('santiago',1)
print(resp)

def es_par(numero) -> bool:
    """
        esta función me indica si el numero que estoy evaluando es par o no.
    """
    if numero % 2 == 0:
        return True
    else:
        return False 