Nempleado=(input("Ingrese su nombre: "))
salarioB= float(input("Ingrese su salario: "))

if salarioB == 1500:
    Vretencion = 0
    Sneto = salarioB
elif salarioB <= 3000:
    Vretencion = salarioB * 5 / 100
    Sneto = salarioB - Vretencion
else:
    Vretencion = salarioB * 8 / 100
    Sneto = salarioB - Vretencion
 
print("Nombre del empleado ", Nempleado)
print("Su salrio Base ", salarioB)
print("Valor de retencion", Vretencion)
print("Su salario neto es ", Sneto)
 


       

