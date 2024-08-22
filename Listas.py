A = [5, 7, 9, 12, 15, 2]
Asumap = 0
Asumai=0

for i in range(len(A)):
    if i % 2 == 0:
        Asumap += A[i]
        print(f"El número {A[i]} es par")

    if A[i] %2 == 1:
        Asumai += A[i]
        print(f"El número {A[i]} es impar")


print(f"La suma total de los números pares es: {Asumap}")
print(f"La suma total de los números impares es: {Asumai}")
