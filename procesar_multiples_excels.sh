#!/bin/bash
# Script para procesar múltiples archivos Excel de check de materiales

# Configuración
DIRECTORIO_ENTRADA="./excels"
DIRECTORIO_SALIDA="./jsons"
HOJA="Inventario"
CATEGORIZAR=true  # true para categorizar, false para no categorizar

# Crear directorio de salida si no existe
mkdir -p "$DIRECTORIO_SALIDA"

# Activar entorno virtual
source venv/bin/activate

echo "Iniciando procesamiento de archivos Excel..."
echo "----------------------------------------"

# Procesar cada archivo Excel en el directorio de entrada
for archivo in "$DIRECTORIO_ENTRADA"/*.xlsx; do
    if [ -f "$archivo" ]; then
        # Obtener el nombre base del archivo sin extensión
        nombre=$(basename "$archivo" .xlsx)
        
        echo "Procesando: $nombre.xlsx"
        
        # Definir archivo de salida
        archivo_salida="$DIRECTORIO_SALIDA/${nombre}.json"
        
        # Comando base
        comando="python check_materiales_a_json.py \"$archivo\" -o \"$archivo_salida\""
        
        # Agregar opciones adicionales
        if [ ! -z "$HOJA" ]; then
            comando="$comando -s \"$HOJA\""
        fi
        
        if [ "$CATEGORIZAR" = true ]; then
            comando="$comando -c"
        fi
        
        # Ejecutar el comando
        echo "Ejecutando: $comando"
        eval $comando
        
        echo "Archivo guardado en: $archivo_salida"
        echo "----------------------------------------"
    fi
done

# Desactivar entorno virtual
deactivate

echo "Procesamiento completado."
echo "Se procesaron $(ls -1 "$DIRECTORIO_ENTRADA"/*.xlsx 2>/dev/null | wc -l) archivos Excel."
echo "Los archivos JSON se guardaron en: $DIRECTORIO_SALIDA" 