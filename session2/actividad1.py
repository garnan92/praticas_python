def agregar(alumnos,alumno):
    alumnos.append(alumno)
    alumnos.sort()
    return alumnos

def main():
    alumnos = []
    while 1:
        nombre = input("nombre del alumno: ")
        if(nombre == "exit"):
            break
        alumnos = agregar(alumnos,nombre)
        print(alumnos)
main()