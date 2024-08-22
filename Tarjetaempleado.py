# Definir variables
nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_hora = float(input("Ingrese el salario básico por hora: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))

# Calcular horas extras
if horas_trabajadas > 48:
  horas_extras = horas_trabajadas - 48
else:
  horas_extras = 0

# Calcular pago por horas normales
pago_normal = horas_trabajadas * salario_hora

# Calcular pago por horas extras
pago_extras = horas_extras * (salario_hora * 3.5 / 100)

# Calcular salario bruto
salario_bruto = pago_normal + pago_extras

# Calcular salario neto (asumiendo deducción fija)
deduccion = 100  # Deducción fija (por ejemplo, seguro social)
salario_neto = salario_bruto - deduccion

# Imprimir resultados
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Salario neto: {salario_neto}")

 