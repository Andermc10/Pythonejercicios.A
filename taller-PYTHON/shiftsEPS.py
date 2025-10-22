turnos = []
servicios = ["Medicina General", "Exámenes de Laboratorio", "Odontología"]

def pedir_nombre():
    while True:
        nombre_paciente = input("Ingrese el nombre del paciente: ").strip()
        if nombre_paciente.upper() == "FIN":
            return None
        if nombre_paciente == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
            continue
        return nombre_paciente

def pedir_motivo():
    while True:
        motivo_consulta = input("Ingrese el motivo de consulta: ").strip()
        if motivo_consulta == "":
            print("El motivo de consulta no puede estar vacío. Intente de nuevo.")
            continue
        return motivo_consulta

def pedir_servicio():
    print("Servicios disponibles:")
    for i, servicio in enumerate(servicios, start=1):
        print(f"{i}. {servicio}")
    
    while True:
        opcion = input("Seleccione el número del servicio: ").strip()
        try:
            indice_opcion = int(opcion) - 1
        except ValueError:
            print("El valor ingresado no es válido. Inténtelo de nuevo.")
            continue
        
        if 0 <= indice_opcion < len(servicios):
            return servicios[indice_opcion]
        else:
            print(f"Opción fuera de rango. Seleccione un número entre 1 y {len(servicios)}.")


print("Escriba 'FIN' como nombre para terminar el registro.")

while True:
    nombre_paciente = pedir_nombre()
    if nombre_paciente is None:
        break
    
    motivo_consulta = pedir_motivo()
    servicio_elegido = pedir_servicio()
    
    nuevo_turno = {
        "nombre": nombre_paciente,
        "motivo": motivo_consulta,
        "servicio": servicio_elegido
    }
    
    turnos.append(nuevo_turno)
    print(f"\n Turno registrado para {nombre_paciente} en {servicio_elegido}\n")

# Reporte
if len(turnos) > 0:
    print("\nREPORTE FINAL DE TURNOS\n")
    
    # Número total de turnos
    total_turnos = len(turnos)
    print(f"\n1. Número total de turnos: {total_turnos}")
    
    # Primer y último paciente 
    primer_paciente = turnos[0]["nombre"]
    ultimo_paciente = turnos[-1]["nombre"]
    
    print(f"\n2. Primer paciente registrado: {primer_paciente}")
    print(f"  Último paciente registrado: {ultimo_paciente}")
    
    # Listado alfabético de nombres
    nombres = [turno['nombre'] for turno in turnos]
    nombres.sort()
    print("\n3. Listado alfabético de nombres:")
    for nombre in nombres:
        print(f"   • {nombre}")
    
    # Cantidad de turnos 
    print("\n4. Cantidad de turnos por servicio:")
    for servicio in servicios:
        cantidad = sum(1 for turno in turnos if turno["servicio"] == servicio)
        print(f"   • {servicio}: {cantidad} turno(s)")
    
else:
    print("\nNo se registraron turnos.")