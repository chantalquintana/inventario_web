import os

# Carpeta donde están tus imágenes
IMAGES_DIR = "imagenes"

# Obtener la ruta completa
base_path = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(base_path, IMAGES_DIR)

# Renombrar cada archivo
for filename in os.listdir(images_path):
    old_path = os.path.join(images_path, filename)
    if os.path.isfile(old_path):
        # Reemplaza espacios por guiones bajos y quita %20 (si existe)
        new_name = filename.replace(" ", "_").replace("%20", "_")
        # Opcional: convertir a minúsculas para evitar problemas
        # new_name = new_name.lower()
        new_path = os.path.join(images_path, new_name)
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"{filename} -> {new_name}")

print("Renombrado temporal completado ✅")
