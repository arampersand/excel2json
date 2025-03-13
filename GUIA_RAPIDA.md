# Guía Rápida: Conversor de Excel a JSON

Esta guía te ayudará a utilizar el script de conversión de Excel a JSON paso a paso.

## Requisitos Previos

- Python 3.6 o superior instalado
- Acceso a la terminal o línea de comandos

## Pasos para Usar el Conversor

### 1. Preparación del Entorno

1. **Abre una terminal** en tu sistema operativo:
   - En Windows: Busca "cmd" o "PowerShell" en el menú inicio
   - En macOS: Abre la aplicación Terminal
   - En Linux: Abre la terminal de tu distribución

2. **Navega hasta el directorio** donde se encuentra el script:
   ```bash
   cd ruta/al/directorio
   ```

### 2. Configuración del Entorno Virtual

1. **Crea un entorno virtual** (solo necesitas hacerlo una vez):
   ```bash
   python3 -m venv venv
   ```

2. **Activa el entorno virtual**:
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   
   Sabrás que está activado cuando veas `(venv)` al inicio de la línea de comandos.

3. **Instala las dependencias** (solo necesitas hacerlo una vez):
   ```bash
   pip install -r requirements.txt
   ```

### 3. Uso del Conversor

#### Caso 1: Convertir un solo archivo Excel

```bash
python excel_to_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json
```

Ejemplo:
```bash
python excel_to_json.py ejemplos/datos_ejemplo.xlsx -o ejemplos/resultado.json
```

#### Caso 2: Convertir una hoja específica

```bash
python excel_to_json.py ruta/al/archivo.xlsx -o ruta/al/archivo.json -s "Nombre de la Hoja"
```

Ejemplo:
```bash
python excel_to_json.py ejemplos/datos_ejemplo.xlsx -o ejemplos/ventas.json -s "Ventas"
```

#### Caso 3: Convertir todos los archivos Excel en un directorio

```bash
python excel_to_json.py ruta/al/directorio/ -o ruta/al/directorio_salida/
```

Ejemplo:
```bash
python excel_to_json.py ejemplos/ -o resultados/
```

#### Caso 4: Convertir recursivamente (incluyendo subdirectorios)

```bash
python excel_to_json.py ruta/al/directorio/ -o ruta/al/directorio_salida/ -r
```

### 4. Finalizar

Cuando hayas terminado, puedes desactivar el entorno virtual:

```bash
deactivate
```

## Ejemplos Prácticos

### Ejemplo 1: Convertir un archivo Excel básico

1. Activa el entorno virtual:
   ```bash
   source venv/bin/activate  # En macOS/Linux
   ```

2. Ejecuta el conversor:
   ```bash
   python excel_to_json.py ejemplos/datos_ejemplo.xlsx -o ejemplos/resultado.json
   ```

3. Verifica el resultado:
   ```bash
   cat ejemplos/resultado.json
   ```

### Ejemplo 2: Convertir solo la hoja "Ventas"

```bash
python excel_to_json.py ejemplos/datos_ejemplo.xlsx -o ejemplos/solo_ventas.json -s "Ventas"
```

## Solución de Problemas

### Error: "No se encuentra el comando pip"

Si ves este error, intenta usar `pip3` en lugar de `pip`:
```bash
pip3 install -r requirements.txt
```

### Error: "externally-managed-environment"

Este error ocurre en Python 3.12+ en sistemas modernos. Asegúrate de estar usando un entorno virtual como se describe en esta guía.

### Error: "No se puede encontrar el archivo"

Verifica que la ruta al archivo Excel sea correcta y que el archivo exista.

## Recordatorio

Siempre activa el entorno virtual antes de usar el script:
```bash
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate     # En Windows
``` 