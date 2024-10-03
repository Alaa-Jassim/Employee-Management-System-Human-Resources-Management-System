




import os, sys

def images_path_vacations_employee(*subdirs, name_image):
    """Access the Resources folder,
    then access the contents of the (images_vacations_employee folder)"""
    
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_path)

    ressources_path = os.path.join(project_root, 'resources', *subdirs)
    
    if not os.path.exists(os.path.join(ressources_path, name_image)):
        raise FileNotFoundError(f"The specified path is incorrect, please check it")
    return os.path.join(ressources_path, name_image)
