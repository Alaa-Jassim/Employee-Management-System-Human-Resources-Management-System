





import os
import sqlite3


def database_vacations_employee(db_name):
    """Create or access the SQLite database in the 'resources/send_message' folder."""
    
    # Get the path to the directory where this script is located
    base_path = os.path.dirname(__file__)
    
    # Define the path to the 'resources/database_employees' directory
    resources_path = os.path.join(base_path, '..', 'resources', 'database_vacations')
    
    # Create the 'database_employees' directory if it does not exist
    os.makedirs(resources_path, exist_ok=True)
    
    # Define the full path to the database file
    db_path = os.path.join(resources_path, db_name)
    return db_path
