import os
import shutil

def replace_spaces_and_organize(folder_path: str):
    """
    Reemplaza los espacios en blanco en los nombres de todos los archivos dentro de una carpeta por guiones '-'.
    Luego, crea una carpeta con el texto después del primer '-' y mueve el archivo a esa carpeta.

    Args:
        folder_path (str): Ruta de la carpeta.
    """
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            new_filename = filename.replace(' ', '-')
            new_path = os.path.join(folder_path, new_filename)
            if old_path != new_path:
                os.rename(old_path, new_path)
                filename = new_filename  # actualizar el nombre

            # Organizar en carpeta según texto después del primer '-'
            if '-' in filename:
                folder_name = filename.split('-', 1)[1].split('.')[0]
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                target_path = os.path.join(target_folder, filename)
                shutil.move(os.path.join(folder_path, filename), target_path)
                
replace_spaces_and_organize('empresa')                