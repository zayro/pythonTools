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


def numeros_telefonos(pdf_paths):
    """
    Extrae números telefónicos de uno o varios PDFs, normaliza y genera CSV.
    Genera un archivo CSV por cada PDF y uno consolidado.
    
    Args:
        pdf_paths: str (ruta única) o list (múltiples rutas)
    """
    
    # Convertir a lista si es una sola ruta
    if isinstance(pdf_paths, str):
        pdf_paths = [pdf_paths]
    
    full_text = ""
    pdf_data = {}  # Diccionario para almacenar datos por PDF
    
    # Procesar cada PDF
    for pdf_path in pdf_paths:
        if not os.path.exists(pdf_path):
            print(f"⚠️  Archivo no encontrado: {pdf_path}")
            continue
        
        print(f"📄 Procesando: {pdf_path}")
        pdf_text = ""
        
        try:
            reader = PdfReader(pdf_path)
            for page in reader.pages:
                try:
                    txt = page.extract_text() or ""
                    pdf_text += txt + "\n"
                except Exception as e:
                    pass
            
            full_text += pdf_text + "\n"
            pdf_data[pdf_path] = pdf_text
            
        except Exception as e:
            print(f"❌ Error al leer {pdf_path}: {e}")
            continue

    # Procesar cada PDF individualmente
    for pdf_path, pdf_text in pdf_data.items():
        # Regex para capturar cadenas parecidas a teléfonos
        pattern = re.compile(r'(\+?\d[\d\-\(\) \.]{5,}\d)')
        matches = pattern.findall(pdf_text)

        # Normalizar: quitar todo menos dígitos
        normalized = []
        for m in matches:
            digits = re.sub(r'\D+', '', m)
            if len(digits) >= 7:
                normalized.append(digits)

        counter = Counter(normalized)

        # Crear dataframe ordenado
        df = pd.DataFrame(counter.items(), columns=['phone','count']).sort_values(
            by=['count','phone'], ascending=[False, True]
        ).reset_index(drop=True)

        if not df.empty:
            df['length'] = df['phone'].str.len()
            df['total_minutos'] = df['count'] * 5

        # Guardar CSV individual por PDF
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        out_csv = os.path.join(os.getcwd(), f'phone_counts_{pdf_name}.csv')
        df.to_csv(out_csv, index=False)
        print(f"  ✅ {out_csv}")

    # Procesar consolidado (todos los PDFs)
    pattern = re.compile(r'(\+?\d[\d\-\(\) \.]{5,}\d)')
    matches = pattern.findall(full_text)

    normalized = []
    for m in matches:
        digits = re.sub(r'\D+', '', m)
        if len(digits) >= 7:
            normalized.append(digits)

    counter = Counter(normalized)

    df_consolidado = pd.DataFrame(counter.items(), columns=['phone','count']).sort_values(
        by=['count','phone'], ascending=[False, True]
    ).reset_index(drop=True)

    if not df_consolidado.empty:
        df_consolidado['length'] = df_consolidado['phone'].str.len()
        df_consolidado['total_minutos'] = df_consolidado['count'] * 5

    out_csv = os.path.join(os.getcwd(), 'phone_counts_CONSOLIDADO.csv')
    df_consolidado.to_csv(out_csv, index=False)
    with open(os.path.join(os.getcwd(), 'phone_raw_matches.txt'), 'w', encoding='utf-8') as f:
        for m in matches:
            f.write(m + "\n")

    print("\n✅ Resultados guardados en:")
    print(" -", out_csv)
    print(" -", os.path.join(os.getcwd(), 'phone_raw_matches.txt'))
    print("\nTop 20 (por pantalla):")
    print(df_consolidado.head(20).to_string(index=False))
 

# Uso: múltiples rutas
numeros_telefonos([
    "D:/GitHub/pythonTools/src/files/pdf/Abril_descifrado.pdf",
    "D:/GitHub/pythonTools/src/files/pdf/Mayo_descifrado.pdf",
    "D:/GitHub/pythonTools/src/files/pdf/Junio_descifrado.pdf",
    "D:/GitHub/pythonTools/src/files/pdf/Julio_descifrado.pdf",
    "D:/GitHub/pythonTools/src/files/pdf/Agosto_descifrado.pdf"
])
