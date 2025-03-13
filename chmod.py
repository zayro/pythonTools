import os

# Función para cambiar recursivamente los permisos
def cambiar_permisos_ruta(ruta, permisos):
    for root, dirs, files in os.walk(ruta):
        for d in dirs:
            os.chmod(os.path.join(root, d), permisos)
        for f in files:
            os.chmod(os.path.join(root, f), permisos)

# Ruta inicial y permisos a establecer (por ejemplo, 0o755 para lectura, escritura y ejecución para el propietario, lectura y ejecución para grupo y otros)
ruta_inicial = 'D:/Imagenes/NuevaCarpeta'
permisos = 0o755

# Llama a la función para cambiar los permisos
cambiar_permisos_ruta(ruta_inicial, permisos)