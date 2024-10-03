import os
import shutil


def get_resources_path():
    """Get the path to the resources directory."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    resources_path = os.path.join(base_path, 'resources')

    if os.path.exists(resources_path):
        return resources_path
    return None 

def get_appdata_dir(subfolder_name=None):
    """Get the user data directory based on the platform."""
    appdata_dir = os.getenv('APPDATA')  
    if not appdata_dir:
        raise EnvironmentError("متغير البيئة APPDATA غير محدد.")

    if subfolder_name:
        return os.path.join(appdata_dir, subfolder_name)
    return appdata_dir

def copy_resources_folder():
    """Copy the resources folder to the AppData directory."""
    source = get_resources_path()
    if source is None:
        return "Error: Resources folder not found."

    destination = get_appdata_dir('resources') 

    if not os.path.exists(destination):
        os.makedirs(destination)

    try:
        shutil.copytree(source, destination, dirs_exist_ok=True)
        return f"Copied resources from {source} to {destination}"
    except Exception as e:
        return f"Error: {e}"


def manager_Sqlite3(sub_dir, file_name):
    """ The function responsible for managing database files in the APPDATA folder """
    appdata_dir = os.getenv('APPDATA')
    path_resources = os.path.join(appdata_dir, 'resources', sub_dir, file_name)
    if os.path.exists(path_resources):
        return path_resources
    return f"Error in the full path of the database file, please check it: {path_resources}."


def manager_Images(sub_dir, file_name):
    """ The function responsible for managing the images used in the application """
    appdata_dir = os.getenv('APPDATA')
    path_resources_images = os.path.join(appdata_dir, 'resources', sub_dir, file_name)
    if os.path.exists(path_resources_images):
        return path_resources_images
    return f"Error in the full path of the Images please check it: {path_resources_images}."



