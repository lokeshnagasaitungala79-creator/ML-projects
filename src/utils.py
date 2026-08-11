import os
import sys
import pickle
import dill

from src.exception import CustomException

def save_object(file_path: str, obj: object) -> None:
    """
    Saves a Python object to disk using dill.
    
    Creates target directories if they do not exist and opens 
    the file in write-binary mode ('wb').
    """
    try:
        dir_path = os.path.dirname(file_path)

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)