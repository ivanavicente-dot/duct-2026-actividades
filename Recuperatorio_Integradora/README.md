# Mi analizador de frecuencias — versión final

Script en Python que lee el archivo `texto_integradora.txt`, lo separa en palabras (en minúsculas y sin signos de puntuación), cuenta cuántas veces aparece cada una (usando un diccionario) y genera un gráfico de barras con las 10 palabras más frecuentes, que se guarda como `grafico_frecuencias.png`. Si el archivo de texto no existe, muestra un mensaje de error en lugar de interrumpirse.

**Requisitos:** Python 3 y las bibliotecas `matplotlib` (para el gráfico) y `pytest` (para las pruebas).

**Instalación:** `python -m pip install matplotlib pytest`

**Uso:** desde la carpeta del proyecto, ejecutar `python analizador.py` para el análisis y el gráfico, y `python -m pytest` para correr las pruebas de `test_analizador.py`.
