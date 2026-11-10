import numpy as np

# Datos proporcionados en la actividad
sistolica = np.array([118, 135, 142, 110, 128, 155, 121])

# a) Calcula el promedio y la desviación estándar
promedio = np.mean(sistolica)
desviacion = np.std(sistolica)

print(f"a) Promedio: {promedio:.2f}")
print(f"   Desviación estándar: {desviacion:.2f}")

# Máscara booleana para lecturas >= 130 mmHg
mascara = sistolica >= 130

# b) Cuenta cuántas lecturas son >= 130 mmHg
conteo = np.sum(mascara)
print(f"b) Cantidad de lecturas >= 130 mmHg: {conteo}")

# c) Indica en qué posiciones están esas lecturas
posiciones = np.flatnonzero(mascara)
print(f"c) Posiciones (índices): {posiciones}")