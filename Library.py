# ==========================================
# SISTEMA DE GESTIÓN DE LIBRERÍA (versión con funciones)
# ==========================================

# Lista donde se guardan los libros
inventario = []


# ------------------------------------------
# FUNCIÓN PARA REGISTRAR UN LIBRO
# ------------------------------------------
def registrar_libro():
    print("\n--- Registrar libro ---")

    # Validar título
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("El título no puede estar vacío.")

    # Validar autor
    while True:
        autor = input("Autor: ").strip()
        if autor:
            break
        print("El autor no puede estar vacío.")

    # Validar año
    while True:
        try:
            anio = int(input("Año de publicación: "))
            if anio > 0:
                break
            else:
                print("El año debe ser positivo.")
        except ValueError:
            print("Debes ingresar un número válido.")

    # Validar precio
    while True:
        try:
            precio = int(input("Precio: "))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Debes ingresar un número válido.")

    # Crear libro y agregar al inventario
    libro = {
        "Título": titulo,
        "Autor": autor,
        "Año": anio,
        "Precio": precio
    }
    inventario.append(libro)
    print(f"Libro '{titulo}' agregado correctamente.")


# ------------------------------------------
# FUNCIÓN PARA CONSULTAR UN LIBRO POR TÍTULO
# ------------------------------------------
def consultar_libro():
    print("\n--- Consultar libro ---")
    titulo_buscar = input("Título del libro: ").strip()

    if not titulo_buscar:
        print("Debes ingresar un título.")
        return

    for libro in inventario:
        if libro["Título"].lower() == titulo_buscar.lower():
            print("\nLibro encontrado:")
            for clave, valor in libro.items():
                print(f"  {clave}: {valor}")
            return

    print("Libro no encontrado.")


# ------------------------------------------
# FUNCIÓN PARA ELIMINAR UN LIBRO
# ------------------------------------------
def eliminar_libro():
    print("\n--- Eliminar libro ---")
    titulo_eliminar = input("Título del libro: ").strip()

    if not titulo_eliminar:
        print("Debes ingresar un título.")
        return

    for libro in inventario:
        if libro["Título"].lower() == titulo_eliminar.lower():
            inventario.remove(libro)
            print(f"Libro '{titulo_eliminar}' eliminado.")
            return

    print("Libro no encontrado.")


# ------------------------------------------
# FUNCIÓN PARA MOSTRAR TODOS LOS LIBROS
# ------------------------------------------
def mostrar_libros():
    print("\n--- Lista de libros ---")
    if not inventario:
        print("No hay libros registrados.")
    else:
        for i, libro in enumerate(inventario, start=1):
            print(f"\nLibro #{i}:")
            for clave, valor in libro.items():
                print(f"  {clave}: {valor}")


# ------------------------------------------
# FUNCIÓN PARA GENERAR REPORTE
# ------------------------------------------
def generar_reporte():
    print("\n--- Reporte del inventario ---")
    if not inventario:
        print("No hay libros registrados.")
        return

    total = len(inventario)
    precios = [libro["Precio"] for libro in inventario]
    promedio = sum(precios) / total
    caro = max(inventario, key=lambda x: x["Precio"])
    barato = min(inventario, key=lambda x: x["Precio"])

    print(f"Cantidad total de libros: {total}")
    print(f"Precio promedio: ${promedio:.2f}")
    print(f"Libro más caro: {caro['Título']} (${caro['Precio']})")
    print(f"Libro más barato: {barato['Título']} (${barato['Precio']})")


# ------------------------------------------
# FUNCIÓN PRINCIPAL (MENÚ)
# ------------------------------------------
def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar libro")
        print("2. Consultar libro por título")
        print("3. Eliminar libro")
        print("4. Mostrar todos los libros")
        print("5. Generar reporte")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            consultar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            generar_reporte()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


# ------------------------------------------
# INICIO DEL PROGRAMA
# ------------------------------------------
menu_principal()
