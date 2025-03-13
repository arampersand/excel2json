# Conversor de Excel a JSON

Este script de Python permite convertir archivos Excel (.xlsx, .xls) a formato JSON de manera sencilla.

## Características

- Convierte un solo archivo Excel a JSON
- Procesa todos los archivos Excel en un directorio
- Opción para procesar subdirectorios recursivamente
- Permite especificar la hoja de cálculo a convertir
- Soporte para caracteres Unicode (acentos, ñ, etc.)

## Requisitos

```
pandas>=1.3.0
openpyxl>=3.0.0
```

## Instalación

### Opción 1: Usando un entorno virtual (recomendado)

En sistemas macOS modernos y algunos sistemas Linux, se recomienda usar un entorno virtual:

1. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ```

2. Activa el entorno virtual:
   ```bash
   # En macOS/Linux
   source venv/bin/activate
   
   # En Windows
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Para desactivar el entorno virtual cuando termines:
   ```bash
   deactivate
   ```

### Opción 2: Instalación global (sistemas antiguos)

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   # o
   pip3 install -r requirements.txt
   ```

## Uso

Asegúrate de tener el entorno virtual activado antes de ejecutar el script:

```bash
source venv/bin/activate  # En macOS/Linux
```

### Convertir un solo archivo Excel

```bash
python excel_to_json.py archivo.xlsx -o datos.json
```

### Convertir un archivo Excel especificando la hoja

```bash
python excel_to_json.py archivo.xlsx -o datos.json -s "Hoja2"
```

### Convertir todos los archivos Excel en un directorio

```bash
python excel_to_json.py directorio_excel/ -o directorio_json/
```

### Convertir recursivamente todos los archivos Excel en un directorio y subdirectorios

```bash
python excel_to_json.py directorio_excel/ -o directorio_json/ -r
```

## Opciones

- `input`: Archivo Excel o directorio a convertir (obligatorio)
- `-o, --output`: Archivo JSON o directorio de salida (opcional)
- `-s, --sheet`: Nombre o índice de la hoja a convertir (por defecto: 0, primera hoja)
- `-r, --recursive`: Procesar subdirectorios recursivamente

## Ejemplos de uso

### Ejemplo 1: Convertir un archivo Excel a JSON

```bash
python excel_to_json.py datos.xlsx -o datos.json
```

### Ejemplo 2: Convertir todos los archivos Excel en un directorio

```bash
python excel_to_json.py ./excels/ -o ./jsons/
```

### Ejemplo 3: Convertir un archivo Excel especificando una hoja por nombre

```bash
python excel_to_json.py ventas.xlsx -o ventas.json -s "Ventas 2023"
```

## Solución de problemas

### Error: "zsh: command not found: pip"
Si encuentras este error, intenta usar `pip3` en lugar de `pip`, o asegúrate de estar usando un entorno virtual como se describe en la sección de instalación.

### Error: "externally-managed-environment"
Este error ocurre en Python 3.12+ en sistemas que implementan PEP 668. La solución es usar un entorno virtual como se describe en la sección de instalación.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. 