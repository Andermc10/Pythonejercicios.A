# inventario=[]

# while True:
#     print ("Menú principal ")
#     print ("1. Registrar libro")
#     print ("2. Buscar libro por titulo")
#     print ("3. Eliminar libro por titulo")
#     print ("4. Mostrar todos los libros")
#     print ("5. Generara reporte de los libros ")
#     print ("6. Salir")
    
#     opcion=input("Seleccione una opción (1-6)")

#     if opcion not in ["1","2","3","4","5","6"]:
#      print("Opción inválida, por favor seleccione una opción del 1 al 6")
    
#      continue    

#     if opcion =="1":
#         print ("Reegistrar libro")
#         while True:
#             titulo=input("Ingrese el titulo del libro :").strip()
#             if titulo:
#                 break
#             print("El titulo no puede estar vacio")
            
#         while True:
#             autor=input("Ingrese e nombre del autor :"). strip()
#             if autor:
#                 break
#             print("El nombre del autor no puede estar vacio")
            
#         while True:
#             try:
#                 anio=int(input("Año de publicación"))
#                 if anio>0:
#                     break
#                 else:
#                     print("El año debe ser un número positivo")
#             except ValueError:
#                 print("Debes ingresar un número valido")
        
#         while True:
#             try:
#                 precio=float(input("Precio del libro"))
#                 if precio>0:
#                     break
#                 else:
#                     print("El precio debe ser un número positivo mayor a 0")
#             except ValueError:
#                 print("Debes ingresar un número valido ")
                
#         Libro= {
#             "Titulo":titulo,
#             "Autor":autor,
#             "Año":anio,
#             "Precio":precio
#         }
#         inventario.append(Libro)
#         print(f"El libro '{titulo}' se agrego correctamente")
        
#     if opcion == "2":
#         print("Buscar libro por titulo")

#         titulo_buscar=input("Titulo del libro :").strip()
#         if not titulo_buscar:
#             print("Debes ingresar un titulo")
#             continue
#         encontrado=False
#         for Libro in inventario:
#             if Libro
                
                
            