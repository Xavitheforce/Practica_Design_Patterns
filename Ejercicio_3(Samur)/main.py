from controlador import gestor_documentos
from utils import separador
from gestion_usuarios import gestor_usuarios
from time import sleep

if __name__ == "__main__":
    #borrar el contenido de logs.txt
    logs = open('Ejercicio_3(Samur)/logs.txt', 'w')
    logs.write("")
    logs.close()
    print("Bienvenido al gestor de documentos")
    separador()
    print("Identifíquese:")
    separador()
    separador()
    identificacion = gestor_usuarios()
    if identificacion:
        bool = True
        while bool:
            separador()
            bool = gestor_documentos()
            sleep(2)