import inspect #CHECK DATACODE
import GUI

#CONTAR FUNCIONES Y RETORNAR NUMERO
def count_functions(module):

    function_list = inspect.getmembers(module, inspect.isfunction)
    number = len(function_list)

    return number

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster(defNumber):

    #PROJECT-DATA
    proyectName = "SpamerBot"
    developer = "MAURO PEPA"
    proyectVersion = "1.2"

    developerCretis = "\n"+proyectName+ " - BY "+developer+" - V"+proyectVersion+"."+defNumber
    print(developerCretis)

    LongNumberStick = "-"*len(developerCretis)
    print(LongNumberStick)

def printCredits():

    #MODULES PROYECTS
    defNumber = count_functions(GUI)

    printCodeMaster(str(defNumber))

if __name__ == '__main__':
    printCredits()