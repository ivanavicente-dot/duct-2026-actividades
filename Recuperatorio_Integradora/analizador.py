import string

import matplotlib.pyplot as plt


def leer_archivo(ruta):
    """
    Lee un archivo de texto y devuelve su contenido.

    Parametros:
        ruta (str): ruta al archivo de texto a leer

    Retorna:
        str: el contenido del archivo, o None si el archivo no existe
    """
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{ruta}'")
        return None


def tokenizar(texto):
    """
    Convierte el texto a minusculas, quita los signos de puntuacion
    y lo separa en una lista de palabras (tokens).

    Parametros:
        texto (str): texto crudo a procesar

    Retorna:
        list[str]: lista de tokens limpios
    """
    texto = texto.lower()
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    return texto.split()


def contar_frecuencias(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parametros:
        texto (str): el texto a analizar

    Retorna:
        dict: pares {palabra: frecuencia}
    """
    palabras = tokenizar(texto)
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def graficar(frecuencias, top_n=10):
    """
    Genera y guarda un grafico de barras horizontales con las top_n
    palabras mas frecuentes.

    Parametros:
        frecuencias (dict): pares {palabra: frecuencia}
        top_n (int): cantidad de palabras a graficar

    Retorna:
        None (genera y guarda el grafico)
    """
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:top_n]

    palabras = [palabra for palabra, frecuencia in top10]
    valores = [frecuencia for palabra, frecuencia in top10]

    plt.figure(figsize=(10, 6))
    plt.barh(palabras[::-1], valores[::-1], color="steelblue")
    plt.title(f"Top {top_n} palabras mas frecuentes")
    plt.xlabel("Frecuencia")
    plt.tight_layout()
    plt.savefig("grafico_frecuencias.png", dpi=150, bbox_inches="tight")
    plt.show()


def main():
    texto = leer_archivo("texto_integradora.txt")
    if texto is None:
        return

    frecuencias = contar_frecuencias(texto)

    print(f"Cantidad de palabras totales: {sum(frecuencias.values())}")
    print(f"Cantidad de palabras distintas: {len(frecuencias)}")
    print("\nLas 10 palabras mas frecuentes:")
    top10 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:10]
    for palabra, frecuencia in top10:
        print(f"  {palabra}: {frecuencia}")

    graficar(frecuencias)


if __name__ == "__main__":
    main()
