import numpy as np

# Datos proporcionados en la actividad
# Columnas: temp_c, fc_lpm, glucosa
datos = np.array([
    [36.5,  72,  95],
    [38.2, 104, 140],
    [37.0,  80,  88],
    [36.8,  65, 110],
    [39.1, 112, 125]
])

# a) y b) Escala cada columna al rango [0, 1] usando broadcasting (sin ningún for)
v_min = np.min(datos, axis=0)
v_max = np.max(datos, axis=0)

datos_normalizados = (datos - v_min) / (v_max - v_min)

print("Matriz normalizada [0, 1]:")
print(datos_normalizados)

# c) Verifica que cada columna tenga mínimo 0 y máximo 1
minimos = np.min(datos_normalizados, axis=0)
maximos = np.max(datos_normalizados, axis=0)

print("\nc) Verificación:")
print(f"   Mínimos por columna: {minimos}")
print(f"   Máximos por columna: {maximos}")