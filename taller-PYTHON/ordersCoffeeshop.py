pedidos = []

menu = {
    1: {"nombre": "papitas", "precio": 3500},
    2: {"nombre": "helados", "precio": 1500},
    3: {"nombre": "agua", "precio": 2300},
    4: {"nombre": "empanadas", "precio": 3400}
}

def pedir_numero():
    while True:
        try:
            numero = int(input("Número de pedido: "))
            for pedido in pedidos:
                if pedido["numero"] == numero:
                    print("Ese número ya existe. Intente otro.")
                    break
            else:
                return numero
        except ValueError:
            print("Debe ingresar un número válido.")

def pedir_cliente():
    while True:
        nombre = input("Nombre del cliente: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        return nombre

def mostrar_menu():
    print("\nMenú disponible:")
    for i, datos in menu.items():
        print(f"{i}. {datos['nombre']} - ${datos['precio']:,}")

def agregar_items():
    items = []
    total = 0
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione número de producto o 'fin' para terminar: ").strip().lower()
        if opcion == "fin":
            break
        if not opcion.isdigit() or int(opcion) not in menu:
            print("Opción inválida.")
            continue
        producto = menu[int(opcion)]
        try:
            cantidad = int(input(f"Cantidad de {producto['nombre']}: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        subtotal = producto["precio"] * cantidad
        items.append({
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "subtotal": subtotal
        })
        total += subtotal
        print(f"Agregado: {cantidad} {producto['nombre']} = ${subtotal:,}")
    return items, total

def registrar_pedido():
    print("\nREGISTRAR PEIDO")
    numero = pedir_numero()
    cliente = pedir_cliente()
    items, total = agregar_items()
    if len(items) == 0:
        print("Debe agregar al menos un ítem. Pedido cancelado.")
        return
    nuevo_pedido = {
        "numero": numero,
        "cliente": cliente,
        "items": items,
        "total": total
    }
    pedidos.append(nuevo_pedido)
    print(f"\nPedido #{numero} registrado. Total: ${total:,}")

def consultar_pedido():
    print("\n--- CONSULTAR PEDIDO ---")
    if len(pedidos) == 0:
        print("No hay pedidoOs registrados.")
        return
    try:
        numero = int(input("Número de pedido: "))
    except ValueError:
        print("Número inválido.")
        return
    for pedido in pedidos:
        if pedido["numero"] == numero:
            print(f"\nPedido #{pedido['numero']} - Cliente: {pedido['cliente']}")
            print("Items:")
            for item in pedido['items']:
                print(f"  {item['cantidad']} x {item['producto']} = ${item['subtotal']:,}")
            print(f"Total: ${pedido['total']:,}")
            return
    print(f"No existe el pedido #{numero}")

def cancelar_pedido():
    print("\n--- CANCELAR PEDIDO ---")
    if len(pedidos) == 0:
        print("No hay pedidos para cancelar.")
        return
    try:
        numero = int(input("Número de pedido a cancelar: "))
    except ValueError:
        print("Número inválido.")
        return
    for i, pedido in enumerate(pedidos):
        if pedido["numero"] == numero:
            confirmar = input(f"¿Cancelar pedido de {pedido['cliente']}? (si/no): ")
            if confirmar.lower() == "si":
                pedidos.pop(i)
                print("Pedido cancelado.")
            else:
                print("Cancelación abortada.")
            return
    print(f"No existe el pedido #{numero}")

def ver_todos():
    print("\n--- TODOS LOS PEDIDOS ---")
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return
    for pedido in pedidos:
        print(f"Pedido #{pedido['numero']} - {pedido['cliente']} - Total: ${pedido['total']:,}")

def generar_reporte():
    print("\n--- REPORTE DEL DÍA ---")
    if len(pedidos) == 0:
        print("No hay pedidos para reportar.")
        return
    print(f"\n1. Total de pedidos: {len(pedidos)}")
    total_recaudado = sum(pedido["total"] for pedido in pedidos)
    print(f"2. Total recaudado: ${total_recaudado:,}")
    promedio = total_recaudado / len(pedidos)
    print(f"3. Promedio por pedido: ${promedio:,.2f}")
    pedido_max = max(pedidos, key=lambda x: x["total"])
    print(f"4. Pedido más alto: #{pedido_max['numero']} - {pedido_max['cliente']} (${pedido_max['total']:,})")

while True:
    print("\n=== CAFETERÍA ===")
    print("1. Registrar pedido")
    print("2. Consultar pedido")
    print("3. Cancelar pedido")
    print("4. Ver todos los pedidos")
    print("5. Generar reporte")
    print("6. Salir")
    opcion = input("\nSeleccione opción: ").strip()
    if opcion == "1":
        registrar_pedido()
    elif opcion == "2":
        consultar_pedido()
    elif opcion == "3":
        cancelar_pedido()
    elif opcion == "4":
        ver_todos()
    elif opcion == "5":
        generar_reporte()
    elif opcion == "6":
        print("Hasta luego.")
        break
    else:
        print("Opción inválida.")
