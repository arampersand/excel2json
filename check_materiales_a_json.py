#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para convertir un archivo Excel de check de materiales a formato JSON.
Este script está especializado para manejar la estructura típica de un
inventario o check de materiales.
"""

import os
import json
import argparse
import pandas as pd
from typing import Dict, List, Any, Union
from datetime import datetime


def check_materiales_a_json(excel_file: str, output_file: str = None, sheet_name: Union[str, int, None] = 0, 
                           categorize: bool = False, categoria_col: str = 'Categoría') -> Dict[str, Any]:
    """
    Convierte un archivo Excel de check de materiales a formato JSON.
    
    Args:
        excel_file: Ruta al archivo Excel de check de materiales
        output_file: Ruta donde guardar el archivo JSON (opcional)
        sheet_name: Nombre o índice de la hoja a convertir (por defecto: 0, primera hoja)
        categorize: Si se deben categorizar los materiales por tipo
        categoria_col: Nombre de la columna que contiene la categoría
        
    Returns:
        Diccionario con los datos convertidos
    """
    try:
        # Leer el archivo Excel
        print(f"Leyendo archivo Excel de check de materiales: {excel_file}")
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        # Limpiar datos: eliminar filas completamente vacías y columnas sin nombre
        df = df.dropna(how='all')
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        # Convertir DataFrame a diccionario
        materiales = df.to_dict(orient='records')
        
        # Crear estructura JSON con metadatos
        resultado = {
            "metadata": {
                "fecha_conversion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "archivo_origen": os.path.basename(excel_file),
                "hoja": sheet_name,
                "total_items": len(materiales)
            }
        }
        
        # Si se solicita categorización y existe la columna de categoría
        if categorize and categoria_col in df.columns:
            print(f"Categorizando materiales por: {categoria_col}")
            # Agrupar por categoría
            categorias = {}
            for material in materiales:
                categoria = material.get(categoria_col, "Sin categoría")
                if categoria not in categorias:
                    categorias[categoria] = []
                categorias[categoria].append(material)
            
            # Agregar estadísticas de categorías
            resultado["metadata"]["categorias"] = list(categorias.keys())
            resultado["metadata"]["items_por_categoria"] = {cat: len(items) for cat, items in categorias.items()}
            
            # Agregar materiales categorizados
            resultado["materiales_por_categoria"] = categorias
        else:
            # Agregar todos los materiales sin categorizar
            resultado["materiales"] = materiales
        
        # Guardar como JSON si se especificó un archivo de salida
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(resultado, f, ensure_ascii=False, indent=4)
            print(f"Archivo JSON guardado en: {output_file}")
        
        return resultado
    
    except Exception as e:
        print(f"Error al convertir Excel a JSON: {str(e)}")
        return {"error": str(e)}


def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(description='Convierte un archivo Excel de check de materiales a formato JSON')
    
    # Argumentos del script
    parser.add_argument('input', help='Archivo Excel de check de materiales a convertir')
    parser.add_argument('-o', '--output', help='Archivo JSON de salida')
    parser.add_argument('-s', '--sheet', default=0, help='Nombre o índice de la hoja (por defecto: 0)')
    parser.add_argument('-c', '--categorize', action='store_true', help='Categorizar materiales por tipo/categoría')
    parser.add_argument('--categoria', default='Categoría', help='Nombre de la columna de categoría (por defecto: "Categoría")')
    
    args = parser.parse_args()
    
    # Verificar si la entrada es un archivo
    if os.path.isfile(args.input):
        # Convertir el archivo
        check_materiales_a_json(args.input, args.output, args.sheet, args.categorize, args.categoria)
    else:
        print(f"El archivo {args.input} no existe.")


if __name__ == "__main__":
    main() 