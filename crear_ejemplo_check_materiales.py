#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para crear un archivo Excel de ejemplo de check de materiales.
"""

import pandas as pd
import os
from datetime import datetime, timedelta

# Crear directorio de ejemplos si no existe
os.makedirs('ejemplos', exist_ok=True)

# Fecha actual para el check
fecha_check = datetime.now()

# Datos de ejemplo para el check de materiales
datos_materiales = {
    'ID': list(range(1, 16)),
    'Código': ['MAT-001', 'MAT-002', 'MAT-003', 'MAT-004', 'MAT-005', 
               'HER-001', 'HER-002', 'HER-003', 'EQP-001', 'EQP-002', 
               'EQP-003', 'INS-001', 'INS-002', 'INS-003', 'INS-004'],
    'Descripción': [
        'Cemento Portland', 'Arena fina', 'Grava', 'Varilla de acero 3/8"', 'Alambre recocido',
        'Martillo', 'Taladro eléctrico', 'Sierra circular', 'Mezcladora de concreto', 'Generador eléctrico',
        'Andamio metálico', 'Casco de seguridad', 'Guantes de trabajo', 'Gafas protectoras', 'Chaleco reflectante'
    ],
    'Categoría': [
        'Material', 'Material', 'Material', 'Material', 'Material',
        'Herramienta', 'Herramienta', 'Herramienta', 'Equipo', 'Equipo',
        'Equipo', 'Seguridad', 'Seguridad', 'Seguridad', 'Seguridad'
    ],
    'Unidad': [
        'Saco', 'M³', 'M³', 'Varilla', 'Kg',
        'Pieza', 'Pieza', 'Pieza', 'Unidad', 'Unidad',
        'Sección', 'Pieza', 'Par', 'Pieza', 'Pieza'
    ],
    'Cantidad Disponible': [
        120, 15, 10, 500, 50,
        8, 3, 2, 1, 1,
        4, 25, 30, 20, 15
    ],
    'Cantidad Mínima': [
        20, 5, 3, 100, 10,
        2, 1, 1, 1, 1,
        2, 10, 10, 10, 5
    ],
    'Estado': [
        'Disponible', 'Disponible', 'Disponible', 'Disponible', 'Disponible',
        'En uso', 'Disponible', 'En reparación', 'Disponible', 'En uso',
        'Disponible', 'Disponible', 'Disponible', 'Disponible', 'Disponible'
    ],
    'Última Revisión': [
        (fecha_check - timedelta(days=i*3)).strftime('%Y-%m-%d') for i in range(15)
    ],
    'Responsable': [
        'Juan Pérez', 'Juan Pérez', 'Juan Pérez', 'María García', 'María García',
        'Carlos López', 'Carlos López', 'Carlos López', 'Ana Martínez', 'Ana Martínez',
        'Luis Rodríguez', 'Luis Rodríguez', 'Luis Rodríguez', 'Pedro Sánchez', 'Pedro Sánchez'
    ],
    'Observaciones': [
        '', '', 'Solicitar más unidades', '', '',
        'Requiere mantenimiento', '', 'Enviar a reparación', '', 'Reservado para proyecto A',
        '', '', 'Solicitar reposición', '', 'Nuevos en almacén'
    ]
}

# Crear DataFrame
df_materiales = pd.DataFrame(datos_materiales)

# Crear un segundo DataFrame para otra hoja (Movimientos)
datos_movimientos = {
    'ID Movimiento': list(range(1, 11)),
    'Fecha': [(fecha_check - timedelta(days=i*2)).strftime('%Y-%m-%d') for i in range(10)],
    'Código Material': ['MAT-001', 'MAT-002', 'HER-001', 'MAT-003', 'EQP-001', 
                        'INS-001', 'MAT-004', 'HER-002', 'INS-002', 'MAT-001'],
    'Tipo Movimiento': ['Entrada', 'Entrada', 'Salida', 'Entrada', 'Salida', 
                         'Salida', 'Entrada', 'Salida', 'Entrada', 'Salida'],
    'Cantidad': [50, 5, 1, 3, 1, 5, 100, 1, 10, 20],
    'Proyecto': ['Edificio Central', 'Edificio Central', 'Casa Modelo', 'Edificio Central', 'Casa Modelo',
                 'Edificio Central', 'Edificio Central', 'Oficinas Norte', 'Oficinas Norte', 'Casa Modelo'],
    'Responsable': ['Juan Pérez', 'Juan Pérez', 'Carlos López', 'María García', 'Ana Martínez',
                    'Luis Rodríguez', 'María García', 'Carlos López', 'Pedro Sánchez', 'Juan Pérez']
}

df_movimientos = pd.DataFrame(datos_movimientos)

# Crear un archivo Excel con múltiples hojas
ruta_excel = os.path.join('ejemplos', 'check_materiales_ejemplo.xlsx')
with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
    df_materiales.to_excel(writer, sheet_name='Inventario', index=False)
    df_movimientos.to_excel(writer, sheet_name='Movimientos', index=False)

print(f"Archivo Excel de ejemplo de check de materiales creado en: {ruta_excel}") 