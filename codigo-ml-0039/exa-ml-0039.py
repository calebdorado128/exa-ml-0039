import sys
import os
import pandas as pd

# Permitir importar dicc-0777.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0039')))
import dicc_0039

print("Caleb Dorado Machine Learning pandas, NC = 0039")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Eliseo Nava Machine Learning pandas, NC 0777"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0039.datos_deportes)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio)
registrar("3. Estadísticas Generales de la Columna 'Duracion_min'", df['Duracion_min'].describe())

# 4. Ordenar Ascendente por Duracion_min
df_asc_precio = df.sort_values(by="Duracion_min", ascending=True)
registrar("4. Ordenar Ascendente por Precio", df_asc_precio)

# 5. Ordenar Descendente por Jugadores
df_desc_stock = df.sort_values(by="Jugadores", ascending=False)
registrar("5. Ordenar Descendente por Jugadores", df_desc_stock)

# 7. Guardar el archivo resultados-ml-0777.md dentro de resultados-0777
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0777'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0777.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Caleb Dorado Machine Learning pandas, NC = 0039")
