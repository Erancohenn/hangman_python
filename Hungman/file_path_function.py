import os


def get_path(file_name):
    """
    This function gives an absolute path to the wanted file
    :param file_name: the name of the file
    :return: absolute path
    :rtype: str
    """
    script_dir = os.path.dirname(__file__)
    rel_path = file_name
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path