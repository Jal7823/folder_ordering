import pytest
from pathlib import Path
import shutil

# Importa las funciones desde tu código
from file_organizer import mover_a_imagenes, mover_a_documentos, mover_a_csv


def test_mover_a_imagenes(tmp_path):
    # Crea un archivo de prueba en el directorio temporal
    archivo_prueba = tmp_path / "archivo_test.jpg"
    archivo_prueba.touch()

    # Llama a la función que estamos probando
    resultado = mover_a_imagenes(archivo_prueba)

    # Comprueba que el archivo se ha movido correctamente a la carpeta de imágenes
    assert resultado == Path("~/Imágenes/archivo_test.jpg").expanduser()
    assert resultado.exists()


def test_mover_a_documentos(tmp_path):
    # Crea un archivo de prueba en el directorio temporal
    archivo_prueba = tmp_path / "archivo_test.pdf"
    archivo_prueba.touch()

    # Llama a la función que estamos probando
    resultado = mover_a_documentos(archivo_prueba)

    # Comprueba que el archivo se ha movido correctamente a la carpeta de documentos
    assert resultado == Path("~/Documentos/docs/archivo_test.pdf").expanduser()
    assert resultado.exists()


def test_mover_a_csv(tmp_path):
    # Crea un archivo de prueba en el directorio temporal
    archivo_prueba = tmp_path / "archivo_test.csv"
    archivo_prueba.touch()

    # Llama a la función que estamos probando
    resultado = mover_a_csv(archivo_prueba)

    # Comprueba que el archivo se ha movido correctamente a la carpeta de CSV
    assert resultado == Path("~/Documentos/excel/archivo_test.csv").expanduser()
    assert resultado.exists()
