#!/usr/bin/env python3
import sys
import argparse
import pikepdf

def remove_password(input_path: str, output_path: str, password: str):
    try:
        # Abrir el PDF cifrado con la contraseña
        with pikepdf.open(input_path, password=password) as pdf:
            # Guardar sin cifrado (por defecto pikepdf no aplica cifrado al guardar)
            pdf.save(output_path)
        print(f"[OK] PDF sin contraseña guardado en: {output_path}")
    except pikepdf.PasswordError:
        print("[ERROR] Contraseña incorrecta o el PDF no está cifrado con la contraseña proporcionada.")
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {input_path}")
    except Exception as e:
        print(f"[ERROR] Ocurrió un error: {e}")


# Ejemplo de uso correcto:
input_pdf = "D:/GitHub/pythonTools/src/files/pdf/Julio_cifrado.pdf"  # Reemplaza con la ruta correcta
output_pdf = "D:/GitHub/pythonTools/src/files/pdf/Julio_descifrado.pdf"
password = "1098697572"  # Reemplaza con la contraseña correcta

remove_password(input_pdf, output_pdf, password)