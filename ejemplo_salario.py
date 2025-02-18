# se define el salario inicial
salario = 1500

# Mostrar salario inicial
print(f"Año 0: ${salario:.2f}")

# calcular y mostrar el salario cada año durante 6 años
for año in range(1, 7):
    salario += salario * 0.10  # Incremento del 10%
    print(f"Año {año}: ${salario:.2f}")

# Mostrar salario final
print(f"Salario final después de 6 años: ${salario:.2f}")
