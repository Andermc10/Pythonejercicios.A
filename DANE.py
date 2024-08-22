Ah=0
Am=0
At=0
for p in range(5):
    sexo=(input("Ingrese su sexo "))
    edad = int(input("Ingrese su edad "))
    if edad >= 18:
        if sexo=="hombre":
            Ah=Ah+1
        if sexo=="mujer":
            Am=Am+1

At=Am+Ah
print("Total etrevistados",At)
print("Total HOMBRES",Ah)
print("Total Mujeres",Am)






