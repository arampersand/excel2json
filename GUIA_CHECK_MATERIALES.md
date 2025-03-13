# Guía: Conversión de Check de Materiales a JSON

Esta guía explica cómo utilizar el script especializado para convertir archivos Excel de check de materiales a formato JSON.

## Requisitos Previos

- Python 3.6 o superior instalado
- Entorno virtual configurado (ver instrucciones generales)
- Dependencias instaladas (pandas, openpyxl)

## Estructura del Archivo Excel

El script está diseñado para trabajar con archivos Excel que tengan la siguiente estructura:

- Columnas con nombres claros (sin columnas sin nombre)
- Datos organizados en filas, donde cada fila representa un material
- Opcionalmente, una columna llamada "Categoría" (o similar) para agrupar los materiales

Ejemplo de columnas típicas:
- ID
- Código
- Descripción
- Categoría
- Unidad
- Cantidad Disponible
- Estado
- Responsable
- Observaciones

## Pasos para la Conversión

### 1. Preparación

Asegúrate de tener activado el entorno virtual:

```bash
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

### 2. Conversión Básica

Para convertir un archivo Excel de check de materiales a JSON:

```bash
python check_materiales_a_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json
```

Ejemplo:
```bash
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/check_materiales.json
```

### 3. Conversión con Categorización

Si tu archivo Excel tiene una columna de categoría y deseas agrupar los materiales por categoría:

```bash
python check_materiales_a_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json -c
```

Si la columna de categoría tiene un nombre diferente a "Categoría":

```bash
python check_materiales_a_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json -c --categoria "Tipo"
```

### 4. Seleccionar una Hoja Específica

Si tu archivo Excel tiene múltiples hojas y deseas convertir una específica:

```bash
python check_materiales_a_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json -s "Inventario"
```

## Estructura del JSON Resultante

### Formato Básico

```json
{
  "metadata": {
    "fecha_conversion": "2023-05-15 10:30:45",
    "archivo_origen": "check_materiales.xlsx",
    "hoja": "Inventario",
    "total_items": 15
  },
  "materiales": [
    {
      "ID": 1,
      "Código": "MAT-001",
      "Descripción": "Cemento Portland",
      "Categoría": "Material",
      ...
    },
    ...
  ]
}
```

### Formato con Categorización

```json
{
  "metadata": {
    "fecha_conversion": "2023-05-15 10:30:45",
    "archivo_origen": "check_materiales.xlsx",
    "hoja": "Inventario",
    "total_items": 15,
    "categorias": ["Material", "Herramienta", "Equipo", "Seguridad"],
    "items_por_categoria": {
      "Material": 5,
      "Herramienta": 3,
      "Equipo": 3,
      "Seguridad": 4
    }
  },
  "materiales_por_categoria": {
    "Material": [
      {
        "ID": 1,
        "Código": "MAT-001",
        "Descripción": "Cemento Portland",
        ...
      },
      ...
    ],
    "Herramienta": [
      ...
    ],
    ...
  }
}
```

## Opciones Disponibles

| Opción | Descripción |
|--------|-------------|
| `-o, --output` | Archivo JSON de salida |
| `-s, --sheet` | Nombre o índice de la hoja a convertir |
| `-c, --categorize` | Categorizar materiales por tipo/categoría |
| `--categoria` | Nombre de la columna de categoría (por defecto: "Categoría") |

## Ejemplos de Uso

### Ejemplo 1: Convertir inventario básico

```bash
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario.json -s "Inventario"
```

### Ejemplo 2: Convertir y categorizar

```bash
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario_categorizado.json -s "Inventario" -c
```

### Ejemplo 3: Convertir movimientos

```bash
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/movimientos.json -s "Movimientos"
```

## Solución de Problemas

### Error: "No se encuentra la columna de categoría"

Si recibes este mensaje al usar la opción `-c`, verifica:
1. Que la columna de categoría exista en tu Excel
2. Que el nombre sea exactamente "Categoría" o especifica el nombre correcto con `--categoria`

### Error al leer el archivo Excel

Verifica que:
1. El archivo exista y la ruta sea correcta
2. El formato sea .xlsx o .xls
3. El archivo no esté dañado o protegido con contraseña 