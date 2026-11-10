import pandas as pd

# Especificar la ruta completa con la carpeta Act_9
df = pd.read_csv("Act_9/pacientes - pacientes (1).csv")

# a) ¿Cuántos pacientes y cuántas columnas hay?
filas, columnas = df.shape
print(f"a) Hay {filas} pacientes (filas) y {columnas} columnas.")

# b) ¿Qué columnas tienen faltantes y cuántos?
faltantes = df.isna().sum()
faltantes_filtrados = faltantes[faltantes > 0]

print("\nb) Columnas con datos faltantes y su cantidad:")
if not faltantes_filtrados.empty:
    print(faltantes_filtrados)
else:
    print("   No hay columnas con datos faltantes.")

# c) ¿Qué tipo de dato tiene cada columna?
print("\nc) Tipo de dato por columna:")
print(df.dtypes)