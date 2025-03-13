# Guía Completa: Conversión de Check de Materiales a JSON

Esta guía detallada explica cómo utilizar el script especializado para convertir archivos Excel de check de materiales a formato JSON.

## Índice

1. [Requisitos Previos](#requisitos-previos)
2. [Instalación](#instalación)
3. [Estructura del Archivo Excel](#estructura-del-archivo-excel)
4. [Uso del Script](#uso-del-script)
5. [Opciones Avanzadas](#opciones-avanzadas)
6. [Estructura del JSON Resultante](#estructura-del-json-resultante)
7. [Ejemplos Prácticos](#ejemplos-prácticos)
8. [Solución de Problemas](#solución-de-problemas)
9. [Preguntas Frecuentes](#preguntas-frecuentes)

## Requisitos Previos

- Python 3.6 o superior instalado
- Acceso a la terminal o línea de comandos
- Conocimientos básicos de línea de comandos

## Instalación

### 1. Configuración del Entorno Virtual

Es recomendable usar un entorno virtual para evitar conflictos con otras instalaciones de Python:

```bash
# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 2. Instalación de Dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Si encuentras el error "command not found: pip", intenta usar `pip3` en lugar de `pip`.

## Estructura del Archivo Excel

El script está diseñado para trabajar con archivos Excel que tengan la siguiente estructura:

### Formato Recomendado

- **Encabezados en la primera fila**: Cada columna debe tener un nombre claro
- **Datos organizados en filas**: Cada fila representa un material o ítem
- **Sin celdas combinadas**: Evita usar celdas combinadas para mejor compatibilidad
- **Sin filas o columnas ocultas**: Todas las filas y columnas deben ser visibles

### Columnas Típicas

- **ID**: Identificador único del material
- **Código**: Código o referencia del material
- **Descripción**: Nombre o descripción del material
- **Categoría**: Tipo o categoría del material (útil para la opción de categorización)
- **Unidad**: Unidad de medida (kg, m, pieza, etc.)
- **Cantidad Disponible**: Stock actual
- **Estado**: Estado del material (disponible, en uso, etc.)
- **Responsable**: Persona a cargo
- **Observaciones**: Notas adicionales

### Múltiples Hojas

El script puede procesar diferentes hojas del mismo archivo Excel. Comúnmente:
- **Inventario**: Lista actual de materiales
- **Movimientos**: Registro de entradas y salidas
- **Proveedores**: Información de proveedores
- **Ubicaciones**: Datos sobre ubicaciones de almacenamiento

## Uso del Script

### Paso 1: Preparación

Asegúrate de tener activado el entorno virtual:

```bash
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
```

### Paso 2: Conversión Básica

Para convertir un archivo Excel completo a JSON:

```bash
python check_materiales_a_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json
```

Ejemplo:
```bash
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/check_materiales.json
```

### Paso 3: Verificar el Resultado

Puedes verificar el archivo JSON resultante con:

```bash
# Ver las primeras líneas
head -20 ejemplos/check_materiales.json

# O abrir con un editor de texto
nano ejemplos/check_materiales.json
```

## Opciones Avanzadas

### Seleccionar una Hoja Específica

Si tu archivo Excel tiene múltiples hojas y deseas convertir una específica:

```bash
python check_materiales_a_json.py archivo.xlsx -o archivo.json -s "Inventario"
```

### Categorización de Materiales

Para agrupar los materiales por categoría (requiere una columna de categoría en el Excel):

```bash
python check_materiales_a_json.py archivo.xlsx -o archivo.json -c
```

Si la columna de categoría tiene un nombre diferente a "Categoría":

```bash
python check_materiales_a_json.py archivo.xlsx -o archivo.json -c --categoria "Tipo"
```

### Tabla de Opciones Disponibles

| Opción | Descripción | Valor por defecto | Ejemplo |
|--------|-------------|-------------------|---------|
| `-o, --output` | Archivo JSON de salida | Ninguno (muestra en consola) | `-o datos.json` |
| `-s, --sheet` | Nombre o índice de la hoja | 0 (primera hoja) | `-s "Inventario"` |
| `-c, --categorize` | Categorizar materiales | False | `-c` |
| `--categoria` | Nombre de la columna de categoría | "Categoría" | `--categoria "Tipo"` |

## Estructura del JSON Resultante

### Formato Básico (Sin Categorización)

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
      "Unidad": "Saco",
      "Cantidad Disponible": 120,
      "Estado": "Disponible"
    },
    // Más materiales...
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
        // Más propiedades...
      },
      // Más materiales...
    ],
    "Herramienta": [
      // Materiales de categoría Herramienta...
    ],
    // Más categorías...
  }
}
```

## Ejemplos Prácticos

### Ejemplo 1: Convertir Inventario Básico

```bash
# Activar entorno virtual
source venv/bin/activate

# Convertir la hoja "Inventario" a JSON
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario.json -s "Inventario"

# Ver el resultado
head -20 ejemplos/inventario.json
```

### Ejemplo 2: Convertir y Categorizar por Tipo de Material

```bash
# Convertir y categorizar por la columna "Categoría"
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario_categorizado.json -s "Inventario" -c

# Ver el resultado
head -30 ejemplos/inventario_categorizado.json
```

### Ejemplo 3: Convertir Registro de Movimientos

```bash
# Convertir la hoja "Movimientos" a JSON
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/movimientos.json -s "Movimientos"
```

### Ejemplo 4: Usar una Columna de Categoría Diferente

```bash
# Si la columna se llama "Tipo" en lugar de "Categoría"
python check_materiales_a_json.py archivo.xlsx -o archivo.json -c --categoria "Tipo"
```

## Solución de Problemas

### Error: "No se encuentra el comando pip"

**Solución**: Usa `pip3` en lugar de `pip` o asegúrate de que Python esté en tu PATH:

```bash
pip3 install -r requirements.txt
```

### Error: "externally-managed-environment"

**Solución**: Este error ocurre en Python 3.12+ en sistemas modernos. Asegúrate de estar usando un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "No se encuentra la columna de categoría"

**Solución**: Verifica que:
1. La columna de categoría exista en tu Excel
2. El nombre sea exactamente "Categoría" o especifica el nombre correcto con `--categoria`
3. No haya espacios adicionales en el nombre de la columna

### Error al Leer el Archivo Excel

**Solución**: Verifica que:
1. El archivo exista y la ruta sea correcta
2. El formato sea .xlsx o .xls
3. El archivo no esté dañado o protegido con contraseña
4. Tengas permisos de lectura para el archivo

## Preguntas Frecuentes

### ¿Puedo convertir varios archivos Excel a la vez?

No directamente con un solo comando, pero puedes crear un script bash o batch para procesar múltiples archivos:

```bash
#!/bin/bash
for archivo in directorio/*.xlsx; do
    nombre=$(basename "$archivo" .xlsx)
    python check_materiales_a_json.py "$archivo" -o "salida/${nombre}.json"
done
```

### ¿Cómo puedo personalizar el formato del JSON resultante?

Para personalizar el formato, necesitarías modificar el script `check_materiales_a_json.py`. La función principal que genera la estructura JSON es `check_materiales_a_json()`.

### ¿El script funciona con archivos Excel muy grandes?

Sí, pero el rendimiento dependerá de la memoria disponible en tu sistema. Para archivos muy grandes (más de 100,000 filas), considera dividir el archivo en partes más pequeñas.

### ¿Puedo usar el script en un servidor sin interfaz gráfica?

Sí, el script funciona completamente en línea de comandos y no requiere interfaz gráfica.

### ¿Cómo puedo programar la ejecución automática del script?

Puedes usar herramientas como cron (Linux/macOS) o el Programador de tareas (Windows) para ejecutar el script automáticamente:

```bash
# Ejemplo de entrada cron para ejecutar diariamente a las 2 AM
0 2 * * * cd /ruta/al/script && source venv/bin/activate && python check_materiales_a_json.py datos.xlsx -o datos.json
``` 