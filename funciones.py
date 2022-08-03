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

resp = multiplicacion(8,10)
print(resp)