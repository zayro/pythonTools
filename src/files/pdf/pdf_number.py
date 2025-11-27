#!/usr/bin/env python3
"""
Extrae números telefónicos de un PDF, normaliza (solo dígitos) y genera un CSV
con recuento ordenado por frecuencia.

Uso:
    python extract_phone_counts.py /ruta/al/archivo.pdf

Salida:
    - phone_counts.csv  (en la misma carpeta donde ejecutas el script)
    - phone_raw_matches.txt (lista de coincidencias crudas)
"""
import sys
import re
from collections import Counter
from PyPDF2 import PdfReader
import pandas as pd
import os


def numeros_telefonos(pdf_path):


 
    if not os.path.exists(pdf_path):
        print("Archivo no encontrado:", pdf_path)
        sys.exit(1)

    # Leer texto del PDF
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        try:
            txt = page.extract_text() or ""
            full_text += txt + "\n"
        except Exception as e:
            # seguir con las páginas restantes
            pass

    # Regex para capturar cadenas parecidas a teléfonos (paréntesis, +, espacios, guiones)
    pattern = re.compile(r'(\+?\d[\d\-\(\) \.]{5,}\d)')
    matches = pattern.findall(full_text)

    # Normalizar: quitar todo menos dígitos
    normalized = []
    for m in matches:
        digits = re.sub(r'\D+', '', m)
        # filtrar por longitud razonable (>=7 dígitos)
        if len(digits) >= 7:
            normalized.append(digits)

    counter = Counter(normalized)

    # Crear dataframe ordenado
    df = pd.DataFrame(counter.items(), columns=['phone','count']).sort_values(
        by=['count','phone'], ascending=[False, True]
    ).reset_index(drop=True)

    # Añadir longitud por si te interesa
    if not df.empty:
        df['length'] = df['phone'].str.len()

    out_csv = os.path.join(os.getcwd(), 'phone_counts.csv')
    df.to_csv(out_csv, index=False)
    with open(os.path.join(os.getcwd(), 'phone_raw_matches.txt'), 'w', encoding='utf-8') as f:
        for m in matches:
            f.write(m + "\n")

    print("Resultados guardados en:")
    print(" -", out_csv)
    print(" -", os.path.join(os.getcwd(), 'phone_raw_matches.txt'))
    print("\nTop 20 (por pantalla):")
    print(df.head(20).to_string(index=False))


numeros_telefonos("D:/GitHub/pythonTools/src/files/pdf/Abril_descifrado.pdf")