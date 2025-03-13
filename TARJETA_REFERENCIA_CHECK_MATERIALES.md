# Tarjeta de Referencia: Check de Materiales a JSON

## Configuración Inicial

```bash
# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Comandos Básicos

| Tarea | Comando |
|-------|---------|
| **Conversión básica** | `python check_materiales_a_json.py archivo.xlsx -o salida.json` |
| **Hoja específica** | `python check_materiales_a_json.py archivo.xlsx -o salida.json -s "Inventario"` |
| **Con categorización** | `python check_materiales_a_json.py archivo.xlsx -o salida.json -c` |
| **Categoría personalizada** | `python check_materiales_a_json.py archivo.xlsx -o salida.json -c --categoria "Tipo"` |

## Opciones

| Opción | Descripción | Valor predeterminado |
|--------|-------------|----------------------|
| `-o, --output` | Archivo JSON de salida | Ninguno (consola) |
| `-s, --sheet` | Hoja a convertir | 0 (primera hoja) |
| `-c, --categorize` | Categorizar materiales | False |
| `--categoria` | Columna de categoría | "Categoría" |

## Ejemplos Prácticos

```bash
# Convertir inventario
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario.json -s "Inventario"

# Convertir con categorización
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/inventario_categorizado.json -s "Inventario" -c

# Convertir movimientos
python check_materiales_a_json.py ejemplos/check_materiales_ejemplo.xlsx -o ejemplos/movimientos.json -s "Movimientos"
```

## Solución de Problemas

- **Error pip**: Usar `pip3` en lugar de `pip`
- **Error entorno**: Asegurarse de activar el entorno virtual
- **Error columna**: Verificar que exista la columna "Categoría" o especificar el nombre correcto
- **Error archivo**: Verificar ruta, formato y permisos del archivo

## Recordatorio

```bash
# Activar entorno antes de usar
source venv/bin/activate

# Desactivar al terminar
deactivate
``` 