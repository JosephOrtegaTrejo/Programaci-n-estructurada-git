import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("Act_9/pacientes - pacientes (1).csv")

# Eliminar posibles espacios en blanco en los nombres de las columnas
df.columns = df.columns.str.strip()

# a) Filtrar pacientes con fiebre (temp_c >= 38) Y taquicardia (fc_lpm > 100)
condicion = (df['temp_c'] >= 38) & (df['fc_lpm'] > 100)
pacientes_alerta = df[condicion]

# b) ¿Cuántos son? Muestra id, temp_c, fc_lpm y servicio
cantidad = len(pacientes_alerta)
print(f"b) Cantidad de pacientes con alerta clínica: {cantidad}\n")

print("Listado de pacientes con alerta (id, temp_c, fc_lpm, servicio):")
# Mostramos únicamente las columnas solicitadas
print(pacientes_alerta[['id', 'temp_c', 'fc_lpm', 'servicio']])

# c) ¿En qué servicios están? (Conteo por servicio)
print("\nc) Distribución de estos pacientes por servicio:")
print(pacientes_alerta['servicio'].value_counts())