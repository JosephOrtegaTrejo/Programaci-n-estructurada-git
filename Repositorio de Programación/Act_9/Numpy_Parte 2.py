import numpy as np

# Matriz de datos (filas: pacientes, columnas: días 1, 2 y 3)
glucosa = np.array([
    [ 95, 102,  99],
    [140, 155, 148],
    [ 88,  91,  85],
    [110, 118, 125]
])

# a) Promedio de glucosa por paciente (por filas -> axis=1)
promedio_pacientes = np.mean(glucosa, axis=1)
print("a) Promedio por paciente:")
for i, prom in enumerate(promedio_pacientes, start=1):
    print(f"   Paciente {i}: {prom:.2f} mg/dL")

# b) Promedio por día (por columnas -> axis=0) y día con el promedio más alto
promedio_dias = np.mean(glucosa, axis=0)
dia_mas_alto = np.argmax(promedio_dias) + 1  # Sumamos 1 para indicar el número de día (1, 2 o 3)

print("\nb) Promedio por día:")
for i, prom in enumerate(promedio_dias, start=1):
    print(f"   Día {i}: {prom:.2f} mg/dL")
print(f"   El día con el promedio más alto fue el Día {dia_mas_alto}")

# c) ¿Qué paciente y qué día tuvieron el valor máximo?
pos_plana = np.argmax(glucosa)
paciente_idx, dia_idx = np.unravel_index(pos_plana, glucosa.shape)

print(f"\nc) El valor máximo ({glucosa[paciente_idx, dia_idx]} mg/dL) pertenece a:")
print(f"   Paciente: {paciente_idx + 1}")
print(f"   Día: {dia_idx + 1}")