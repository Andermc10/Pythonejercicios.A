consumos = []
dia = 1

print("Sistema para el seguimiento de consumo de agua")
print("Ingrese los litros consumidos por día. Escriba -1 para finaliza.\n")

while True:
    try:
        valor = float(input(f"Día {dia}: "))
        if valor == -1:
            break
        if valor <= 0:
            print("El valor debe ser mayor que cero.")
            continue
        consumos.append(valor)
        dia += 1
    except ValueError:
        print("Debe ingresar un número válido.")

if len(consumos) == 0:
    print("\nNo se registraron datos.")
else:
    total_dias = len(consumos)
    promedio = sum(consumos) / total_dias
    mayor = max(consumos)
    menor = min(consumos)
    ordenado = sorted(consumos)

    print("\nINNFORME DE CONSUMO")
    print(f"Días registrados: {total_dias}")
    print(f"Promedio de consumo: {promedio:.2f} litros")
    print(f"Día con mayor consumo: {consumos.index(mayor) + 1} ({mayor} litros)")
    print(f"Día con menor consumo: {consumos.index(menor) + 1} ({menor} litros)")
    print("\nListado en orden ascendente:")
    for i, valor in enumerate(ordenado, start=1):
        print(f"{i}. {valor} litros")
