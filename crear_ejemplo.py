#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para crear un archivo Excel de ejemplo.
"""

import pandas as pd
import os

# Crear directorio de ejemplos si no existe
os.makedirs('ejemplos', exist_ok=True)

# Datos de ejemplo para la primera hoja (Empleados)
datos_empleados = {
    'ID': [1, 2, 3, 4, 5],
    'Nombre': ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Luis Rodríguez'],
    'Departamento': ['Ventas', 'Marketing', 'IT', 'RRHH', 'Finanzas'],
    'Salario': [45000, 52000, 60000, 48000, 55000],
    'Fecha de Contratación': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-05', '2022-02-28']
}

# Datos de ejemplo para la segunda hoja (Ventas)
datos_ventas = {
    'ID Producto': [101, 102, 103, 104, 105],
    'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Teclado'],
    'Precio': [1200.50, 800.75, 350.25, 250.00, 45.99],
    'Unidades Vendidas': [25, 40, 30, 15, 50],
    'Fecha de Venta': ['2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25', '2023-01-30']
}

# Crear DataFrames
df_empleados = pd.DataFrame(datos_empleados)
df_ventas = pd.DataFrame(datos_ventas)

# Crear un archivo Excel con múltiples hojas
ruta_excel = os.path.join('ejemplos', 'datos_ejemplo.xlsx')
with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
    df_empleados.to_excel(writer, sheet_name='Empleados', index=False)
    df_ventas.to_excel(writer, sheet_name='Ventas', index=False)

print(f"Archivo Excel de ejemplo creado en: {ruta_excel}") 