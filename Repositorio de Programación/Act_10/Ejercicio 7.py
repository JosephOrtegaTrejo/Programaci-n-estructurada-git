import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("Act_9/pacientes - pacientes (1).csv")

# Limpiar nombres de columnas por si contienen espacios extra
df.columns = df.columns.str.strip()

# a), b) y c) Agrupar por servicio, calcular métricas, redondear y ordenar
resumen = (
    df.groupby("servicio")
    .agg(
        num_pacientes=("servicio", "count"),
        temp_promedio=("temp_c", "mean"),
        fc_promedio=("fc_lpm", "mean")
    )
    .round(1)
    .sort_values(by="fc_promedio", ascending=False)
)

# Mostrar el resultado final
print("Ejercicio 7 - Resumen por servicio:")
print(resumen)