# Instrucciones Visuales: Excel a JSON

## Diagrama de Flujo

```
┌─────────────────┐
│  INICIO         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 1. Preparación  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ Abrir terminal y navegar al         │
│ directorio del script               │
│ $ cd ruta/al/directorio             │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ 2. Configurar entorno virtual       │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ Crear entorno virtual (una vez)     │
│ $ python3 -m venv venv              │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ Activar entorno virtual             │
│ $ source venv/bin/activate          │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ Instalar dependencias (una vez)     │
│ $ pip install -r requirements.txt   │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ 3. Usar el conversor                │
└────────────────┬────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
┌─────────────────┐ ┌─────────────────┐
│ Archivo único   │ │ Directorio      │
└────────┬────────┘ └────────┬────────┘
         │                   │
         ▼                   ▼
┌─────────────────┐ ┌─────────────────┐
│ $ python        │ │ $ python        │
│ excel_to_json.py│ │ excel_to_json.py│
│ archivo.xlsx    │ │ directorio/     │
│ -o salida.json  │ │ -o salida/      │
└────────┬────────┘ └────────┬────────┘
         │                   │
         │        ┌──────────┘
         │        │
         ▼        ▼
┌─────────────────────────────────────┐
│ 4. Finalizar                        │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────┐
│ Desactivar entorno virtual          │
│ $ deactivate                        │
└────────────────┬────────────────────┘
                 │
                 ▼
┌─────────────────┐
│     FIN         │
└─────────────────┘
```

## Resumen de Comandos

### Configuración (solo una vez)
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Uso Diario
```bash
# 1. Activar entorno virtual
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 2. Convertir Excel a JSON
python excel_to_json.py archivo.xlsx -o archivo.json

# 3. Desactivar entorno virtual cuando termines
deactivate
```

## Opciones Disponibles

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `-o, --output` | Archivo o directorio de salida | `-o datos.json` |
| `-s, --sheet` | Hoja específica a convertir | `-s "Ventas"` |
| `-r, --recursive` | Procesar subdirectorios | `-r` |

## Ejemplos Comunes

### Convertir un archivo Excel
```bash
python excel_to_json.py datos.xlsx -o datos.json
```

### Convertir una hoja específica
```bash
python excel_to_json.py datos.xlsx -o ventas.json -s "Ventas"
```

### Convertir todos los archivos en un directorio
```bash
python excel_to_json.py directorio_excel/ -o directorio_json/
```

### Convertir recursivamente
```bash
python excel_to_json.py directorio_excel/ -o directorio_json/ -r
``` 