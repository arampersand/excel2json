#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para convertir archivos Excel a formato JSON.
"""

import os
import json
import argparse
import pandas as pd
from typing import Dict, List, Any, Union


def excel_to_json(excel_file: str, output_file: str = None, sheet_name: Union[str, int, None] = 0) -> Dict[str, Any]:
    """
    Convierte un archivo Excel a formato JSON.
    
    Args:
        excel_file: Ruta al archivo Excel
        output_file: Ruta donde guardar el archivo JSON (opcional)
        sheet_name: Nombre o índice de la hoja a convertir (por defecto: 0, primera hoja)
        
    Returns:
        Diccionario con los datos convertidos
    """
    try:
        # Leer el archivo Excel
        print(f"Leyendo archivo Excel: {excel_file}")
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        # Convertir DataFrame a diccionario
        data = df.to_dict(orient='records')
        
        # Guardar como JSON si se especificó un archivo de salida
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Archivo JSON guardado en: {output_file}")
        
        return data
    
    except Exception as e:
        print(f"Error al convertir Excel a JSON: {str(e)}")
        return {}


def process_directory(directory: str, output_dir: str = None, recursive: bool = False) -> None:
    """
    Procesa todos los archivos Excel en un directorio.
    
    Args:
        directory: Directorio a procesar
        output_dir: Directorio donde guardar los archivos JSON
        recursive: Si se deben procesar subdirectorios
    """
    if not os.path.exists(directory):
        print(f"El directorio {directory} no existe.")
        return
    
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Si es un directorio y recursive es True, procesar recursivamente
        if os.path.isdir(item_path) and recursive:
            sub_output_dir = os.path.join(output_dir, item) if output_dir else None
            process_directory(item_path, sub_output_dir, recursive)
        
        # Si es un archivo Excel, convertirlo
        elif item.endswith(('.xlsx', '.xls')):
            if output_dir:
                output_file = os.path.join(output_dir, f"{os.path.splitext(item)[0]}.json")
            else:
                output_file = os.path.join(directory, f"{os.path.splitext(item)[0]}.json")
            
            excel_to_json(item_path, output_file)


def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(description='Convierte archivos Excel a formato JSON')
    
    # Argumentos del script
    parser.add_argument('input', help='Archivo Excel o directorio a convertir')
    parser.add_argument('-o', '--output', help='Archivo JSON o directorio de salida')
    parser.add_argument('-s', '--sheet', default=0, help='Nombre o índice de la hoja (por defecto: 0)')
    parser.add_argument('-r', '--recursive', action='store_true', help='Procesar subdirectorios recursivamente')
    
    args = parser.parse_args()
    
    # Verificar si la entrada es un archivo o directorio
    if os.path.isfile(args.input):
        # Convertir un solo archivo
        excel_to_json(args.input, args.output, args.sheet)
    elif os.path.isdir(args.input):
        # Convertir todos los archivos en un directorio
        process_directory(args.input, args.output, args.recursive)
    else:
        print(f"La entrada {args.input} no existe.")


if __name__ == "__main__":
    main() 