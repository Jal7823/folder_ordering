from pathlib import Path
import os
import shutil


def obtener_rutas_descargas():
    ruta_descargas = Path(os.path.join(os.path.expanduser('~'), 'Descargas'))
    os.chdir(ruta_descargas)
    return list(ruta_descargas.glob('*'))


def mover_a_imagenes(archivo):
    ruta_imagenes = Path(os.path.join(os.path.expanduser('~'), 'Imágenes'))
    ruta_destino = ruta_imagenes / archivo.name
    shutil.copy(archivo, ruta_destino)
    archivo.unlink()  # Eliminar el archivo original después de copiar
    return ruta_destino


def mover_a_documentos(archivo):
    ruta_documentos = Path(os.path.join(os.path.expanduser('~'), 'Documentos/docs'))
    ruta_destino = ruta_documentos / archivo.name
    shutil.copy(archivo, ruta_destino)
    archivo.unlink()  # Eliminar el archivo original después de copiar
    return ruta_destino


def mover_a_csv(archivo):
    ruta_csv = Path(os.path.join(os.path.expanduser('~'), 'Documentos/excel'))
    ruta_destino = ruta_csv / archivo.name
    shutil.copy(archivo, ruta_destino)
    archivo.unlink()  # Eliminar el archivo original después de copiar
    return ruta_destino


if __name__ == "__main__":
    archivos_en_descargas = obtener_rutas_descargas()

    for archivo in archivos_en_descargas:
        extension = archivo.suffix
        print('extensión ==>', extension)

        if extension in {'.png', '.jpg', '.jpg_large', '.png_large'}:
            ruta_destino = mover_a_imagenes(archivo)
            print(f"Se movió '{archivo.name}' a '{ruta_destino}'")

        elif extension == '.pdf':
            ruta_destino = mover_a_documentos(archivo)
            print(f"Se movió '{archivo.name}' a '{ruta_destino}'")

        elif extension in {'.csv', '.xls'}:
            ruta_destino = mover_a_csv(archivo)
            print(f"Se movió '{archivo.name}' a '{ruta_destino}'")
