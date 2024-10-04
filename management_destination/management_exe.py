import os
import shutil
import filecmp

def get_resources_path():
    """Get the path to the resources directory."""
    base_path = os.path.abspath(__file__)
    main_folder_path = os.path.dirname(os.path.dirname(base_path))
    resources_path = os.path.join(main_folder_path, 'resources')

    if not os.path.exists(os.path.dirname(resources_path)):
        return "Error"
    return resources_path


def get_appdata_dir(subfolder_name=None):
    """Get the user data directory based on the platform."""
    appdata_dir = os.getenv('APPDATA')
    if not appdata_dir:
        raise EnvironmentError("متغير البيئة APPDATA غير محدد.")

    if subfolder_name:
        return os.path.join(appdata_dir, subfolder_name)
    return appdata_dir



def copy_resources_folder():
    """Copy the resources folder to the AppData directory if it doesn't exist."""
    source = get_resources_path()
    if source is None:
        return "Error: Resources folder not found."
    
    destination = get_appdata_dir('resources')

    if not os.path.exists(destination):
        try:
            shutil.copytree(source, destination)
            return f"Copied resources from {source} to {destination}"
        except Exception as e:
            return f"Error copying resources: {e}"

    return f"Resources already synchronized at {destination}."



def manager_Sqlite3(sub_dir, file_name):
    """ The function responsible for managing database files in the APPDATA folder """
    appdata_dir = os.getenv('APPDATA')
    path_resources = os.path.join(appdata_dir, 'resources', sub_dir, file_name)

    if not os.path.exists(os.path.dirname(path_resources)):
        os.makedirs(os.path.dirname(path_resources), exist_ok=True)
    return path_resources



def manager_Images(sub_dir, file_name):
    """ The function responsible for managing the images used in the application """
    appdata_dir = os.getenv('APPDATA')
    path_resources_images = os.path.join(appdata_dir, 'resources', sub_dir, file_name)
    if not os.path.exists(os.path.dirname(path_resources_images)):
        os.makedirs(os.path.dirname(path_resources_images))
    return path_resources_images

