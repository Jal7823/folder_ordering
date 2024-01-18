from pathlib import Path
import os

# Obtener el directorio de inicio del usuario actual
ruta_descargas = Path(os.path.join(os.path.expanduser('~'), 'Descargas'))
ruta_imagenes = Path(os.path.join(os.path.expanduser('~'), 'Imágenes'))
ruta_documentos = Path(os.path.join(os.path.expanduser('~'), 'Documentos/docs'))
ruta_csv = Path(os.path.join(os.path.expanduser('~'), 'Documentos/excel'))

# Cambiar el directorio de trabajo actual al directorio "Descargas"
os.chdir(ruta_descargas)

# Obtener una lista de rutas de todos los archivos en el directorio
archivos_en_descargas = list(ruta_descargas.glob('*'))

# Iterar sobre cada archivo en el directorio
for archivo in archivos_en_descargas:
    # Obtener la extensión del archivo
    extension = archivo.suffix
    print('extensión ==>', extension)

    match extension:
        # images
        case '.png':
            # Construir la ruta de destino
            ruta_destino = ruta_imagenes / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_imagenes}'")

        case '.jpg':
            # Construir la ruta de destino
            ruta_destino = ruta_imagenes / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_imagenes}'")

        case '.jpg_large':
            # Construir la ruta de destino
            ruta_destino = ruta_imagenes / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_imagenes}'")

        case '.png_large':
            # Construir la ruta de destino
            ruta_destino = ruta_imagenes / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_imagenes}'")
        # pdf
        case '.pdf':
            # Construir la ruta de destino
            ruta_destino = ruta_documentos / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_documentos}'")

        # csv
        case '.csv':
            # Construir la ruta de destino
            ruta_destino = ruta_csv / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_csv}'")

        case '.xls':
            # Construir la ruta de destino
            ruta_destino = ruta_csv / archivo.name
            # Mover el archivo
            os.rename(archivo, ruta_destino)
            print(f"Se movió '{archivo.name}' a '{ruta_csv}'")