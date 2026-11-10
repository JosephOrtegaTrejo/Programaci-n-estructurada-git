import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("Act_9/pacientes - pacientes (1).csv")

# a) Crea la columna imc = peso / estatura²
# (Verifica si en tu CSV las columnas se llaman 'peso' y 'estatura')
df['imc'] = df['peso_kg'] / (df['estatura_m'] ** 2)

# Datos y límites de categorización
bins = [0, 18.5, 25, 30, 100]
labels = ["Bajo peso", "Normal", "Sobrepeso", "Obesidad"]

# b) Clasifícala con pd.cut
df['categoria_imc'] = pd.cut(df['imc'], bins=bins, labels=labels, right=False)

# c) Cuenta pacientes por categoría y encuentra cuántos quedaron sin IMC
print("c) Conteo de pacientes por categoría:")
print(df['categoria_imc'].value_counts(dropna=False))

# Cantidad de pacientes sin IMC
sin_imc = df['imc'].isna().sum()
print(f"\nPacientes que quedaron sin IMC: {sin_imc}")
print("¿Por qué?: Quedaron sin IMC porque tenían un dato faltante (NaN) en la columna 'peso' o en 'estatura', o porque la estatura era 0.")