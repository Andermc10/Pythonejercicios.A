

clientes = []

# Variable para generar números de cuenta automáticos
numero_cuenta_actual = 1000



# FUNCIÓN PARA REGISTRAR UN CLIENTE

def registrar_cliente():
    global numero_cuenta_actual

    print("\n--- Registrar cliente ---")

    # Validar nombre
    while True:
        nombre = input("Nombre del cliente: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    # Verificar si el cliente ya existe
    for cliente in clientes:
        if cliente["Nombre"].lower() == nombre.lower():
            # Si ya tiene 3 cuentas, no puede registrar más
            if len(cliente["Cuentas"]) >= 3:
                print(" Este cliente ya tiene el máximo de 3 cuentas.")
                return
            else:
                print("Cliente encontrado. Se creará una nueva cuenta.")
                break
    else:
        # Si el cliente no existe, se crea uno nuevo
        cliente = {"Nombre": nombre, "Cuentas": []}
        clientes.append(cliente)

    # Validar saldo inicial
    while True:
        try:
            saldo = float(input("Saldo inicial (mínimo $100.000): "))
            if saldo >= 100000:
                break
            else:
                print("El saldo debe ser mínimo de $100.000.")
        except ValueError:
            print("Debes ingresar un número válido.")

    # Crear la cuenta
    numero_cuenta_actual += 1
    cuenta = {
        "Número de cuenta": numero_cuenta_actual,
        "Saldo": saldo,
        "Total depositado": 0,
        "Total retirado": 0
    }
    cliente["Cuentas"].append(cuenta)

    print(f"Cuenta creada correctamente. Número de cuenta: {numero_cuenta_actual}")


# FUNCIÓN PARA CONSULTAR SALDO
def consultar_saldo():
    print("\n--- Consultar saldo ---")
    try:
        numero = int(input("Número de cuenta: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    for cliente in clientes:
        for cuenta in cliente["Cuentas"]:
            if cuenta["Número de cuenta"] == numero:
                print(f"\nCliente: {cliente['Nombre']}")
                print(f"Número de cuenta: {numero}")
                print(f"Saldo actual: ${cuenta['Saldo']:.2f}")
                return

    print("Cuenta no encontrada.")


# FUNCIÓN PARA REALIZAR DEPÓSITO

def realizar_deposito():
    print("\n--- Depósito ---")
    try:
        numero = int(input("Número de cuenta: "))
        monto = float(input("Monto a depositar: "))
    except ValueError:
        print("Debes ingresar números válidos.")
        return

    if monto <= 0:
        print("El monto debe ser mayor a cero.")
        return

    for cliente in clientes:
        for cuenta in cliente["Cuentas"]:
            if cuenta["Número de cuenta"] == numero:
                cuenta["Saldo"] += monto
                cuenta["Total depositado"] += monto
                print(f"Depósito exitoso. Nuevo saldo: ${cuenta['Saldo']:.2f}")
                return

    print("Cuenta no encontrada.")



# FUNCIÓN PARA REALIZAR RETIRO

def realizar_retiro():
    print("\n--- Retiro ---")
    try:
        numero = int(input("Número de cuenta: "))
        monto = float(input("Monto a retirar (múltiplo de $10.000): "))
    except ValueError:
        print("Debes ingresar números válidos.")
        return

    if monto <= 0 or monto % 10000 != 0:
        print("El monto debe ser múltiplo de $10.000 y mayor a cero.")
        return

    for cliente in clientes:
        for cuenta in cliente["Cuentas"]:
            if cuenta["Número de cuenta"] == numero:
                if cuenta["Saldo"] >= monto:
                    cuenta["Saldo"] -= monto
                    cuenta["Total retirado"] += monto
                    print(f"Retiro exitoso. Nuevo saldo: ${cuenta['Saldo']:.2f}")
                else:
                    print("Fondos insuficientes.")
                return

    print("Cuenta no encontrada.")


# FUNCIÓN PARA MOSTRAR TODOS LOS CLIENTES

def mostrar_clientes():
    print("\n--- Lista de clientes y cuentas ---")
    if not clientes:
        print("No hay clientes registrados.")
        return

    for i, cliente in enumerate(clientes, start=1):
        print(f"\nCliente #{i}: {cliente['Nombre']}")
        for cuenta in cliente["Cuentas"]:
            print(f"  Cuenta: {cuenta['Número de cuenta']} - Saldo: ${cuenta['Saldo']:.2f}")


# FUNCIÓN PARA GENERAR REPORTE POR CLIENTE

def generar_reporte():
    print("\n--- Reporte por cliente ---")
    nombre = input("Nombre del cliente: ").strip()

    for cliente in clientes:
        if cliente["Nombre"].lower() == nombre.lower():
            print(f"\n Reporte de {cliente['Nombre']}")
            for cuenta in cliente["Cuentas"]:
                print(f"\nCuenta N°: {cuenta['Número de cuenta']}")
                print(f"  Total depositado: ${cuenta['Total depositado']:.2f}")
                print(f"  Total retirado: ${cuenta['Total retirado']:.2f}")
                print(f"  Saldo actual: ${cuenta['Saldo']:.2f}")
            return

    print("Cliente no encontrado.")


# FUNCIÓN PRINCIPAL (MENÚ)

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar cliente / cuenta")
        print("2. Consultar saldo")
        print("3. Realizar depósito")
        print("4. Realizar retiro")
        print("5. Mostrar todos los clientes")
        print("6. Generar reporte por cliente")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            consultar_saldo()
        elif opcion == "3":
            realizar_deposito()
        elif opcion == "4":
            realizar_retiro()
        elif opcion == "5":
            mostrar_clientes()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            print("Gracias por usar el sistema bancario. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


menu_principal()
