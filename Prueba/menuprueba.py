#Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente
#caso: Una librería necesita desarrollar una aplicación que permita registrar libros en el
#inventario y realizar ventas. Para ello, la aplicación debe cumplir con las siguientes
#funcionalidades:
#Registrar libro: Para registrar un libro se requiere lo siguiente: Título, Autor, Género, Precio.
#Debe validar que todos los datos sean ingresados, los cuales no deben quedar vacíos
#Listar todos los libros: Debe mostrar en la pantalla la lista de todos los libros registrados.
#Registrar venta: Para registrar una venta se requiere lo siguiente: Título del libro, Cantidad
#vendida, precio por unidad y precio final. Debe validar que el título exista en el inventario y
#que la cantidad no exceda el stock disponible. Simule una boleta estándar
#Imprimir reporte de ventas: Para imprimir el reporte de ventas, el usuario puede seleccionar
#imprimir todos o por un género en específico. Estos géneros deben estar previamente
#definidos en una colección de Python en el código y por lo menos deben ser tres, por ejemplo:
#"Ficción", "No Ficción", "Ciencia".
#Generar TXT: Debe exportar a un archivo txt con el registro de las ventas
#Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe
#ser llamada desde el programa principal.








import funcionesprueba as fn

Libreria = []

while True:
    print("-------------MENU-------------")
    print("1.Registrar libro")
    print("2.Listar todos los libros")
    print("3.Registrar venta")
    print("4.Imprimir reporte de ventas")
    print("5.Generar txt")
    print("6.Salir del Programa")
    print("------------------------------")
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        fn.registarlibro(Libreria)
    elif opcion == 2:
        fn.listalibros(Libreria)
    elif opcion == 3:
        fn.registroventa(Libreria)
    elif opcion == 4:
        fn.reporteventas(Libreria)
    elif opcion == 5:
        fn.generartxt(Libreria)
    elif opcion == 6:
        break
    else:
        print("!ERROR USTED NO ELIGIO UNA OPCION EXISTENTE!")