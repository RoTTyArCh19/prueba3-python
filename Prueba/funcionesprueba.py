TIPOLIBRO = ['ficcion','no ficcion', 'ciencia']
def registarlibro(libreria):
    titulo = input("Ingrese titulo del libro: ") 
    autor = input("Ingrese autor del libro: ")
    tipolib = input("ingrese el genero del libro ficcion/no ficcion/ciencia").lower()
    while tipolib in TIPOLIBRO:
        print("tipo de libro no existe")
        tipolib = input("Ingrese el genero del libro ficcion/no ficcion/ciencia : ").lower()
    precio = int(input("ingrese el valor del libro:"))
    libreria.append({
        'titulo' : titulo,
        'autor'  : autor,
        'tipolib' : tipolib,
        'precio'  : precio
    })
def listalibros(Libreria):
    print("Lista de libros")
    for libro in libreria:
        print(libreria)     
def registroventa(Libreria):
    print("")
def reporteventas(Libreria):
    print("")
def generartxt(Libreria):
    

