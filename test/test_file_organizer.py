from pathlib import Path
import os
import shutil


def mover_a_imagenes(archivo):
    ruta_imagenes = Path("Imágenes")
    ruta_destino = ruta_imagenes / archivo.name
    ruta_imagenes.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe
    shutil.move(archivo, ruta_destino)
    return ruta_destino


def mover_a_documentos(archivo):
    ruta_documentos = Path("Documentos/docs")
    ruta_destino = ruta_documentos / archivo.name
    ruta_documentos.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe
    shutil.move(archivo, ruta_destino)
    return ruta_destino


def mover_a_csv(archivo):
    ruta_csv = Path("Documentos/excel")
    ruta_destino = ruta_csv / archivo.name
    ruta_csv.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe
    shutil.move(archivo, ruta_destino)
    return ruta_destino


def test_mover_a_imagenes(tmp_path):
    archivo_prueba = tmp_path / "archivo_test.jpg"
    archivo_prueba.touch()

    # Construir rutas relativas a partir del directorio actual
    ruta_imagenes = Path("Imágenes")
    ruta_destino = ruta_imagenes / archivo_prueba.name

    # Llama a la función que estamos probando
    resultado = mover_a_imagenes(archivo_prueba)

    # Verifica que la ruta de destino sea la esperada
    assert resultado == ruta_destino


def test_mover_a_documentos(tmp_path):
    archivo_prueba = tmp_path / "archivo_test.pdf"
    archivo_prueba.touch()

    # Construir rutas relativas a partir del directorio actual
    ruta_documentos = Path("Documentos/docs")
    ruta_destino = ruta_documentos / archivo_prueba.name

    # Llama a la función que estamos probando
    resultado = mover_a_documentos(archivo_prueba)

    # Verifica que la ruta de destino sea la esperada
    assert resultado == ruta_destino


def test_mover_a_csv(tmp_path):
    archivo_prueba = tmp_path / "archivo_test.csv"
    archivo_prueba.touch()

    # Construir rutas relativas a partir del directorio actual
    ruta_csv = Path("Documentos/excel")
    ruta_destino = ruta_csv / archivo_prueba.name

    # Llama a la función que estamos probando
    resultado = mover_a_csv(archivo_prueba)

    # Verifica que la ruta de destino sea la esperada
    assert resultado == ruta_destino
