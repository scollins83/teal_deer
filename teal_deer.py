import glob

def get_file_list(path, type='pdf'):
    """
    Gets a list of files of the directory of pdfs.
    :param path: Directory path
    :return: List of files.
    """
    path += ('*.' + type)
    return glob.glob(path)