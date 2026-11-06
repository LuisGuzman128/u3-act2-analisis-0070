# importar librerias
import pandas as pd
import numpy as np

print("Analisis de datos clientes Axel Guzman NC 0070")

clientes = {
    "Cliente": ["User1", "User2", "User3", "User4", "User5", "User6"],
    "Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
    "Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
    "Cancela_Servicio": [True, False, False, True, False, True]
}

df = pd.DataFrame(clientes)
print(df)

print("-+-+-+-+ Agrupar por una sola columna cliente -+-+-+-+")
agrupado = df.groupby('Cliente')
print(agrupado)

print("-+-+-+-+ por agregacion -+-+-+-+")
# antiguedad promedio por cliente
print(agrupado['Antiguedad_Meses'].mean())

print("-+-+-+-+ Antiguedad maxima -+-+-+-+")
# Antiguedad maxima en cada cliente
print(agrupado['Antiguedad_Meses'].max())