"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    import pandas as pd
    # Cargar el archivo TSV en un DataFrame
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Obtener la cantidad de filas
    return df.shape[0]
