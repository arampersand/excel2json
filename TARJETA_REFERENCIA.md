# Tarjeta de Referencia Rápida: Excel a JSON

## Configuración Inicial

```
1. Crear entorno virtual:
   python3 -m venv venv

2. Activar entorno:
   source venv/bin/activate  (macOS/Linux)
   venv\Scripts\activate     (Windows)

3. Instalar dependencias:
   pip install -r requirements.txt
```

## Comandos Básicos

| Tarea | Comando |
|-------|---------|
| **Archivo único** | `python excel_to_json.py archivo.xlsx -o salida.json` |
| **Hoja específica** | `python excel_to_json.py archivo.xlsx -o salida.json -s "Hoja1"` |
| **Directorio** | `python excel_to_json.py directorio/ -o salida/` |
| **Recursivo** | `python excel_to_json.py directorio/ -o salida/ -r` |

## Opciones

| Opción | Descripción |
|--------|-------------|
| `-o, --output` | Archivo/directorio de salida |
| `-s, --sheet` | Hoja específica (nombre o índice) |
| `-r, --recursive` | Procesar subdirectorios |

## Solución de Problemas

- **Error pip**: Usar `pip3` en lugar de `pip`
- **Error entorno**: Asegurarse de activar el entorno virtual
- **Error archivo**: Verificar que la ruta sea correcta

## Recordatorio

```
# Activar entorno antes de usar
source venv/bin/activate

# Desactivar al terminar
deactivate
``` 